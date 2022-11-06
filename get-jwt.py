import requests as r
import json

headers = {'content-type': 'application/json'}

user = json.dumps({
	"identifier":"USER_NAME",
	"password":"PASSWORD"
})

token = r.post('http://208.85.21.227:1337/auth/local', data=user, headers=headers).json()
print(token)
token = 'Bearer ' + token['jwt']
print(token)
