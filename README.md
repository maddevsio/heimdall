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
5. Setup firebase connection:   
*FIREBASE_CERTIFICATE*   
Take certificate from Project Settings -> Service account -> Generate new private key
Place this certificate inside project root.
*FIREBASE_DATABASE*   
Database url from Firebase real-time database settings.
6. Run ginicorn:   
Temporary define large timeout, will be fixed:   
`$ gunicorn main -e GITHUB_TOKEN=<token_here> -e FIREBASE_CERTIFICATE=<FIREBASE_CERTIFICATE_PATH> -e FIREBASE_DATABASE=<FIREBASE_DATABASE> -t 200 --reload`

