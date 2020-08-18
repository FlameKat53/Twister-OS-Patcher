#!/bin/bash
echo "Checking for and installing available Twister OS patches..."
read -p "This application will now attempt to update Twister OS. When ready, press [Enter] to update, or press [CTRL+C] to close the updater..."
cd ~/updater/
wget https://twisteros.com/Patches/checkversion.sh
. checkversion.sh
FILE=~/updater/latest.txt
if [ -f "$FILE" ]; then
    rm latest.txt
fi
wget https://twisteros.com/Patches/latest.txt
if [ -f "$FILE" ]; then
VERSIONLATEST=$(cat latest.txt)
	rm -f *patchinstall.sh
	checkVersion
	echo "You are running the most current version."
else
	echo "You seem to be offline!"
fi
