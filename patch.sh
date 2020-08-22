#!/bin/bash
echo "Checking for and installing available Twister OS patches... Press Ctrl-C to cancel"
echo "Please wait while we get the latest patch files."
sleep 5s

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
	clear
	echo "You are running the most current version of" $VERSIONLATEST " Exiting..."
	sleep 3s
else
	clear
	echo "You seem to be offline! Exiting..."
	sleep 1.5s
fi
