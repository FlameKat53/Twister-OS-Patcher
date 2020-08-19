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
if [ -f ~/patcher/.bashrc.bak ]; then
  mv ~/patcher/.bashrc.bak ~/.bashrc
fi
crontab -l | sed "s/^@weekly/#&/" | crontab -
echo 'Uninstalled.'
