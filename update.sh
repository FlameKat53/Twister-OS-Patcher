#!/bin/bash
echo Updating TwisterOS to the latest version
read -p "The updater will now update TwisterOS. When ready, press [Enter] to try to update, or, press [CTRL+C] to close the updater..."
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
	checkVersion
	echo 'Already up to date.'
else
	echo "You seem to be offline!"
fi
