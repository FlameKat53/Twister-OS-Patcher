#!/bin/bash
echo 'Installing Twister OS Patcher by FlameKat53, Jack47, and MobileGamesMotionYT...'

problem=$(dpkg -s python3-tk|grep installed)
path=$(pwd)
echo $path
echo Checking for tkinter: $problem
if [ "" == "$problem" ]; then
	sudo apt-get install python3-tk
fi
sudo apt install -y python3-pil python3-pil.imagetk python3-wget
sudo pip3 install wget
#Get archive from github and unzip it
wget https://github.com/FlameKat53/Twister-OS-Patcher/archive/master.zip
unzip master.zip
rm master.zip
sudo rm -r -f /home/pi/patcher
mv Twister-OS-Patcher-master/ /home/pi/patcher/
cd /home/pi/patcher/
python3 c_desktop.py $USER
sudo chmod +x *.sh
cd /home/pi/patcher/src/
sudo chmod +x *.sh
#crontab -l | { cat; echo "* 12 * * * python3 '/home/pi/patcher/src/notifysend.py'"; } | crontab -

cd /home/pi/patcher
sudo rm README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
sudo rm -r .github

#Adds commands
sudo rm -f /usr/local/bin/twistpatch

if [ ! -f "/usr/local/bin/twistpatch" ]; then
    sudo ln -s '/home/pi/patcher/src/noup.sh' /usr/local/bin/twistpatch
    sudo chmod +x /usr/local/bin/twistpatch
fi

sudo rm -f /usr/local/bin/twistpatch-uninstall
sudo rm -f /usr/local/bin/twistpatch-remove

if [ ! -f "/usr/local/bin/twistpatch-remove" ]; then
    sudo ln -s '/home/pi/patcher/uninstall.sh' /usr/local/bin/twistpatch-remove
    sudo chmod +x /usr/local/bin/twistpatch-remove
fi

sudo rm -f /usr/local/bin/twistpatch-update

if [ ! -f "/usr/local/bin/twistpatch-update" ]; then
    sudo ln -s /home/pi/patcher/upgradepatcher.sh /usr/local/bin/twistpatch-update
    sudo chmod +x /usr/local/bin/twistpatch-update
fi
