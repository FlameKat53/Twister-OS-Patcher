echo 'Uninstalling Twister OS Patcher by FlameKat53 and MobileGamesMotionYT...'
echo 'Thanks for using me! You can install me again at "https://bit.ly/patchtwist"'
cd ~/
if [ -d ~/patcher/ ]; then
  rm -r ~/patcher/
fi
if [ -f ~/.local/share/applications/patcher.desktop ]; then
  rm ~/.local/share/applications/patcher.desktop
  rm ~/Desktop/patcher.desktop
fi
