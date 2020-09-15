#!/bin/bash
echo 'Uninstalling Twister OS Patcher by FlameKat53, Jack47 and MobileGamesMotionYT...'
echo 'Thanks for using me! You can install me again at "https://bit.ly/patchtwist"'
cd ~

#Checks to see if these files exist and replace or remove them
if [ -d ~/patcher/ ]; then
  sudo rm -r ~/patcher/
  # we need sudo for the pycache files
fi
if [ -f ~/.local/share/applications/patcher.desktop ]; then
  sudo rm ~/.local/share/applications/patcher.desktop
fi
if [ -f ~/Desktop/patcher.desktop ]; then
  sudo rm ~/Desktop/patcher.desktop
fi
sudo rm -f /usr/local/bin/twistpatch
sudo rm -f /usr/local/bin/twistpatch-update
sudo rm -f /usr/local/bin/twistpatch-remove
crontab -l | grep -v checkforupdates | crontab -
echo 'Uninstalled.'
