#Copy .desktop file and cron
cp ~/Desktop/patcher.desktop ~/Pictures/patcher.desktop

#Uninstalls and reinstalls the patcher
bash ~/patcher/uninstall.sh
wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh

#Remove new desktop files
rm ~/Desktop/patcher.desktop
rm ~/.local/share/applications/patcher.desktop

#Replace with old one
cp ~/Pictures/patcher.desktop ~/.local/share/applications/patcher.desktop
mv ~/Pictures/patcher.desktop ~/Desktop/patcher.desktop