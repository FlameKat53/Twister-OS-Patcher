# TwisterOS-Updater
An updater for TwisterOS that automatically downloads, unzips, and runs the latest patch for TwisterOS.
If you're on a version that is not the previous latest (e.g. you're on 1.5 and the latest is 1.7) you WILL break your install, so it's recommened to run the tool at least once a week with cron, or every time you boot the Pi with rc.local becuase if a update is missed files will be broken. Also do NOT run this on Raspberry Pi OS becuase it will BREAK too.

# Install
`cd ~/Downloads && wget https://github.com/FlameKat53/TwisterOS-Updater/blob/master/install.sh && chmod +x ./install.sh && ./install.sh`

# Credits
FlameKat53: install.sh and updater.desktop files. @MobileGamesMotionYT#7199 on Discord: desktop file icon and install.sh

# To-do
- [ ] Automatically update in order from current release to latest release
