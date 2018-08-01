
import requests
import os


GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
CONTRACT_FILE = 'contract.sol'
# TODO: remove hardcode
CONTRACT_URL = 'https://api.github.com/repos/neureal/neureal-token-test/contents/contracts/TESTToken.sol'


def fetch_github_contract():
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.raw',
    }
    response = requests.get(CONTRACT_URL, headers=headers)
    with open(CONTRACT_FILE, 'wb+') as f:
        f.write(response.content)
    return f.name
