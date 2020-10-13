#!/bin/bash

cd ~/patcher
latestversion="$(wget -qO- https://twisteros.com/downloads.html | grep 'Version' | head -n1 | awk '{print $4}' | cut -f1 -d"<")"
localversion="$(twistver | awk '{print $4}' | cut -f1 -d"<")"

if [ -z "$latestversion" ];then
  echo "Failed to get latest version number of Twister OS! Are you connected to the internet?"
  exit 1
fi

if [ -z "$localversion" ];then
  echo "Failed to get current version of Twister! Does the command 'twistver' work?"
  exit 1
fi

#Check if you are up to date
if [ "$localver" == "$latestver" ];then
  #up to date
  exit 0
fi

#Open YAD window
echo "A new Twister OS patch is available!
You are currently running v${localversion}, but v${latestversion} is available." | yad \
  --wrap --fontname="12" --text-info \
  --center --title='Twister OS Patcher' --width=310 --height=150 \
  --window-icon="/home/pi/patcher/src/icon.png" \
  --button='Cancel'!"/home/pi/patcher/src/icons/exit.png"!:1 \
  --button='Update now'!"/home/pi/patcher/src/icons/download.png":0 2>/dev/null || exit 0

bash /home/pi/patcher/patch.sh
