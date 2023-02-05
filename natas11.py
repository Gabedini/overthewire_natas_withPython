#!/usr/bin/env python

import requests
import re

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username

"""Starting with our default stuff"""
#response = requests.get(url, auth = (username, password))
#content = response.text
#print(content)


"""Things of note right away, looks like we're setting a background color now on the webpage instead of returning something...ok
Probably more importantly, we see: "Cookies are protected with XOR encryption"

Before we get too crazy, let's just pull the cookies real quick:"""
session = requests.Session()
response = session.get(url, auth = (username, password))
#print(session.cookies)
"""<RequestsCookieJar[<Cookie data=MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D for natas11.natas.labs.overthewire.org/
]

So, I am guessing that that string is what's encrypted in our data, if we can un-xor-ecnrypt that we might be able to do something?

Next, let's check out what's going on behind the scenes and view our sourcecode"""
#response = requests.get(url + "index-source.html", auth = (username, password))
#content = response.text
#print(content)
"""Ok, alright ok - this one is significantly more complicated, let's see if we can pull some logic out of it, though
I think this is the important part: 
<?
if($data["showpassword"] == "yes")  {
        print "The  password  for  natas12  is  <censored
<br
";
}

?
So yes, if we can get it to accept what we send it, ie if it runs our supplied cookie through it's PHP function and it comes out as 'yes'
then we will get the password


Ok, so that's great, but how do we do that?
Well, so the first thing of note is what is xor encrypting? https://www.101computing.net/xor-encryption-algorithm/
tl;dr is that it's this function, you can see it in the php a ^ b = c
In other words, our plaintext ^ key = ciphertext
Now this is a simple algebra math problem, the fun thing is, this is easily reversed
So, if we have the items we want, we can do this to get the key: plaintext ^ ciphertext = key
and then produce the ciphertext that we want, which is the cookie being 'yes' then we can submit that with our request.

Now, if you wanted to use PHP, you could leverage the PHP code already written and reverse it, but that's getting into PHP and I don't care to mess with that.
So, we're going to do this entirely in Python.
There are a couple of additional things worth noting in that PHP though, beyond the xor_encrypt($in) function,
the loadData($d) fuction has this: json_decode(xor_encrypt(base64_decode($_COOKIE["data"])),true);
We also see a similar process further town doing that, so it's modifying the input to make it xor-able

We know we're going to need a few more modules, so let's get those in here:"""
import base64, urllib

"""We're going to try implementing our first function, here. https://www.w3schools.com/python/python_functions.asp"""
dataIn = ""
key = ""
def xor_encrypt(dataIn, key)
        for i,j in dataIn, key
                i = ord(i)
                i = int(i)
                







defaultdata = { "showpassword" : "yes", "bgcolor" : "#ffff00"}
cookies = { "showpassword" : "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D" }
response = session.get(url, auth = (username, password), cookies = defaultdata)
content = response.text
print(content)


######################
#print(content)
"""
print(session.cookies)#can use this to view cookies on the page
#<RequestsCookieJar[<Cookie data=MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D for natas11.natas.labs.overthewire.org/
]

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
#    $key = '<censored
';
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
#print(re.findall('Output:\n<pre
\n(.*)\n</pre
', content))
"""


"""SDG"""