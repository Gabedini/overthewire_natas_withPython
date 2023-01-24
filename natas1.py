#!/usr/bin/env python

"""
Welcome to the natas solutions! The objective is to find the password for the next level in the webpages.
"""

#using requests module for python to pull the pages.
import requests
import re

"""Assigning username/password variables,
as well as inserting the username into the URL for our level to save us an extra step.
"""
username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'
url = 'http://%s.natas.labs.overthewire.org/' % username

#make sure the URL works fine
print(url)

#gettings the webpage and authenticating using the username and password.
response = requests.get(url, auth = (username, password))

#notice, the response is simply the return code.
print(response, "<---------response")

#Getting the page xml from the response so we have more than just status code of the request.
content = response.text

#printing the page
print(content)

#regexing out everything but the password.
print(re.findall('<!--The password for natas2 is (.*) -->', content))

#SDG