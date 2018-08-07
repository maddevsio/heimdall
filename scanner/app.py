import os
import json
import firebase_admin
import aiohttp_jinja2

from aiohttp import web
from firebase_admin import db
from firebase_admin import credentials
from analyzer.mythrilapp import mythril_scanner

from sources.github import fetch_github_contract
from badge import badge_generator


FIREBASE_CERTIFICATE = os.environ.get('FIREBASE_CERTIFICATE')
FIREBASE_DATABASE = os.environ.get('FIREBASE_DATABASE')

cred = credentials.Certificate(FIREBASE_CERTIFICATE)
firebase_admin.initialize_app(cred, {
    'databaseURL' : FIREBASE_DATABASE
})


root = db.reference()
REPO_NAME = 'neureal'


def report_get_or_create():
    report = db.reference(REPO_NAME).get()
    if not report:
        # TODO: send report generation to background task
        generate_report()
        report = db.reference(REPO_NAME).get()
    return report


def generate_report():
    contract_path = fetch_github_contract()
    report = mythril_scanner(contract_path)
    data = json.loads(report.as_json())
    root.child(REPO_NAME).update(data)
    return data


async def scan(request):
    data = generate_report()
    return web.json_response(data)


async def badge_view(request):
    status = 'passed'
    report = report_get_or_create()
    if report.get('issues'):
        status = 'critical'
    return web.Response(body=badge_generator(status), content_type='image/svg+xml')


@aiohttp_jinja2.template('report.jinja2')
async def report_view(request):
    report = report_get_or_create()
    return {
        'mythril': report
    }