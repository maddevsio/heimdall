import os
import json
import firebase_admin
import aiohttp_jinja2

from aiohttp import web
from firebase_admin import db
from firebase_admin import credentials
from analyzer.mythrilapp import mythril_scanner

from badge import badge_generator
from sources.github import github_fetch_smart_contracts


FIREBASE_CERTIFICATE = os.environ.get('FIREBASE_CERTIFICATE')
FIREBASE_DATABASE = os.environ.get('FIREBASE_DATABASE')

cred = credentials.Certificate(FIREBASE_CERTIFICATE)
firebase_admin.initialize_app(cred, {
    'databaseURL' : FIREBASE_DATABASE
})


root = db.reference()


def generate_report(owner, repo):
    smart_contracts = github_fetch_smart_contracts(owner, repo)
    result = []
    for smart_contract in smart_contracts:
        try:
            report = mythril_scanner(smart_contract)
            data = json.loads(report.as_json())
            result.append({'file': smart_contract, 'data': data})
        except Exception:
            # Looks like it is not smart contract
            pass
    root.child(f'{owner}/{repo}').update({'report': result})
    return result


def report_get_or_create(owner, repo):
    report = db.reference(f'{owner}/{repo}').get()
    if not report:
        generate_report(owner, repo)
        report = db.reference(f'{owner}/{repo}').get()
    return report


async def badge_view(request):
    owner = request.match_info['owner']
    repo = request.match_info['repo']
    # owner, repo
    report = report_get_or_create(owner, repo)
    status = 'critical' if report.get('issues') else 'passed'
    return web.Response(
        body=badge_generator(status),
        content_type='image/svg+xml',
        headers={'Cache-Control': 'no-cache', 'Expires': '0'}
    )


@aiohttp_jinja2.template('homepage.jinja2')
async def homepage(request):
    return {}


@aiohttp_jinja2.template('report.jinja2')
async def report_view(request):
    owner = request.match_info['owner']
    repo = request.match_info['repo']
    # GET owner, repo
    report = report_get_or_create(owner, repo)
    return {
        'mythril': report
    }