#!/bin/bash
echo Updating TwisterOS to the latest version
cd /home/pi/updater/
FILE=/home/pi/updater/latest.txt
if [ -f "$FILE" ]; then
    rm latest.txt
fi
wget https://twisteros.com/Patches/latest.txt
if [ -f "$FILE" ]; then
VERSIONLATEST=$(cat latest.txt)
VERSIONCURRENT=$(twistver)
if [ "$VERSIONCURRENT" = "$VERSIONLATEST" ];
then
	echo 'Already up to date.'
	read -p "The updater will now close. When ready, press [Enter] to close the updater..."
else
	echo 'Downloading latest version...'
	wget https://twisteros.com/Patches/latestLink.txt
	VERSIONLINK=$(cat latestLink.txt)
	rm latestLink.txt
	echo 'Extracting .zip...'
	unzip *.zip
	chmod +x *patchinstall.sh
	./*patchinstall.sh
	#rm *patchinstall.sh
fi
else
	echo "You seem to be offline!"
fi