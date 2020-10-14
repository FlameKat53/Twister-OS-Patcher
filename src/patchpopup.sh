#!/bin/bash

while true;do
  latestversion="$(wget -qO- https://twisteros.com/downloads.html | grep 'Version' | head -n1 | awk '{print $4}' | cut -f1 -d"<")"
  localversion="$(twistver | awk '{print $4}' | cut -f1 -d"<")"
  
  update=1
  
  if [ -z "$latestversion" ];then
    echo "Failed to get latest version number of Twister OS! Are you connected to the internet?"
    update=0
  fi
  
  if [ -z "$localversion" ];then
    echo "Failed to get current version of Twister! Does the command 'twistver' work?"
    update=0
  fi
  
  #Check if you are up to date
  if [ "$localver" == "$latestver" ];then
  #up to date
    update=0
  fi
  
  if [ $update == 1 ];then
    #Open YAD window
    echo "A new Twister OS patch is available!
    You are currently running v${localversion}, but v${latestversion} is available." | yad \
      --wrap --fontname="12" --text-info \
      --center --title='Twister OS Patcher' --width=310 --height=150 \
      --window-icon="/home/pi/patcher/src/icon.png" \
      --button='Not yet'!"/home/pi/patcher/src/icons/pause.png"!:1 \
      --button='Update now'!"/home/pi/patcher/src/icons/download.png":0 2>/dev/null || update=0
  fi
  
  if [ $update == 1 ];then
    bash /home/pi/patcher/patch.sh
  fi
  
  sleep 43200
done