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

#Move scripts into patcher folder
mv patch.sh ~/patcher/patch.sh
mv uninstall.sh ~/patcher/uninstall.sh
mv upgradepatcher.sh ~/patcher/upgradepatcher.sh

#Move patcher.desktop
sudo chmod +x patcherdesktop.desktop
mv patcherdesktop.desktop ~/.local/share/applications/patcherdesktop.desktop
cp ~/.local/share/applications/patcherdesktop.desktop ~/Desktop

#Checks if crontab.bak exists before making it
if [ ! -f "~/patcher/crontab.bak" ]; then
    crontab -l > ~/patcher/crontab.bak
fi

# add new crontab for checking each sunday at midnight
(crontab -l && echo "0 0 * * 0 ~/patcher/checkforupdates.sh") | crontab -

#Add custom alias
echo '#####Twister OS Patcher' >> ~/.bashrc
echo 'alias twistpatch="~/patcher/patch.sh"' >> ~/.bashrc
echo 'alias twistpatch upgrade="bash ~/patcher/upgradepatcher.sh"' >> ~/.bashrc
echo 'alias twistpatch uninstall="bash ~/patcher/uninstall.sh"' >> ~/.bashrc

#Remove useless folders and make all files executable
cd ../
rm -r Twister-OS-Patcher-master/
rm master.zip
cd ~/patcher/
chmod +x *
chmod +x patch.sh