# TwistPatcher
![](https://i.postimg.cc/rwTFyXLs/tos-patcher-new2.png)<br>
An updater for Twister OS that automatically downloads, unzips, and runs the latest patch for Twister OS. It is fine if you run the patcher more than once as it auto-detects your version. You have to run the patcher when you can reboot your computer as it is required for patching.<br>


#### Go support Twister OS!</br>
### <a href="https://twisteros.com/">>Twister OS<</a>

# Install/Update
`wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh`<br>
If you notice the repo has been changed, run `twistpatch-update` to update your current version of the patcher.

# Uninstall
`twistpatch-remove`

# Usage
![18-08-2020-08-02-21-REC.png](https://i.postimg.cc/cHq94jWb/18-08-2020-08-02-21-REC.png)<br>
There are 3 ways to open the patcher. Firstly, you can click on the "Twister OS Patcher" in your desktop and applications menu. Secondly, you can type "twistpatch" into terminal. Lastly, you can install [MacOS Notification Center](https://github.com/krishenriksen/notificationcenter), open it, and click "Patch Twister OS to the latest version". Once you open the patcher, make sure nothing important is running so you can reboot. Once it is open wait about 5 seconds to download the latest scripts and then  either it'll start downloading patches and rebooting, say you're on the latest patch and exit, or say you're offline and exit. If you have missed out on more than 1 patch, then you'll have to run it again until you get to the latest version because this is WHAT YOU GET for not updating.

### Commands
```
twistpatch:           Runs the main patcher script to patch Twister OS
twistpatch-update:    Removes and reinstalls TwistPatcher to get the latest code
twistpatch-remove:    Uninstalls TwistPatcher from your system
```

# Icon
![twister-update-blue.png](https://i.postimg.cc/65RvYzJG/twister-update-blue.png) [![twister-update.png](https://i.postimg.cc/8kxvR93S/twister-update.png)](https://postimg.cc/G9J9r7d7)<br>
If you don't like the default icon, then right-click on the application and select 'Edit application' for the application menu. For the desktop application, right clikc and select "Edit launcher". Then click on either one of the two other icons which are displayed above.<br>
[![18-08-2020-12-08-17-REC.png](https://i.postimg.cc/mkVFbMwh/18-08-2020-12-08-17-REC.png)](https://postimg.cc/8fJC47xV)<br>
[![18-08-2020-12-08-49-REC.png](https://i.postimg.cc/MZYBb2Sx/18-08-2020-12-08-49-REC.png)](https://postimg.cc/pypyRSr1)

# Support
If you have any problems, make an issue in this repository or go to the Pi Labs discord to connect with us at https://discord.gg/ttxhYrX

# Demonstration
This patcher has been featured by the following people:
[leepsvideo on Youtube](https://www.youtube.com/watch?v=EP1KWsvT4ME)

# Credits
[FlameKat53](https://github.com/FlameKat53): Main patch.sh and logic behind automatic patching. Started developing the code first.<br>
[mobilegmYT](https://github.com/mobilegmYT)/[Raspberry Pi News](https://www.youtube.com/channel/UCmp6JswV90SV5agNFGQuWkw): The idea of an automatic patcher, install.sh and various other pieces of code.<br>
[grayduck](https://www.youtube.com/channel/UCgfQjdc5RceRlTGfuthBs7g): Lending us his bash expertise and all graphics in this patcher.<br>
[phoenixbyrd](https://github.com/phoenixbyrd): Uploading files for us to the website.<br>
[kreal](https://github.com/krishenriksen): making checkforupdates.sh, modifying install.sh, and cron code.
[vlevit](https://github.com/vlevit/): https://github.com/vlevit/notify-send.sh

# Changes
Dev phase
- [x] Can install patch
- [x] Automatically update in order from current release to latest release
- [x] Uninstall script
- [x] Prefixes

Alpha/Beta
- [x] Make sure it works

Official release
- [x] Release program to public
