import requests as r
import json

headers = {'content-type': 'application/json', 'Authorization':'{}'.format(os.environ.get('strapi_token'))}

# get specific entry with /1 at the end
res = r.delete('http://208.85.21.227:1337/Tests/1', headers=headers).json()
print(res)
