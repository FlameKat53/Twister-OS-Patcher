echo 'Installing Twister OS Patcher by FlameKat53 and MobileGamesMotionYT...'
wget https://github.com/FlameKat53/Twister-OS-Updater/archive/master.zip
unzip master.zip
cd Twister-OS-Updater-master/
mkdir -p ~/updater/icons/
mv twister-update.png ~/updater/icons/twister-update.png
mv twister-update-blue.png ~/updater/icons/twister-update-blue.png
mv twister-update-dark.png ~/updater/icons/twister-update-dark.png
mv update.sh ~/updater/update.sh
mv uninstall.sh ~/updater/uninstall.sh
mv updater.desktop ~/.local/share/applications/updater.desktop
cp ~/.local/share/applications/updater.desktop ~/Desktop
cd ../
rm -r Twister-OS-Updater-master/
rm master.zip
cd ~/updater/
chmod +x *
