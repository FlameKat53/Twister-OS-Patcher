# TwisterOS-Updater
An updater for TwisterOS that automatically downloads, unzips, and runs the latest patch for TwisterOS.
If you're on a version that is not the previous latest (e.g. you're on 1.5 and the latest is 1.7) you WILL break your install, so it's recommended to run the tool at least once a week with cron, or every time you boot the Pi with rc.local because if an update is missed, files will be broken. Also do NOT run this on Raspberry Pi OS because it will BREAK too. It is fine if you run the latest patch multiple times.

# Install
`cd ~/Downloads && wget https://raw.githubusercontent.com/FlameKat53/TwisterOS-Updater/master/install.sh && chmod +x ./install.sh &&./install.sh`

# Automatically Patch
Run the following command to run the script once every 3 days<br>
`sudo su`<br>
`echo '0 0 */3 * * ~/updater/update.sh' >> /var/spool/cron/crontabs/pi && exit`<br>
Do this to run the patcher on startup<br>
Run `sudo nano /etc/rc.local` and add the following code BEFORE the line `exit 0`<br>
`/home/pi/updater/update.sh &`

# Credits
FlameKat53: install.sh and updater.desktop files. 
@MobileGamesMotionYT#7199 on Discord: install.sh
grayduck: icon

# To-do
- [ ] Automatically update in order from current release to latest release
