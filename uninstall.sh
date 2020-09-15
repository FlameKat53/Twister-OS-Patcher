#!/bin/bash
echo 'Uninstalling Twister OS Patcher by FlameKat53, Jack47 and MobileGamesMotionYT...'
echo 'Thanks for using me! You can install me again at "https://bit.ly/patchtwist"'
cd ~

#Checks to see if these files exist and replace or remove them
if [ -d ~/patcher/ ]; then
  rm -r ~/patcher/
fi
if [ -f ~/.local/share/applications/patcher.desktop ]; then
  rm ~/.local/share/applications/patcher.desktop
fi
if [ -f ~/Desktop/patcher.desktop ]; then
  rm ~/Desktop/patcher.desktop
fi
sudo rm -f /usr/local/bin/twistpatch
sudo rm -f /usr/local/bin/twistpatch-uninstall
crontab -l | sed -n '/0 \* \* \* \* \~\/patcher\/checkforupdates.sh/!p' | crontab -
echo 'Uninstalled.'
