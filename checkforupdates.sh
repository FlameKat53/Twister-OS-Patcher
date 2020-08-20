#!/bin/bash
cd ~/patcher/
VERSIONCURRENT=$(twistver)
WEBVERSION=$(curl https://twisteros.com/Patches/latest.txt)

if [ "$VERSIONCURRENT" != "$WEBVERSION" ]; then
    ./notify-send.sh --urgency=normal --expire-time=20000 --app-name=twistpatch --icon=~/patcher/icons/arrow-white.png --action=Update:twistpatch 'Twister OS update' $WEBVERSION 'is now avaliable, click [Update] to upgrade now!'
fi