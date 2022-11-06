import requests as r
import json
import os

headers = {'content-type': 'application/json', 'Authorization':'{}'.format(os.environ.get('strapi_token'))}

data = {
            "String": 'brasil campeone de futebol'
    }

data = json.dumps(data)

res = r.post('http://208.85.21.227:1337/Tests', data=data, headers=headers).json()
print(res)
