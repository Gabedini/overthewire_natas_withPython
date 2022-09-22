#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'
url = 'http://%s.natas.labs.overthewire.org/' % username
#print(url) #make sure the URL works fine

session = requests.Session()

response = requests.get(url, auth = (username, password))
content = response.text


######################
print(content)

#classic regexing
#print(re.findall('Output:\n<pre>\n(.*)\n</pre>', content))