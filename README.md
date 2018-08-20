# Heimdall   
[![CircleCI](https://circleci.com/gh/maddevsio/heimdall/tree/master.svg?style=svg)](https://circleci.com/gh/maddevsio/heimdall/tree/master)  
Tool for analyzing smart contracts using mythril

Demo:  
[![Heimdall Scanner](https://heimdall.maddevs.io/badge/github/maddevsio/heimdall)](https://heimdall.maddevs.io/report/github/maddevsio/heimdall)   

### Usage:

### Deployment:  
1. Install [mythril](https://github.com/ConsenSys/mythril/wiki/Installation-and-Setup) via pypi
Mythril require additional setup doc from mythril source code:
```
Whenever you disassemble or analyze binary code, Mythril will try to
resolve function names using its local signature database. The database
must be provided at ``~/.mythril/signatures.json``. You can start out
with the `default file <signatures.json>`__ as follows:
::
    $ cd ~/.mythril
    $ wget https://raw.githubusercontent.com/b-mueller/mythril/master/signatures.json
::
```
2. Install project dependencies:   
 `$ pip install -r requirements.txt`
3. Go to project scanner dir  
`$ cd scanner`
4. Create github personal token:  
[https://github.com/settings/tokens](https://github.com/settings/tokens)
5. Setup firebase connection:   
- **FIREBASE_CERTIFICATE**   
Take certificate from Project Settings -> Service account -> Generate new private key   
Place this certificate inside project root.   
- **FIREBASE_DATABASE**   
Database url from Firebase real-time database settings.
6. Run ginicorn:   
Temporary define large timeout, will be fixed:   
`$ gunicorn main:run --bind localhost:8000 --worker-class aiohttp.GunicornWebWorker -e GITHUB_TOKEN=<token_here> -e FIREBASE_CERTIFICATE=<FIREBASE_CERTIFICATE_PATH> -e FIREBASE_DATABASE=<FIREBASE_DATABASE> -t 200 --reload`

