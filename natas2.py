#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
url = 'http://%s.natas.labs.overthewire.org/files' % username
#investigating the /files directory we saw when pulling the whole page
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username
#investigating the text file in /files


print(url) #make sure the URL works fine

response = requests.get(url, auth = (username, password))
content = response.text
######################
#print(content)

print(re.findall('natas3:(.*)', content))