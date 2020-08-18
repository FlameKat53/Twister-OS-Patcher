# TwisterOS-Updater
[![twister-update.png](https://i.postimg.cc/5tsT4pyc/twister-update.png)](https://postimg.cc/HJ7B3wb3)<br>
An updater for TwisterOS that automatically downloads, unzips, and runs the latest patch for TwisterOS.
If you're on a version that is not the previous latest (e.g. you're on 1.5 and the latest is 1.7) you WILL break your install, so it's recommended to run the tool at least once a week with cron, or every time you boot the Pi with rc.local because if an update is missed, files will be broken. Also do NOT run this on Raspberry Pi OS because it will BREAK too. It is fine if you run the latest patch multiple times.

#### Go support TwisterOS!</br>
### <a href="https://twisteros.com/">>TwisterOS<</a>

# Install
`cd ~/Downloads && wget https://raw.githubusercontent.com/FlameKat53/TwisterOS-Updater/master/install.sh && chmod +x ./install.sh &&./install.sh`

# Usage
[![18-08-2020-08-02-21-REC.png](https://i.postimg.cc/cHq94jWb/18-08-2020-08-02-21-REC.png)](https://postimg.cc/DWgdxx8r)<br>
Go in the applications menu and search for TwisterOS updater in the system section. Click on it and a terminal window will open.

# Automatically Patch
Run the following command to run the script once every 3 days<br>
`sudo su`<br>
`echo '0 0 */3 * * ~/updater/update.sh' >> /var/spool/cron/crontabs/pi && exit`<br>
Do this to run the patcher on startup<br>
Run `sudo nano /etc/rc.local` and add the following code BEFORE the line `exit 0` as seen in the image below<br>
`/home/pi/updater/update.sh &` 

# Icon
If the default icon for the application is a little too "dark" for you, then replace the contents of 'updater.desktop'
with this:<br>
`[Desktop Entry]`<br>
`Name=TwisterOS Updater`<br>
`Comment=Automatically patches TwisterOS to the latest version`<br>
`Exec=/home/pi/updater/update.sh`<br>
`Icon=/home/pi/updater/updater.jpg`<br>
`Version=1.0`<br>
`Type=Application`<br>
`Categories=Settings`<br>
`Terminal=true`<br>
`StartupNotify=false`<br>
`Path=`<br>

# Support
If you have any problems, make a issue in this repository or go to the Pi Labs discord to connect with us at https://discord.gg/ttxhYrX

# Credits
FlameKat53: install.sh and updater.desktop files. 
@MobileGamesMotionYT#7199 on Discord: install.sh and light icon
Grayduck: dark icon

# To-do
- [ ] Automatically update in order from current release to latest release
- [ ] Get program installed by default onto TwisterOS
