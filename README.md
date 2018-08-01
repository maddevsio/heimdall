# Mythril scanner

Tool for analyzing smart contracts using mythril

### Features:

- [x] Analyze neureal repo
- [ ] Add health badge
- [ ] Add input for getting repo badge


### Deployment:

1. Install [mythril](https://github.com/ConsenSys/mythril/wiki/Installation-and-Setup)

2. Install project dependencies:   
 `$ pip install -r requirements.txt`

3. Go to project scanner dir  
`$ cd scanner`

4. Create github personal token:  
[https://github.com/settings/tokens](https://github.com/settings/tokens)
4. Run ginicorn:   
Temporary define large timeout, will be fixed:   
`$ gunicorn main -e GITHUB_TOKEN=<token_here> -t 200 --reload`

