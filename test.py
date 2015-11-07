import httplib, urllib
params = urllib.urlencode({
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
}})

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

conn = httplib.HTTPConnection("localhost", 5000)
conn.request("POST", "/event", params, headers)
response = conn.getresponse()
print response.status, response.reason