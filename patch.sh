#!/bin/bash
echo "Checking for and installing available Twister OS patches..."
read -p "This application will now attempt to update Twister OS. When ready, press [Enter] to update, or press [CTRL+C] to close the patcher..."

#Download the latest patchversion.sh and run it to determine your current version
cd ~/patcher/
wget https://twisteros.com/Patches/checkversion.sh
. checkversion.sh
FILE1=~/patcher/checkversion.sh
if [ -f "$FILE1" ]; then
    rm -f checkversion.sh
fi
FILE2=~/patcher/latest.txt
if [ -f "$FILE2" ]; then
    rm -f latest.txt
fi
wget https://twisteros.com/Patches/latest.txt
if [ -f "$FILE2" ]; then
VERSIONLATEST=$(cat latest.txt)
	rm -f *patchinstall.sh
	checkVersion
	read -p "You are running the most current version. Press [Enter] to quit"
else
	read -p "You seem to be offline! Press [Enter] to quit"
fi
