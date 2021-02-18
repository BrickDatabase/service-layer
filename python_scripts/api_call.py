##############################################
# Author:                                    #
# Edward Riley & Joel Parker  #
##############################################

import requests
import json


# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('5H8SluqMBijdSA', 'wZAjkKUXYRMD02YnA7XTcKiie3-OaQ')
# here we pass our login method (password), username, and password

data = {'grant_type': 'password',
        'username': 'EuropaReport3',
        'password': 'Dare8devil'}
# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'EuropaReport/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# personal use script
# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
'https://www.reddit.com/dev/api/oauth/'

# while the token is valid (~2 hours) we just add headers=headers to our requests
response = requests.get('https://oauth.reddit.com/subreddits/popular', headers=headers)

# converts to JS
responseJSON = json.loads(response.content)
prettyJSON = json.dumps(responseJSON, indent=2)

print(prettyJSON)
