#!/bin/bash
echo 'Installing Twister OS Patcher by FlameKat53, Jack47, and RaspberryPiNews...'

problem=$(dpkg -s python3-tk|grep installed)
path=$(pwd)
echo $path
echo Checking for tkinter: $problem
if [ "" == "$problem" ]; then
	sudo apt-get install python3-tk
fi
sudo apt install -y python3-pil python3-pil.imagetk python3-wget yad
sudo rm /usr/share/applications/yad-icon-browser.desktop
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
#crontab -l | { cat; echo "0 11 * * * /bin/bash -c "/home/pi/patcher/src/patchpopup.sh""; } | crontab -

cd ~/patcher
rm README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
rm -r .github

#Adds commands
sudo rm -f /usr/local/bin/twistpatch

if [ ! -f "/usr/local/bin/twistpatch" ]; then
    sudo ln -s '/home/pi/patcher/src/start.sh' /usr/local/bin/twistpatch
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

mkdir -p ~/.config/autostart
echo "[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Twister OS Patcher
Exec=/home/pi/patcher/src/patchnotify.sh
OnlyShowIn=XFCE;
StartupNotify=false
Terminal=false
Hidden=false" > ~/.config/autostart/patcher.desktop
chmod +x ~/.config/autostart/patcher.desktop
echo 'Install completed sucessfully!'
read -p 'Please press [Enter] to reboot and finish installation!'
sudo reboot