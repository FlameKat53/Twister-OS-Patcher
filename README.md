# TwisterOS-Updater
[![twister-update-dark.png](https://i.postimg.cc/nrkk8y7b/twister-update-dark.png)](https://postimg.cc/p5m8z1qq)<br>
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
[![twister-update-blue.png](https://i.postimg.cc/tJy5MqsN/twister-update-blue.png)](https://postimg.cc/WFWgDP6d)<br>
If the default icon for the application is a little too "dark" for you, then right click on the application and select 'Edit application'. Then click on the icon and choose `twister-update-blue.png` or `twister-update.png` as seen in the images below. The icon will become the one shown below.
[![18-08-2020-12-08-17-REC.png](https://i.postimg.cc/mkVFbMwh/18-08-2020-12-08-17-REC.png)](https://postimg.cc/8fJC47xV)<br>
[![18-08-2020-12-08-49-REC.png](https://i.postimg.cc/MZYBb2Sx/18-08-2020-12-08-49-REC.png)](https://postimg.cc/pypyRSr1)

# Support
If you have any problems, make a issue in this repository or go to the Pi Labs discord to connect with us at https://discord.gg/ttxhYrX

# Credits
FlameKat53: install.sh and updater.desktop files. 
@MobileGamesMotionYT#7199 on Discord: install.sh and light icon
Grayduck: dark icon

# To-do
- [ ] Automatically update in order from current release to latest release
- [ ] Get program installed by default onto TwisterOS
