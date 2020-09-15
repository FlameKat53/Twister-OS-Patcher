#!/bin/bash
rm -f /home/pi/patcher/src/checkversion.py
wget https://twisteros.com/Patches/checkversion.py
sudo python3 ${HOME}/patcher/src/main.py ${HOME} 1> log.txt
