#!/usr/bin/env python

import requests
import re
import base64
import urllib
import codecs

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
url = 'http://%s.natas.labs.overthewire.org/' % username
"""See the natas11.py for the explanation of the solution. I will only comment the parts that are 
doing something differently over here

One thing that is done differently in this file is the use of f-strings. Due to changes in python 3 in how it handles data types
f strings are useful, notice how we're able to append non-string data types to our strings with this method
https://realpython.com/python-f-strings/"""

session = requests.Session()
response = session.get(url, auth = (username, password))
content = response.text

"""Let's pull the cookie(s) real quick:"""
print(f"This is the cookie as a dictionary data type: {session.cookies.get_dict()}")

"""Looks like we might need just the 'data' value, so let's get that now
The urllib step removes the extra characters at the end of the data value"""
rawCookie = urllib.parse.unquote(session.cookies["data"])
print("this is the cookie after removing the URL encoding characters at the end: " + rawCookie)

"""This step base64 decodes the value which is then the raw data."""
encryptedDefaultData = base64.b64decode(rawCookie)
print(f"This is the value of 'data' in the cookie with no b64 encoding applied: {encryptedDefaultData}")

"""Note: the .decode() removes the b"123456" in the variable being passed. https://btechgeeks.com/how-to-remove-b-in-front-of-string-in-python/
The b indicates that it's a byte object, for our use case, it's in the way"""
unencodedDefaultData = encryptedDefaultData.decode()
print(f"This is the value of 'data' now that we removed the byte object encoding: {unencodedDefaultData}")

key = ""
defaultDataPlaintext = "{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}"
print(f"Here we have our default plaintext: {defaultDataPlaintext}")

def findKey():
	global defaultDataPlaintext
	global key
	"""not sure if we have used len() before, it just returns length as you might have guess already
	It just so happens that our defaultDataPlaintext and the unencodedDefaultData are the same lenght. Additional care may be needed
	if they did not match up, I presume that was intentional by the creators of the level.
	However, we really only need this to iterate 4 times as that's the lenght of the key and the rest just repeats"""
	for x in range(0, len(unencodedDefaultData)):
		"""the next line is for debugging"""
		#print(f"handling: {chr(ord(unencodedDefaultData[x]))} : {chr(ord(defaultDataPlaintext[x]))}: {chr(ord(unencodedDefaultData[x]) ^ ord(defaultDataPlaintext[x]))} : index: {x}")
		key += chr(ord(unencodedDefaultData[x]) ^ ord(defaultDataPlaintext[x]))
	return key
findKey()
"""I don't think the logic makes sense for string slicing, but we do need 4 for this to get 0-3 indices?
https://www.w3schools.com/python/python_strings_slicing.asp
We only need the first four digits of the key to use below"""
print(f"Here is our key: {key.encode('utf-8').decode()[:4]}")


global newCookieSaysYes
newCookieSaysYes = "{\"showpassword\":\"yes\",\"bgcolor\":\"#ffffff\"}"
print(newCookieSaysYes)
global newEncryptedCookie
newEncryptedCookie = ""
def makeNewData():
	global key
	global newCookieSaysYes
	global newEncryptedCookie
	for x in range(0, len(newCookieSaysYes)):
		newEncryptedCookie += chr(ord(newCookieSaysYes[x]) ^ ord(key[x % 4]))
		"""the next line is for debugging"""
		#print(f"handling: {x} : {key[x % 4]} : {chr(ord(newCookieSaysYes[x]) ^ ord(key[x % 4]))}    index: {x}")
makeNewData()
print(f"Now that we've XOR'd our 'yes' data we have: {newEncryptedCookie}")

"""yes the .encode .decode is in fact needed, we need to encode it into bytes object but then it adds the b"" thing again so we remove that with decode"""
b64YesCookie = base64.b64encode(newEncryptedCookie.encode()).decode()
print(f"How about that base64 though?: {b64YesCookie}")

"""you wouldn't think we need to recreate the session. But if we don't, it just re-passes the default info from before"""
session = requests.Session()
superSecureCookie = { "data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz" }
response = session.get(url, auth = (username, password), cookies = superSecureCookie)
content = response.text
print(content)
print(response)




"""SDG"""