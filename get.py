import requests as r
import json
import os

headers = {'content-type': 'application/json', 'Authorization':'{}'.format(os.environ.get('strapi_token'))}

# get specific entry with /1 at the end
res = r.get('http://208.85.21.227:1337/Tests/5', headers=headers).json()
print(res)
