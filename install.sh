#!/bin/sh
echo 'Installing TwisterOS Patcher by FlameKat53 and MobileGamesMotionYT...'
git clone --depth=1 https://github.com/FlameKat53/TwisterOS-Updater.git
cd TwisterOS-Updater/
mv updater.png ~/updater/updater.png
mv update.sh ~/updater/update.sh
mv updater.desktop ~/.local/share/applications/updater.desktop
cd ../
rm -r TwisterOS-Updater/
