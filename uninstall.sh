#!/bin/bash
echo 'Uninstalling Twister OS Patcher by FlameKat53, Jack47 and MobileGamesMotionYT...'
echo 'Thanks for using me! You can install me again at "https://bit.ly/patchtwist"'
cd ~

#Checks to see if these files exist and replace or remove them
  sudo rm -r /home/pi/patcher/
  # we need sudo for the pycache files
if [ -f /home/pi/.local/share/applications/patcher.desktop ]; then
  sudo rm /home/pi/.local/share/applications/patcher.desktop
fi
if [ -f /home/pi/Desktop/patcher.desktop ]; then
  sudo rm /home/pi/Desktop/patcher.desktop
fi
sudo rm -f /usr/local/bin/twistpatch
sudo rm -f /usr/local/bin/twistpatch-update
sudo rm -f /usr/local/bin/twistpatch-remove
#crontab -l | grep -v notifysend | crontab -
echo 'Uninstalled.'
