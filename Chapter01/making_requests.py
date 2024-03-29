__author__ = 'Chetan'

import requests
r = requests.get('http://ip.jsontest.com/')
print("Response object:", r)
print("Response Text:", r.text)

payload = {'q': 'chetan'}
r = requests.get('https://github.com/search', params=payload)
print("Request URL:", r.url)

#
payload = {'key1': 'value1'}
r = requests.post("http://httpbin.org/post", data=payload)
print("Response text:", r.json())

try:
    r = requests.get("http://www.google.com/")
except requests.exceptions.RequestException as e:
    print("Error Response:", e.message)