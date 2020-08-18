echo 'Uninstalling Twister OS Updater by FlameKat53 and MobileGamesMotionYT...'
cd ~/
if [ -d "~/updater/" ]; then
rm -r ~/updater/
fi
if [ -f "~/.local/share/applications/updater.desktop" ]; then
rm ~/.local/share/applications/updater.desktop
fi
