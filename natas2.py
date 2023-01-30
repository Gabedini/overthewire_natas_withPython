#!/usr/bin/env python

#using requests module for python to pull the pages.
import requests
import re

"""Notice for this level the URL is different, has items on the end"""
username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
"""After pulling the original page,
url = 'http://%s.natas.labs.overthewire.org/' % username
we noticed that there was no password on that page as before.
However, there is a picture stored at a /files directory. We could pull that?
url = 'http://%s.natas.labs.overthewire.org/files/' % username
And look at that, more files, one being a text file so why not print that out?
"""
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username #investigating the text file in /files

#make sure the URL works fine
#print(url) #not needed right now, commented

#grab the page
response = requests.get(url, auth = (username, password))
content = response.text
print(content)

#regex needed to be slightly different than the last level
print(re.findall('natas3:(.*)', content))

"""SDG"""