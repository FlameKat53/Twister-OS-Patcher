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

def update_twist():
	if rs.twistver == rs.webversion:
		msb.showinfo(title="TwistPatch", message="There is no update available!")
	else:
		answer = msb.askyesno(title="TwistPatch", message="This will update Twister OS it could take a while, do you wish to proceed?")
		if answer == True:
			delete_oldfiles()
			cv.update()

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
		print("Network is connected")
		return True
	else:
		print("Network is disconnected")
		return False

