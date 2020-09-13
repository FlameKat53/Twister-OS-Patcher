#!/usr/bin/python3
import sys
import urllib.request
import socket
import os
import resources as rs
from tkinter import messagebox as msb

path = os.path.dirname(os.path.realpath(__file__))
Files = ["https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/gui.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/resources.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/main.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/update.py", "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/theme.py"]
Names = ["gui.py", "resources.py", "main.py", "update.py", "theme.py"]
def delete_old():
	for name in Names:
		os.system('rm '+path+'/'+name)
		print("Deleted "+name)

def download_git(url, name):
	filename, headers = urllib.request.urlretrieve(url, filename="/home/pi/patcher/src/"+name)
	print ("download start!")
	print ("download complete!")
	print ("download file location: ", filename)
	
def delete_oldSh():
	os.system('rm /patcher/src/')

def download_patch(url, name):
	filename, headers = urllib.request.urlretrieve(url, filename="/home/pi/patcher/src/"+name)
	print ("download start!")
	msb.showinfo(title=None, message="Downloading!")
	print ("download complete!")
	msb.showinfo(title=None, message="Download Complete!")
	print ("download file location: ", filename)

def update_twist():
	url = "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/resources.py"
	with urllib.request.urlopen(url) as f:
		bcontent = f.read().decode('utf-8')
		bcontent = bcontent.splitlines()
		bversion = ""
		for line in bcontent:
			if "app_version =" in line:
				bversion=line
		if rs.twistver[:-1] in bversion:
			msb.showinfo(title=None, message="There is no update available!")
		else:
			delete_oldSh()
			for f, x in zip(Files, Names):
				download_patch(f, x)
			sys.exit(0)

def update_cpi():
	url = "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/resources.py"
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
def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False
def check_update():
	url = "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/src/resources.py"
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
				msb.showinfo(title=None, message="Update is available!")
			print(rs.app_version)
			print(xversion)
	else:
		print("Network is disconnected")