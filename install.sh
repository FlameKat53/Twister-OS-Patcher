echo 'Installing Twister OS Patcher by FlameKat53 and MobileGamesMotionYT...'

#Get archive from github and unzip it
wget https://github.com/FlameKat53/Twister-OS-Patcher/archive/master.zip
unzip master.zip
cd Twister-OS-Patcher-master/

#Move pictures into icons folder
mkdir -p ~/patcher/icons/
mv twister-update.png ~/patcher/icons/twister-update.png
mv twister-update-blue.png ~/patcher/icons/twister-update-blue.png
mv twister-update-dark.png ~/patcher/icons/twister-update-dark.png
mv arrow-white.png ~/patcher/icons/arrow-white.png

#Move scripts into patcher folder
mv patch.sh ~/patcher/patch.sh
mv uninstall.sh ~/patcher/uninstall.sh
mv upgradepatcher.sh ~/patcher/upgradepatcher.sh
mv checkforupdates.sh ~/patcher/checkforupdates.sh
mv notify-send.sh ~/patcher/notify-send.sh
mv notify-action.sh ~/patcher/notify-action.sh

#Move patcher.desktop
sudo chmod +x patcher.desktop
mv patcher.desktop ~/.local/share/applications/patcher.desktop
cp ~/.local/share/applications/patcher.desktop ~/Desktop/patcher.desktop

# Add new crontab for checking each Monday at 11:00AM
(crontab -l && echo "0 * * * * ~/patcher/checkforupdates.sh") | crontab -

#Adds commands
if [ ! -f "/usr/local/bin/twistpatch" ]; then
    sudo ln -s ~/patcher/patch.sh /usr/local/bin/twistpatch
    sudo chmod 755 /usr/local/bin/twistpatch
	
fi
if [ ! -f "/usr/local/bin/twistpatch-uninstall" ]; then
    sudo ln -s ~/patcher/uninstall.sh /usr/local/bin/twistpatch-uninstall
    sudo chmod 755 /usr/local/bin/twistpatch-uninstall
	 
fi
if [ ! -f "/usr/local/bin/twistpatch-update" ]; then
    sudo ln -s ~/patcher/upgradepatcher.sh /usr/local/bin/twistpatch-update
    sudo chmod 755 /usr/local/bin/twistpatch-update
	
fi

#Remove useless folders and make all files executable
cd ../
rm -r Twister-OS-Patcher-master/
rm master.zip
cd ~/patcher/
chmod +x *
