import requests

payload = {"user": "abhi", 'password': 'testing'}
r = requests.post("http://httpbin.org/post", data=payload)

res = r.json()
print(res['form'])