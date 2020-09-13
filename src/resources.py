import os
import subprocess as sp
import fileinput
import configparser
from os import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

home_path = sys.argv[1]

config = configparser.ConfigParser()
if os.path.exists(home_path+'/patcher/src/pat.config'):
	config.read(home_path+'/patcher/src/pat.config')
	print("Exist and read")
else:
	print("Creating config...")
	config['DEFAULT'] = {'color_mode': '0',
	'version': 'Alpha 13'}
	with open(home_path+'/patcher/src/pat.config', 'w') as configfile:
		config.write(configfile)

### update stuff
app_version = "Version Alpha 13\n"
def get_app_version():
	return app_version

### Open url link
def cpi_open_url(link):
	os.system('sudo -upi chromium-browser '+link)

img_path = os.path.dirname('logo.png')
### Reboot RPI	
def reboot():
	os.system("sudo reboot now")

twistver = sp.getoutput('twistver')
webversion = sp.getoutput('curl https://twisteros.com/Patches/checkversion.sh')