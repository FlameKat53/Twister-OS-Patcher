#!/bin/bash
echo "Checking for and installing available Twister OS patches..."
read -p "This application will now attempt to update Twister OS. When ready, press [Enter] to update, or press [CTRL+C] to close the updater..."
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
	echo "You are running the most current version."
else
	echo "You seem to be offline!"
fi
