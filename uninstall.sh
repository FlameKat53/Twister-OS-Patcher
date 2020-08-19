echo 'Uninstalling Twister OS Patcher by FlameKat53 and MobileGamesMotionYT...'
echo 'Thanks for using me! You can install me again at "https://bit.ly/twistpatch"'
cd ~/
if [ -d ~/updater/ ]; then
rm -r ~/updater/
fi
if [ -f ~/.local/share/applications/updater.desktop ]; then
rm ~/.local/share/applications/updater.desktop
fi
