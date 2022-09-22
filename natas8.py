#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'
url = 'http://%s.natas.labs.overthewire.org/' % username
#print(url) #make sure the URL works fine

#main page describes a view source page: index-source.html....turns out to be php again which sublime doesn't format, checking webpage
#found the below php script
#<?
#
#$encodedSecret = "3d3d516343746d4d6d6c315669563362";
#
#function encodeSecret($secret) {
#    return bin2hex(strrev(base64_encode($secret))); #so we see base64, then reverse, then hextobin to undo secret
#}
#
#if(array_key_exists("submit", $_POST)) {
#    if(encodeSecret($_POST['secret']) == $encodedSecret) {
#    print "Access granted. The password for natas9 is <censored>";
#    } else {
#    print "Wrong secret";
#    }
#}
#?>
#Also another input secret form

#John Hammond does this in PHP but I'm just going to steal a solution for directly in python from online
import base64
import binascii
encodedSecret = '3d3d516343746d4d6d6c315669563362'
secret = base64.b64decode(binascii.unhexlify(encodedSecret)[::-1])
#print(secret) #printed b and oubWYf2kBq ? It works though so let's modify posting that secret

session = requests.Session()

response = requests.post(url, data = {"secret": "oubWYf2kBq", "submit" : "submit"}, auth = (username, password))

content = response.text


######################
#print(content)

#classic regexing
print(re.findall('The password for natas9 is (.*)', content))