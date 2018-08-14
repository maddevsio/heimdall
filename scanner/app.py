import functools
import json
import logging
import operator
import os

import aiohttp_jinja2
import firebase_admin
from aiohttp import web
from firebase_admin import credentials, db

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
    if 'Warning' in data:
        return 'critical'
    if 'Informational' in data:
        return 'minor'
    return 'passed'

def generate_report(owner, repo):
    smart_contracts = github_fetch_smart_contracts(owner, repo)
    logging.info(f'[github/{owner}/{repo}] Fetch smart contracts {smart_contracts}')
    result = []
    try:
        for smart_contract in smart_contracts:
            report = json.loads(mythril_scanner(smart_contract))
            print('=' * 10)
            print(type(report))
            print('=' * 10)
            status = get_report_status(report.get('issues'))
            result.append({'file': smart_contract, 'data': report, 'status': status})
    except Exception as e:
        logging.error(f'[github/{owner}/{repo}] {e}')
    status = get_report_status_full(result)
    root.child(f'{owner}/{repo}').update({'report': result, 'badge': status})
    return result


def report_get_or_create(owner, repo):
    report = db.reference(f'{owner}/{repo}').get()
    logging.info(f'[github/{owner}/{repo}] Firebase Report Cache: {report}')
    if not report:
        logging.info(f'[github/{owner}/{repo}] Start report processing')
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
    logging.info(f'[github/{owner}/{repo}] Request report')
    report = report_get_or_create(owner, repo)
    logging.info(f'[github/{owner}/{repo}] Report sended')
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
