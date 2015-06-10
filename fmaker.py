#!/usr/bin/env python

#Python importing the subprocess library
import subprocess

#Some other bullshit library i needed
import getpass

#Foldermaker Program

# It essentially does that; folders!
# Useful when it comes to create a whole lot of directories
# that need to be nicely organized.

# For this first attempt i'm gonna try and make it create web programming
# related folders such as 'js', 'css', 'dir' or 'html' and so on.

# First of all, ask the user for input on where will the main folder this program
# will create, it'll be something like this:
# 'Hey listen up bruh, where you gonna put yo folder at bruh!?'
# User: 'well gee i dunno, maybe in /home?'
# 'Gotcha covered bruh!'. And then do a fuckload of stuff and print the result.

def mover_func():
	us_name = getpass.getuser()
	# Should you want to place your main folder somewhere in particular, replace home with another directory name
	locale = "/home/" + us_name
	# Although i'll be removing this imposed placement and let user choose where their main folder will be in the future
	subprocess.call(["mkdir",locale + "/" + dirname])
	print "\nMain folder created"
	subprocess.call(["mkdir", locale + "/" + dirname + "/css", locale + "/" + dirname + "/js", locale + "/" + dirname + "/img",locale + "/" + dirname + "/html"])
	print "\nSubfolders created!"


print "Hello and welcome to the Foldermaker v1.0 \n"


while 1:
	print "Where will you want your directories created? \n\n"

	dirname = raw_input()

	print "You asked for %s, right?\n" % dirname
	conf = raw_input("y/n: ")

	if conf == "y":
		mover_func()
		break
	elif conf == "n":
		print "Try again?\n"
	else:
		print "Invalid option\n"
		break

# Remember to make it an executable and i would suggest that you add it to a folder that's in your PATH variable so you can run it right away
