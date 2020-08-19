echo 'Installing Twister OS Patcher by FlameKat53 and MobileGamesMotionYT...'

#Get archive from github and unzip it
wget https://github.com/FlameKat53/Twister-OS-Patcher/archive/master.zip
unzip master.zip
cd Twister-OS-Patcher-master/

#Move pictures into icons folder
mkdir -p /home/pi/patcher/icons/
mv twister-update.png /home/pi/patcher/icons/twister-update.png
mv twister-update-blue.png /home/pi/patcher/icons/twister-update-blue.png
mv twister-update-dark.png /home/pi/patcher/icons/twister-update-dark.png

#Move scripts into patcher folder
mv patch.sh /home/pi/patcher/patch.sh
mv uninstall.sh /home/pi/patcher/uninstall.sh
mv upgradepatcher.sh /home/pi/patcher/upgradepatcher.sh

#Move patcher.desktop
sudo chmod +x patcher.desktop
mv patcher.desktop /home/pi/.local/share/applications/patcher.desktop
cp /home/pi/.local/share/applications/patcher.desktop /home/pi/Desktop

#Checks if crontab.bak exists before making it
if [ ! -f "/home/pi/patcher/crontab.bak" ]; then
    crontab -l > /home/pi/patcher/crontab.bak
fi

# add new crontab for checking each sunday at midnight
(crontab -l && echo "0 0 * * 0 /home/pi/patcher/checkforupdates.sh") | crontab -

#Add custom alias
echo '#####Twister OS Patcher' >> /home/pi/.bashrc
echo 'alias twistpatch="/home/pi/patcher/patch.sh"' >> /home/pi/.bashrc
echo 'alias twistpatch upgrade="bash /home/pi/patcher/upgradepatcher.sh"' >> /home/pi/.bashrc
echo 'alias twistpatch uninstall="bash /home/pi/patcher/uninstall.sh"' >> /home/pi/.bashrc

#Remove useless folders and make all files executable
cd ../
rm -r Twister-OS-Patcher-master/
rm master.zip
cd /home/pi/patcher/
chmod +x *
