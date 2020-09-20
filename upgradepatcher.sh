#!/bin/bash
#Uninstalls and reinstalls the patcher
bash ~/patcher/uninstall.sh
wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/py/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh
#wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh
