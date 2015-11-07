__author__ = 'gaoce'

import httplib, urllib
import json
params = {
    'id': '12345'
}

params = json.dumps(params)

headers = {"Content-type": "application/json", "Accept": "text/plain"}

conn = httplib.HTTPConnection("localhost", 5000)
conn.request("POST", "/poll", params, headers)
response = conn.getresponse()
print response.status, response.reason, response.read()