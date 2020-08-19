echo 'Installing Twister OS Patcher by FlameKat53 and MobileGamesMotionYT...'
wget https://github.com/FlameKat53/Twister-OS-Patcher/archive/master.zip
unzip master.zip
cd Twister-OS-Patcher-master/
mkdir -p ~/patcher/icons/
mv twister-update.png ~/patcher/icons/twister-update.png
mv twister-update-blue.png ~/patcher/icons/twister-update-blue.png
mv twister-update-dark.png ~/patcher/icons/twister-update-dark.png
mv patch.sh ~/patcher/patch.sh
mv uninstall.sh ~/patcher/uninstall.sh
mv patcher.desktop ~/.local/share/applications/patcher.desktop
cp ~/.local/share/applications/patcher.desktop ~/Desktop
cd ../
rm -r Twister-OS-Patcher-master/
rm master.zip
cd ~/patcher/
chmod +x *
chmod +x patch.sh