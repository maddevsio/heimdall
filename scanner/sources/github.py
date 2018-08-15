import os

import requests


GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_REPOS_API = 'https://api.github.com/repos'
BLACK_LIST = [
    'Migrations.sol',
]

async def github_fetch_smart_contracts(owner, repo):
    repository_files = await repository_tree(owner, repo)
    smart_contracts = []
    for item in repository_files.get('tree'):
        contract = item.get('path')
        if contract:
            contract = contract.split('/')[-1]

        if contract.endswith('.sol') and contract not in BLACK_LIST:
            smart_contracts.append(item)
    return [await write_contracts(owner, repo, contract['path']) for contract in smart_contracts]


async def repository_tree(owner, repository):
    url = f'{GITHUB_REPOS_API}/{owner}/{repository}/git/trees/master?recursive=1'
    response = requests.get(url, headers={
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.raw',
    })
    return response.json()


async def fetch_github_contract(owner, repository, path):
    url = f'{GITHUB_REPOS_API}/{owner}/{repository}/contents/{path}'
    response = requests.get(url, headers={
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.raw',
    })
    return response.content


async def write_contracts(owner, repository, path):
    smart_contract = await fetch_github_contract(owner, repository, path)
    with open(path.split('/')[-1], 'wb+') as f:
        f.write(smart_contract)
    return f.name
