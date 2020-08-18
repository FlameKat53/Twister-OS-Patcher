# TwisterOS-Updater
An updater for TwisterOS that automatically downloads, unzips, and runs the latest patch for TwisterOS.
If you're on a version that is not the previous latest (e.g. you're on 1.5 and the latest is 1.7) you WILL break your install, so it's recommended to run the tool at least once a week with cron, or every time you boot the Pi with rc.local because if an update is missed, files will be broken. Also do NOT run this on Raspberry Pi OS becuase it will BREAK too. It is fine if you run the latest patch multiple times.

# Install
`cd ~/Downloads && wget https://raw.githubusercontent.com/FlameKat53/TwisterOS-Updater/master/install.sh && chmod +x ./install.sh &&./install.sh`

# Automatically Patch
Run the following command to run the script once every 3 days
`sudo su && echo '0 0 */3 * * ~/updater/update.sh' >> /var/spool/cron/crontabs/pi && exit`
Run this to run the patcher on startup
`echo '0 0 */3 * * ~/updater/update.sh' >> /etc/rc.local`

# Credits
FlameKat53: install.sh and updater.desktop files. @MobileGamesMotionYT#7199 on Discord: desktop file icon and install.sh

# To-do
- [ ] Automatically update in order from current release to latest release
