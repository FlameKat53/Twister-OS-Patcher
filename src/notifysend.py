#!/usr/bin/python3
import os
import resources as rs

if rs.twistver != rs.webversion:
        os.system('WEBVERSION=$(curl https://twisteros.com/Patches/latest.txt) && /home/pi/patcher/notify-send.sh --urgency=normal --expire-time=20000 --app-name=TwistPatch --icon=/home/pi/patcher/src/icons/update.png --action=Update:/home/pi/patcher/patch.sh "A new Twister OS update is now avaliable, click [Update] to update to" "$WEBVERSION"')
