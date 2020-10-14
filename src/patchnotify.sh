#!/bin/bash

sleep 20
latestversion="$(wget -qO- https://twisteros.com/downloads.html | grep 'Version' | head -n1 | awk '{print $4}' | cut -f1 -d"<")"
localversion="$(twistver | awk '{print $4}' | cut -f1 -d"<")"

#Check if you are up to date
if [ "$localver" == "$latestver" ];then
#up to date
  exit 0
fi

/home/pi/patcher/src/notify-send.sh --urgency=normal --expire-time=20000 --app-name=TwistPatch --icon=/home/pi/patcher/src/icons/logo.png --action=Update:~/patcher/patch.sh 'Twister OS update' $latestversion 'is now avaliable, click [Update] to update now!'
sleep 1d
/home/pi/patcher/src/patchpopup.sh