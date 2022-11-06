import requests as r
import json
import os

headers = {'content-type': 'application/json', 'Authorization':'{}'.format(os.environ.get('strapi_token'))}

data = {
            "String": 'I am just gonna put this here'
    }

data = json.dumps(data)

res = r.put('http://208.85.21.227:1337/Tests/1', data=data, headers=headers).json()
print(res)
