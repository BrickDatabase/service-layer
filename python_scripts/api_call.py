import requests
import json

link = "https://www.reddit.com/reddits.json?limit=99999"
response = requests.get(link, headers = {'User-agent': 'your bot 0.1'})

responseJSON = json.loads(response.content)
print(responseJSON)