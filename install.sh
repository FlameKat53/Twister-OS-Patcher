echo 'Installing TwisterOS Patcher by FlameKat53 and MobileGamesMotionYT...'
wget https://github.com/FlameKat53/TwisterOS-Updater/archive/master.zip
unzip master.zip
cd TwisterOS-Updater-master/
mkdir ~/updater/
mkdir ~/updater/icons/
mv twister-update.png ~/updater/icons/twister-update.png
mv twister-update-blue.png ~/updater/icons/twister-update-blue.png
mv twister-update-dark.png ~/updater/icons/twister-update-dark.png
mv update.sh ~/updater/update.sh
mv updater.desktop ~/.local/share/applications/updater.desktop
cd ../
rm -r TwisterOS-Updater-master/
rm master.zip
cd ~/updater/
chmod +x *
