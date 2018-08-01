import json
from aiohttp import web
from analyzer.mythrilapp import mythril_scanner
from sources.github import fetch_github_contract

async def scan(request):
    contract_path = fetch_github_contract()
    report = mythril_scanner(contract_path)
    return web.json_response(json.loads(report.as_json()))