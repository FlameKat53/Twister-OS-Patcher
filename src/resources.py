import os
import subprocess as sp
import fileinput
import configparser
from os import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

config = configparser.ConfigParser()
if os.path.exists('/home/pi/patcher/src/pat.config'):
	config.read('/home/pi/patcher/src/pat.config')
	print("Exist and read")
else:
	print("Creating config...")
	config['DEFAULT'] = {'color_mode': '0',
	'version': '0.1.1'}
	with open('/home/pi/patcher/src/pat.config', 'w') as configfile:
		config.write(configfile)

### update stuff
app_version = "Version 0.1.1\n"
def get_app_version():
	return app_version

### Open url link
def cpi_open_url(link):
	os.system('sudo -upi chromium-browser '+link)

img_path = os.path.dirname('logo.png')
webversion = sp.getoutput('wget -q https://twisteros.com/Patches/latest.txt && cat latest.txt && rm latest.txt')
twistver = sp.getoutput('twistver')
