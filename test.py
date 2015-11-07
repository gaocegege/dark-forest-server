import httplib, json
params = {
    'id': '12345',
    'missile': {
        'pos': {
            'x': 1,
            'y': 2
        },
        'vel': {
            'x': 1,
            'y': 2
        }
}}

params = json.dumps(params)

headers = {"Content-type": "application/json", "Accept": "text/plain"}

conn = httplib.HTTPConnection("localhost", 5000)
conn.request("POST", "/event", params, headers)
response = conn.getresponse()
print response.status, response.reason