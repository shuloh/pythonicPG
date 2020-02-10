import requests

#get
url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)
print(response.text.encode('utf8'))
#post url encoded form
url = "https://en5m1hsutnp5m.x.pipedream.net"
payload = "foo_key=foo_value"
headers= {"Content-Type":"application/x-www-form-urlencoded"}
response = requests.request("POST", url, headers=headers, data = payload)
print(response.text.encode('utf8'))
#post json content body
payload = {"foo_key" : "foo_value"}
response = requests.request("POST", url, json = payload)
print(response.text.encode('utf8'))