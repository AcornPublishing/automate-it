__author__ = 'Chetan'

import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = 'cjgiridhar'
api_token = '77c7f875ecff38199f39d41838ee4a19a513e445'
gist_id = 'de7cd21746ef39677c63ab3bc1b29b14'

header = {  'X-Github-Username': '%s' % username,
            'Content-Type': 'application/json',
            'Authorization': 'token %s' % api_token,
}

url = "/gists/%s" % gist_id
r = requests.delete('%s%s' %(BASE_URL, url),
                 headers=header,
)
print r