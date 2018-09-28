import asyncio
import aioredis
import functools
import json
import logging
import operator
import os
import json

import aiohttp_jinja2
import firebase_admin
import requests
from aiohttp import web
from firebase_admin import credentials, db

from analyzer.mythrilapp import mythril_scanner
from badge import badge_generator
from sources.github import github_fetch_smart_contracts
from aiohttp_basicauth import BasicAuthMiddleware


auth = BasicAuthMiddleware(username=os.environ.get('HEIMDALL_USER'), password=os.environ.get('HEIMDALL_PASSWORD'), force=False)


FIREBASE_CERTIFICATE = os.environ.get('FIREBASE_CERTIFICATE')
FIREBASE_DATABASE = os.environ.get('FIREBASE_DATABASE')

cred = credentials.Certificate(FIREBASE_CERTIFICATE)
firebase_admin.initialize_app(cred, {
    'databaseURL' : FIREBASE_DATABASE
})

root = db.reference()


@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        if response.status != 404:
            return response
        message = response.message
    except web.HTTPException as ex:
        if ex.status != 404:
            raise
        message = ex.reason
    context = {'error': message}
    response = aiohttp_jinja2.render_template(
        'error.jinja2', request, context
    )
    response.headers['Content-Language'] = 'ru'
    return response


async def get_report_status(issues):
    if not issues:
        return 'passed'

    data = [issue['type'] for issue in issues]
    if 'Warning' in data:
        return 'Warning'

    if 'Informational' in data:
        return 'Informational'


async def get_report_status_full(result):
    data = [item['status'] for k, item in result.get('report', {}).items()]
    if 'Warning' in data:
        return 'critical'
    if 'Informational' in data:
        return 'minor'
    return 'passed'

async def mythril_firebase_logic(owner, repo, smart_contract, contract_hash):
    repository_path = f'{owner}/{repo}'
    try:
        report = json.loads(mythril_scanner(smart_contract))

        current_report = root.child(f'{repository_path}/report')
        item = {
            'key': contract_hash,
            'file': smart_contract,
            'data': report,
            'status': await get_report_status(report.get('issues')),
        }
        name_for_firebase = smart_contract.replace('.', '-')
        node = current_report.child(name_for_firebase)

        node.set(item)
        logging.info(f'[github/{owner}/{repo}] Report item: {item}')
    except Exception as e:
        logging.error(f'[github/{owner}/{repo}] Skipped exception: {e}')
        pass

async def generate_report(owner, repo):
    smart_contracts = await github_fetch_smart_contracts(owner, repo)

    repository_path = f'{owner}/{repo}'
    logging.info(f'[github/{repository_path}] Fetch smart contracts: {smart_contracts}')
    
    root.child(repository_path).update({'processing': True})
    for contract in smart_contracts:
        smart_contract = contract['name']
        contract_hash = contract['sha']
        replace_name = smart_contract.replace('.', '-')

        logging.info(f'[github/{owner}/{repo}] Processing contract: {smart_contract}')

        CONTRACT = f'{owner}/{repo}/report/{replace_name}'
        FIREBASE_CONTRACT = root.child(f'{owner}/{repo}/report/{replace_name}').get('key')

        if not db.reference(CONTRACT).get():
            await mythril_firebase_logic(owner, repo, smart_contract, contract_hash)
        else:
            if FIREBASE_CONTRACT[0]['key'] != contract_hash:
                db.reference(f'{owner}/{repo}/report').delete()
                await mythril_firebase_logic(owner, repo, smart_contract, contract_hash)
            else:
                logging.info(f'[github/{owner}/{repo}] The contract was not changed: {smart_contract}')
                pass

    report = root.child(repository_path).get()
    status = await get_report_status_full(report)
    logging.info(f'[github/{owner}/{repo}] status: {status}')
    root.child(repository_path).update({'badge': status, 'processing': False})
    return report


async def report_get_or_create(owner, repo):
    report = db.reference(f'{owner}/{repo}').get()
    logging.info(f'[github/{owner}/{repo}] Firebase Report Cache: {report}')
    if not report:  
        logging.info(f'[github/{owner}/{repo}] Start report processing')
        pub = await aioredis.create_redis(('localhost', 6379))
        res = await pub.publish_json('chan:1', {'owner': owner, 'repo': repo})
        pub.close()
        report = db.reference(f'{owner}/{repo}').get()
    return report

async def badge_view(request):
    owner = request.match_info['owner']
    repo = request.match_info['repo']
    await report_get_or_create(owner, repo)
    report = db.reference(f'{owner}/{repo}').get()
    badge = 'processing'
    if report:
        badge = report.get('badge', 'processing')
    return web.Response(
        body=badge_generator(badge),
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
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}')

    if response.status_code == 404:
        return {'error': 'Github repository does not exist', }

    await report_get_or_create(owner, repo)
    report = db.reference(f'{owner}/{repo}').get()
    logging.info(f'[github/{owner}/{repo}] Report sended')

    return {
        'mythril': report,
        'owner': owner,
        'repo': repo,
        'error': None
    }


async def report_view_json(request):
    owner = request.match_info['owner']
    repo = request.match_info['repo']
    report = await report_get_or_create(owner, repo)
    return web.json_response({
        'mythril': report,
        'owner': owner,
        'repo': repo
    })

@auth.required
@aiohttp_jinja2.template('worker_view.jinja2')
async def worker_view(request):
    return {
        'apiKey': os.environ.get('apiKey'),
        'authDomain': os.environ.get('authDomain'),
        'databaseURL': os.environ.get('databaseURL'),
        'projectId': os.environ.get('projectId'),
        'storageBucket': os.environ.get('storageBucket'),
        'messagingSenderId': os.environ.get('messagingSenderId'),
    }