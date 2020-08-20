#Rename .desktop file
mv ~/Desktop/patcher.desktop ~/Desktop/patcher.desktop.bak

#Uninstalls and reinstalls the patcher
bash ~/patcher/uninstall.sh
wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh

#Remove new desktop files
rm ~/Desktop/patcher.desktop
rm ~/.local/share/applications/patcher.desktop

#Replace with old one
cp ~/Desktop/patcher.desktop.bak ~/.local/share/applications/patcher.desktop
mv ~/Desktop/patcher.desktop.bak ~/Desktop/patcher.desktop