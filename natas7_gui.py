#!/usr/bin/env python

"""just leaving these here for demoing purposes
username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'
"""

"""GUI README:
Hey y'all, so this is going to be the first foray into making a GUI with Python, trying to keep it functional, but simple.
The number one goal for this one is to simply to make it easy to follow, for learning's sake.
However, do not think that this is the PROPER way to do this, this is an ultra simplistic and, honestly, probably a bad way of doing it.
I would highly recommend only doing 1-2 scripts/programs this way before looking at the below page to learn some more about writing
in a more readable and scalable format:
https://github.com/TomSchimansky/CustomTkinter/wiki/App-structure-and-layout
Anyway, that's just the warning, you do with it what you like, but I just don't want us to get too used to writing improperly.
We get a pass for this first one since we're just playing around with what's possible to spark the imagination and really SEE progress.
"""

import requests
import re

"""We need to set these to global so they can be accessed within the login() method below"""
global usernm
global passwd
global content
"""I am unsure if I am doing it improperly or if this is the only way to initialize these.
It didn't seem to be able to be able to use 'content' until I defined it up here."""
usernm = 'wrong' 
passwd = 'creds'
content = 'you haven\'t gotten anything from the server yet'

"""———————————————————————————————————————"""

"""Firstly, we must import a module for out GUI, Custom TKInter
This video is motivation for why, mainly, it looks nice and is based off another module that is widely used: https://www.youtube.com/watch?v=iM3kjbbKHQU
it can be downloaded here: https://github.com/TomSchimansky/CustomTkinter
or with this command: pip3 install customtkinter"""
import customtkinter

"""The video or github (which has a couple of awesome examples showing how to make various widgets) shows how we initially set this up."""
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.geometry("600x350")
app.title("GUI Level nasas7.py")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand="True")
"""Here we give the window a label that displays at the top"""
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto Mono", 24))
label.pack(pady=12, padx=10)

"""The next two items are the text fields where we can input a username and password
THIS SHOULD BE OBVIOUS, since we're doing security 'hacks' with these levels, but we're not hiding this info at all
DON'T DO IT THIS WAY for an IRL application, we'll get into better methods of doing this later later, I think
but for right now, this is just all going to stay in plaintext"""
usernm = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
usernm.pack(pady=12, padx=10)

passwd = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
passwd.pack(pady=12, padx=10)

"""oh hey, what's this?? We're making out first function y'all!

This is what our login button is going to do when we click it"""
def login():
        global usernm
        """Let's gather those username and password inputs and put them into a variable"""
        usernmvalue = usernm.get()
        global passwd
        passwdvalue = passwd.get()
        """this hides out widgets that we no longer need, seems to be laggy, I'm not sure if that can be helped?"""
        button.pack_forget()
        usernm.pack_forget()
        passwd.pack_forget()

        """URL goes here because it needs the above"""
        url = 'http://%s.natas.labs.overthewire.org' % usernmvalue

        """make sure this gets the stuff"""
        print(usernmvalue, passwdvalue)

        response = requests.get(url + "/index.php?page=/etc/natas_webpass/natas8", auth = (usernmvalue, passwdvalue))
        
        global content
        content = response.text
        """We have hidden the other widgets, so let's make a new one, and then output our webpage reponse to it!
        I'm not sure what the 0.0 does, I tried setting it to 50 and nothing changed as far as I can tell, it was just in the example I used...
        I'll look into that, but later"""
        textbox.pack(padx=20, pady=20, expand="true")
        justthecontentwewant = re.findall('<br>\n(.*)\n\n', content)
        """so it turns out, the regexing returns a list not a string and we can't append a list into the text box, so we gotta fix that"""
        formattedcontentwewant = "" #initialize a string
        for i in justthecontentwewant:
                formattedcontentwewant = formattedcontentwewant + i
        textbox.insert("0.0", "Hey, here's the information you requested: " + formattedcontentwewant)

"""our login button"""
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

textbox = customtkinter.CTkTextbox(master=frame)

"""We'll do something with this later, but for now, we won't worry about it"""
#checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
#checkbox.pack(pady=12, padx=10)

app.mainloop()

print(content)









"""SDG"""