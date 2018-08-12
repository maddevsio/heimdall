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
import operator, functools


FIREBASE_CERTIFICATE = os.environ.get('FIREBASE_CERTIFICATE')
FIREBASE_DATABASE = os.environ.get('FIREBASE_DATABASE')

cred = credentials.Certificate(FIREBASE_CERTIFICATE)
firebase_admin.initialize_app(cred, {
    'databaseURL' : FIREBASE_DATABASE
})


root = db.reference()

def get_report_status(issues):
    if not issues:
        return 'passed'

    data = [issue['type'] for issue in issues]
    if 'Warning' in data:
        return 'Warning'
    
    if 'Informational' in data:
        return 'Informational'


def get_report_status_full(result):
    data = [item['status'] for item in result]
    print(data)
    if 'Warning' in data:
        return 'critical'
    if 'Informational' in data:
        return 'minor'
    return 'passed'

def generate_report(owner, repo):
    smart_contracts = github_fetch_smart_contracts(owner, repo)
    result = []
    for smart_contract in smart_contracts:
        try:
            report = mythril_scanner(smart_contract)
            data = json.loads(report.as_json())
            status = get_report_status(data.get('issues'))
            result.append({'file': smart_contract, 'data': data, 'status': status})
        except Exception as e:
            # Looks like it is not smart contract
            pass
    status = get_report_status_full(result)
    root.child(f'{owner}/{repo}').update({'report': result, 'badge': status})
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
    report = report_get_or_create(owner, repo)
    return web.Response(
        body=badge_generator(report['badge']),
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
    report = report_get_or_create(owner, repo)
    return {
        'mythril': report,
        'owner': owner,
        'repo': repo
    }

async def report_view_json(request):
    owner = request.match_info['owner']
    repo = request.match_info['repo']
    report = report_get_or_create(owner, repo)
    return web.json_response({
        'mythril': report,
        'owner': owner,
        'repo': repo
    })
