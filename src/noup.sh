#!/bin/bash
cd /home/pi/patcher/src/
rm -f /home/pi/patcher/src/checkversion.py
wget https://twisteros.com/Patches/checkversion.py
sudo python3 /home/pi/patcher/src/main.py ${HOME} 0 > log.txt
