#!/bin/bash
#Uninstalls and reinstalls the patcher
bash ~/patcher/uninstall.sh
cd ~
wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh
chmod +x ./install.sh
./install.sh
cd ~
rm install.sh