VERSIONCURRENT=$(twistver)
WEBVERSION=$(curl https://twisteros.com/Patches/latest.txt)

if [ "$VERSIONCURRENT" != "$WEBVERSION" ]; then
    notify-send --urgency=normal --app-name=Twister-OS-Patcher --icon=svn-update New available. Run Twister OS Patcher 
fi