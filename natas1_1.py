#!/usr/bin/env python
print('howdy')

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas0'
password = username
url = 'http://%s.natas.labs.overthewire.org/' % username

print(url) #make sure the URL works fine

#response = request.get(url)
#print(response) #this will return a 401 since we didn't includ creds

response = requests.get(url, auth = (username, password))
#print(response.text)
content = response.text

#getting fancy here, regexing out the context
print(re.findall('<!--The password for natas1 is (.*) -->', content))