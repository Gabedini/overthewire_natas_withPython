#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
url = 'http://%s.natas.labs.overthewire.org/' % username
#print(url) #make sure the URL works fine


session = requests.Session()

response = session.get(url, auth = (username, password))
content = response.text


######################
print(content)

#classic regexing
#print(re.findall('Output:\n<pre>\n(.*)\n</pre>', content))