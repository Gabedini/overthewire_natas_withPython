#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'
url = 'http://%s.natas.labs.overthewire.org/' % username

print(url) #make sure the URL works fine

response = requests.get(url, auth = (username, password))
content = response.text
######################
print(content)

print(re.findall('<!--The password for natas2 is (.*) -->', content))