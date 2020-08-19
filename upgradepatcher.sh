#Copy .desktop file and cron
cp /home/pi/Desktop/patcher.desktop /home/pi/Pictures/patcher.desktop

#Uninstalls and reinstalls the patcher
bash /home/pi/patcher/uninstall.sh
wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh

#Remove new desktop files
rm /home/pi/Desktop/patcher.desktop
rm /home/pi/.local/share/applications/patcher.desktop

#Replace with old one
cp /home/pi/Pictures/patcher.desktop /home/pi/.local/share/applications/patcher.desktop
mv /home/pi/Pictures/patcher.desktop /home/pi/Desktop/patcher.desktop