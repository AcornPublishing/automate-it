__author__ = 'Chetan'

import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = 'cjgiridhar'
api_token = '77c7f875ecff38199f39d41838ee4a19a513e445'
header = {  'X-Github-Username': '%s' % username,
            'Content-Type': 'application/json',
            'Authorization': 'token %s' % api_token,
}

url = "/gists"
data = {
  "description": "the description for this gist",
  "public": True,
  "files": {
    "file3.txt": {
      "content": "String file contents"
    }
  }
}

r = requests.post('%s%s' % (BASE_URL, url),
        headers=header,
        data=json.dumps(data))
print r.json()['url']