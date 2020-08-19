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

# add new crontab for checking each sunday at midnight
(crontab -l && echo "@weekly ~/patcher/checkforupdates.sh") | crontab -

#Add custom alias
cd /home/pi/
echo '#####Twister OS Patcher' >> .bashrc
echo 'alias twistpatch="/home/pi/patcher/patch.sh"' >> .bashrc
echo 'alias twistpatch-update="bash /home/pi/patcher/upgradepatcher.sh"' >> .bashrc
echo 'alias twistpatch-remove="bash /home/pi/patcher/uninstall.sh"' >> .bashrc
source ~/.bashrc
cd Twister-OS-Patcher-master/

#Remove useless folders and make all files executable
cd ../
rm -r Twister-OS-Patcher-master/
rm master.zip
cd /home/pi/patcher/
chmod +x *
