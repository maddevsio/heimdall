import json
import requests
import os

from aiohttp import web
from mythril.analysis.symbolic import SymExecWrapper
from mythril.ether.soliditycontract import SolidityContract
from mythril.analysis.security import fire_lasers
from mythril.analysis.report import Report 


GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
CONTRACT_FILE = 'contract.sol'
ADDRESS = "0x0000000000000000000000000000000000000000"

async def scan(request):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.raw',
    }
    # Hardcode contract address
    url = 'https://api.github.com/repos/neureal/neureal-token-test/contents/contracts/TESTToken.sol'
    response = requests.get(url, headers=headers)
    with open(CONTRACT_FILE, 'wb+') as f:
        f.write(response.content)
    contract = SolidityContract(CONTRACT_FILE)
    sym = SymExecWrapper(contract, address=ADDRESS, strategy="dfs")
    issues = fire_lasers(sym)
    report = Report()
    for issue in issues:                                           
        issue.filename = "test-filename.sol"
        report.append_issue(issue)
    result = json.loads(report.as_json())
    return web.json_response(result)