#!/usr/bin/python3
import sys
import urllib.request
import socket
import os
import resources as rs
from tkinter import messagebox as msb
from tkinter import *
import wget
import subprocess as sp

path = os.path.dirname(os.path.realpath(__file__))
Files = ["https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/src/gui.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/src/resources.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/src/main.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/src/update.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/src/theme.py"]
#Files = ["https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/gui.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/resources.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/main.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/update.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/theme.py"]
Names = ["gui.py", "resources.py", "main.py", "update.py", "theme.py"]
def delete_old():
	for name in Names:
		os.system('rm '+path+'/'+name)
		print("Deleted "+name)

def download_git(url, name):
	filename, headers = urllib.request.urlretrieve(url, filename="/home/pi/CommanderPi/src/"+name)
	print ("download start!")
	print ("download complete!")
	print ("download file location: ", filename)
	#print ("download headers: ", headers)

def update_pat():
	url = "https://raw.githubusercontent.com/Jack477/CommanderPi/master/src/resources.py"
	with urllib.request.urlopen(url) as f:
		xcontent = f.read().decode('utf-8')
		xcontent = xcontent.splitlines()
		xversion = ""
		for line in xcontent:
			if "app_version =" in line:
				xversion=line
		if rs.app_version[:-1] in xversion:
			msb.showinfo(title=None, message="There is no update available!")
		else:
			delete_old()
			for f, x in zip(Files, Names):
				download_git(f, x)
			sys.exit(0)

def delete_oldfiles():
	os.system('rm -f /home/pi/patcher/src/*patchinstall.sh')

def download_patch():
	msb.showinfo(title="TwistPatch", message="Download will start in the background\n Press OK to continue.")
	import checkversion as cv
	cv.update()

def update_twist():
	if rs.twistver == rs.webversion:
			msb.showinfo(title="TwistPatch", message="There is no update available!")
	else:
		answer = msb.askyesno(title="TwistPatch", message="This will update Twister OS, do you wish to proceed?")
		if answer == True:
			delete_oldfiles()
			download_patch()

def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

def update_patcher(upgradeavaliable):
	if upgradeavaliable == True:
		answer = msb.askyesno(title="TwistPatch", message='A patcher update is avaliable.\nWould you like to update the patcher?')
		if answer == True:
			os.system('twistpatch-update')

			return True
		else:
			return False

def check_online():
	url = "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/src/resources.py"
	if is_connected("1.1.1.1"):
		with urllib.request.urlopen(url) as f:
			xcontent = f.read().decode('utf-8')
			xcontent = xcontent.splitlines()
			xversion = ""
			for line in xcontent:
				if "app_version =" in line:
					xversion=line
			if rs.app_version[:-1] in xversion:
				print("It works bc it's same version!")
			else:
				answer = msb.askyesno(title="TwistPatch", message='A patcher update is avaliable.\nWould you like to update the patcher?')
				if answer == True:
					update_pat()
				print(rs.app_version)
				print(xversion)
		return True
	else:
		print("Network is disconnected")
		return False

