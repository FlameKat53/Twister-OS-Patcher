echo 'Installing TwisterOS Patcher by FlameKat53 and MobileGamesMotionYT...'
wget https://github.com/FlameKat53/TwisterOS-Updater/archive/master.zip
unzip master.zip
cd TwisterOS-Updater-master/
mkdir ~/updater/
mv twister-update.png ~/updater/twister-update.png
mv updater.jpg ~/updater/updater.jpg
mv update.sh ~/updater/update.sh
mv updater.desktop ~/.local/share/applications/updater.desktop
cd ../
rm -r TwisterOS-Updater-master/
rm master.zip
cd ~/updater/
chmod +x *
