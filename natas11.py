#!/usr/bin/env python

#using requests module for python, not sure if I will need to install anything for this?
import requests
import re



username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
url = 'http://%s.natas.labs.overthewire.org/' % username
#print(url) #make sure the URL works fine


session = requests.Session()
response = session.get(url, auth = (username, password))#reeeeeeee make sure you don't have requests.get or cookies won't return
print(session.cookies)
content = response.text


######################
#print(content)

print(session.cookies)#can use this to view cookies on the page
#<RequestsCookieJar[<Cookie data=MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D for natas11.natas.labs.overthewire.org/>]>
#can scrape the cookie data only with but it displays goofy (the data is clearly the password, which makes sense from the php on /index-source.html)
print(session.cookies['data'])

import urllib
#new python module for the this next one: urllib
#this lets us see the base64 wihtout the %3d at the end ((note, had to inlcude .parse, not all pythons/compilers require it? not sure))
print(urllib.parse.unquote(session.cookies['data']))

import base64
#so now that we have that, we can start the decode process as shown on /index-source.html with base64 first, adding module above
#print(base64.b64decode(urllib.parse.unquote(session.cookies['data'])))#returns garbled nonsense, aka out XOR'd data
#yeah so we're going to put this into hex
#I tried 123873827 versions of this command, reading the YT comments revealed .hex() is the way to go and not .encode('hex')
print(base64.b64decode(urllib.parse.unquote(session.cookies['data'])).hex())
#ok so we're gonna take that over to the PHP file and mess with that
#value: 306c3b242439382d383d3f23392a6a766920276e676c2a2b28212423396c726e68282e2a2d282e6e36


#———————————————————————————————————————
#so we're back from php and we have the cookie data of MGw7JCQ5FzwqPTs7JDwsbnFsMSk4bGRuKSkrIychOm5xbGsqLSguKi1sNQ==
#guessing we'll just ignore the == and toss that into the cookie and see what happens
cookies = { "data" : "MGw7JCQ5FzwqPTs7JDwsbnFsMSk4bGRuKSkrIychOm5xbGsqLSguKi1sNQ" }
response = session.get(url, auth = (username, password), cookies = cookies)#cookies being the item being passed and the value from our variable

content = response.text

print(content)

#pasting the XOR function from the PHP below, I think we might have to reverse this in PHP, natas11.php?
# ———————————————————————————————————————
#function xor_encrypt($in) {
#    $key = '<censored>';
#    $text = $in;
#    $outText = '';
#
#    // Iterate through each character
#    for($i=0;$i<strlen($text);$i++) {
#    $outText .= $text[$i] ^ $key[$i % strlen($key)];
#    }
#
#    return $outText;
#}
# ———————————————————————————————————————

#classic regexing
#print(re.findall('Output:\n<pre>\n(.*)\n</pre>', content))

"""SDG"""