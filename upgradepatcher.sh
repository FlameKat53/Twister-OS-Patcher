#Copy .desktop file
cp ~/Desktop/patcher.desktop ~/Pictures/patcher.desktop

#Uninstalls and reinstalls the patcher
bash /home/pi/patcher/uninstall.sh
wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh

#Remove new desktop files
rm ~/Desktop/patcher.desktop
rm /home/pi/.local/share/applications/patcher.desktop

#Replace with old one
cp ~/Pictures/patcher.desktop /home/pi/.local/share/applications/patcher.desktop
mv ~/Pictures/patcher.desktop ~/Desktop/patcher.desktop