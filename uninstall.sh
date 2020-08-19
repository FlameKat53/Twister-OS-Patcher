echo 'Uninstalling Twister OS Patcher by FlameKat53 and MobileGamesMotionYT...'
echo 'Thanks for using me! You can install me again at "https://bit.ly/patchtwist"'
cd /home/pi/

#Checks to see if these files exist and replace or remove them
if [ -d /home/pi/patcher/ ]; then
  rm -r /home/pi/patcher/
fi
if [ -f /home/pi/.local/share/applications/patcher.desktop ]; then
  rm /home/pi/.local/share/applications/patcher.desktop
fi
if [ -f /home/pi/Desktop/patcher.desktop ]; then
  rm /home/pi/Desktop/patcher.desktop
fi
sudo rm -f /usr/local/bin/twistpatch
sudo rm -f /usr/local/bin/twistpatch-uninstall
sudo rm -f /usr/local/bin/twistpatch-update
crontab -l | sed -n '/0 11 * * 1 \~\/patcher\/checkforupdates.sh/!p' | crontab -
echo 'Uninstalled.'
