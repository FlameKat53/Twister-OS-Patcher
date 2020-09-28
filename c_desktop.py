#!/usr/bin/python
import sys
import os
import subprocess as sp
from os.path import expanduser
from /home/pi/patcher/src/resources.py import get_app_version

patcherversion = str(get_app_version())

user = sys.argv[1]
home_path = expanduser("~%s" % user)

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)
f_content = "[Desktop Entry]\nName=Twister OS Patcher\nComment=Updates Twister OS\nExec="+dir_path+"/src/start.sh 0\nIcon="+dir_path+"/src/icon.png\nCategories=System;\nVersion="+patcherversion+"\nType=Application\nTerminal=false\nStartupNotify=true"
print(f_content)

x_dir = "/home/pi/.local/share/applications/patcher.desktop"
print("Save menu shortcut to %s" % x_dir)
f2 = open(x_dir, "w+")
f2.write(f_content)
f2.close
