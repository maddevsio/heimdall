import os

import requests

"""
Usage:
Input: github/maddevsio/neureal-test-token
1. Split to: source, owner, repo
2. Search all solidity files
3. Grab solidity file content
4. Pass path to content to analyzer
"""
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_REPOS_API = 'https://api.github.com/repos'

CONTRACT_FILE = 'contract.sol'


def github_fetch_smart_contracts(owner, repo):
    repository_files = repository_tree(owner, repo)
    smart_contracts = filter(lambda x: x['path'].endswith('.sol'), repository_files['tree'])
    return [write_contracts(owner, repo, contract['path']) for contract in smart_contracts]


def repository_tree(owner, repository):
    url = f'{GITHUB_REPOS_API}/{owner}/{repository}/git/trees/master?recursive=1'
    response = requests.get(url, headers={
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.raw',
    })
    return response.json()


def fetch_github_contract(owner, repository, path):
    url = f'{GITHUB_REPOS_API}/{owner}/{repository}/contents/{path}'
    response = requests.get(url, headers={
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.raw',
    })
    return response.content


def write_contracts(owner, repository, path):
    smart_contract = fetch_github_contract(owner, repository, path)
    with open(path.split('/')[-1], 'wb+') as f:
        f.write(smart_contract)
    return f.name
