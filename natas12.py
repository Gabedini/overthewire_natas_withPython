#!/usr/bin/env python

import requests
import re

username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'
url = 'http://%s.natas.labs.overthewire.org/' % username

"""Starting with our default stuff"""
response = requests.get(url, auth = (username, password))
content = response.text
print(content)