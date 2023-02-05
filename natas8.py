#!/usr/bin/env python

import requests
import re

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'
url = 'http://%s.natas.labs.overthewire.org/' % username


"""Starting with our default stuff"""
#response = requests.get(url, auth = (username, password))
#content = response.text
#print(content)
"""main page describes a view source page: index-source.html....turns out to be php again which sublime doesn't format real well
It does format it legibly if you use a mix of setting to xml/html formatting, then use htmlbeautify and html/xml deentitize functions, but the browser exists for a reason"""
#response = requests.get(url + "index-source.html", auth = (username, password))
#content = response.text
#print(content) 
"""found the below php script
<?
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret))); #so we see base64, then reverse, then hextobin to undo secret
}
if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>

If you're following the John Hammond videos, he does it in PHP. However, this can be done in Python just the same.
https://docs.python.org/3/library/base64.html
https://docs.python.org/3/library/binascii.html and https://stackoverflow.com/questions/2072351/python-conversion-from-binary-string-to-hexadecimal"""
import base64
import binascii
encodedSecret = '3d3d516343746d4d6d6c315669563362'
secret = base64.b64decode(binascii.unhexlify(encodedSecret)[::-1])
"""this prints b'oubWYf2kBq' which I think we only want the part in quotes. It might be my formatting of the binascii part, I'm not entirely sure."""
print(secret)

"""We can submit this the same we we did for natas6, it didn't work inline in that challenge, but it seems to work fine putting it inline now"""
session = requests.Session()
response = requests.post(url, data = {"secret": "oubWYf2kBq", "submit" : "submit"}, auth = (username, password))
content = response.text

######################
print(content)

#classic regexing
print(re.findall('The password for natas9 is (.*)', content))

"""SDG"""




