#!/bin/bash
cd /home/pi/patcher/
VERSIONCURRENT=$(twistver)
WEBVERSION=$(curl https://twisteros.com/Patches/latest.txt)
if [ "$VERSIONCURRENT" != "$WEBVERSION" ]; then
    ./notify-send.sh --urgency=normal --expire-time=20000 --app-name=TwistPatch --icon=/home/pi/patcher/icons/arrow-white.png --action=Update:/home/pi/patcher/patch.sh 'A new Twister OS update is now avaliable, click [Update] to update to' "$WEBVERSION"
fi