#!/bin/bash
echo 'Installing Twister OS Patcher by FlameKat53, Jack47, and MobileGamesMotionYT...'

problem=$(dpkg -s python3-tk|grep installed)
path=$(pwd)
echo $path
echo Checking for tkinter: $problem
if [ "" == "$problem" ]; then
	sudo apt-get install python3-tk
fi
sudo apt-get install python3-pil python3-pil.imagetk python3-wget python3-schedule
#Get archive from github and unzip it
wget https://github.com/FlameKat53/Twister-OS-Patcher/archive/py.zip
unzip py.zip
rm py.zip
#wget https://github.com/FlameKat53/Twister-OS-Patcher/archive/master.zip
#unzip master.zip
#rm master.zip
mv Twister-OS-Patcher-master/ ~/patcher/
sudo python3 c_desktop.py $USER
sudo chmod +x /home/pi/patcher/src/start.sh
