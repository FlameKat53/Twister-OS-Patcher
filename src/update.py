#!/usr/bin/python3
import sys
import urllib.request
import socket
import os
import checkversion as cv
import resources as rs
from tkinter import messagebox as msb
from tkinter import *
import wget
import subprocess as sp

path = os.path.dirname(os.path.realpath(__file__))
def delete_oldfiles():
	os.system('rm -f /home/pi/patcher/src/*patchinstall.sh')

def download_patch():
	cv.update()

def update_twist():
	if rs.twistver == rs.webversion:
		msb.showinfo(title="TwistPatch", message="There is no update available!")
	else:
		answer = msb.askyesno(title="TwistPatch", message="This will update Twister OS it could take a while, do you wish to proceed?")
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

def check_online():
	url = "https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/src/resources.py"
	if is_connected("1.1.1.1"):
		#with urllib.request.urlopen(url) as f:
		#	xcontent = f.read().decode('utf-8')
		#	xcontent = xcontent.splitlines()
		#	xversion = ""
		#	for line in xcontent:
		#		if "app_version =" in line:
		#			xversion=line
		#	if rs.app_version[:-1] in xversion:
		#		print("It works bc it's same version!")
		#	else:
		#		answer = msb.askyesno(title="TwistPatch", message='A patcher update is avaliable.\nWould you like to update the patcher?')
		#		if answer == True:
		#			update_pat()
		#		print(rs.app_version)
		#		print(xversion)
		print("Network is connected")
		return True
	else:
		print("Network is disconnected")
		return False

