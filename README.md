# TwistPatcher
[![tos-patcher-new2.png](https://i.postimg.cc/rwTFyXLs/tos-patcher-new2.png)](https://postimg.cc/Mvs8tLHJ)<br>
An updater for Twister OS that automatically downloads, unzips, and runs the latest patch for Twister OS. It is fine if you run the patcher more than once as it auto-detects your version. You have to run the patcher when you can reboot your computer as it is required for patching.<br>


#### Go support Twister OS!</br>
### <a href="https://twisteros.com/">>Twister OS<</a>

# Install/Update
`wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh`<br>
If you notice the repo has been changed, run `twistpatch-update` to update your current version of the patcher.

# Uninstall
`twistpatch-remove`

# Usage
[![18-08-2020-08-02-21-REC.png](https://i.postimg.cc/cHq94jWb/18-08-2020-08-02-21-REC.png)](https://postimg.cc/DWgdxx8r)<br>
To use the patcher you can go in the applications menu and search for Twister OS Patcher in the system section, or type the commands below. Click on it and a terminal window will open. If a window pops-up saying the file is untrusted, just click 'Mark Executable'. Press enter to continue and the program will check to see which version you are on and if you are on the latest version, it'll tell you and you can close it with [Enter]. If you are on an old patch, it'll confirm your current version which you can check by typing `twistver`. If it is correct press [Enter] and it will automatically run the patch and reboot for you. Every Sunday at 11:00AM, a notification will be sent if there is a patch you can install.

### Commands
```
twistpatch:           Runs the main patcher script to patch Twister OS
twistpatch-update:    Removes and reinstalls TwistPatcher to get the latest code
twistpatch-remove:    Uninstalls TwistPatcher from your system
```

# Icon
[![twister-update-blue.png](https://i.postimg.cc/6qNWSdHT/twister-update-blue.png)](https://postimg.cc/HcB1871C)  [![twister-update.png](https://i.postimg.cc/zfgjCcfs/twister-update.png)](https://postimg.cc/xk9MYgM5)<br>
If you don't like the default icon, then right-click on the application and select 'Edit application'. Then click on either one of the two other icons which are displayed above.<br>
[![18-08-2020-12-08-17-REC.png](https://i.postimg.cc/mkVFbMwh/18-08-2020-12-08-17-REC.png)](https://postimg.cc/8fJC47xV)<br>
[![18-08-2020-12-08-49-REC.png](https://i.postimg.cc/MZYBb2Sx/18-08-2020-12-08-49-REC.png)](https://postimg.cc/pypyRSr1)

# Support
If you have any problems, make an issue in this repository or go to the Pi Labs discord to connect with us at https://discord.gg/ttxhYrX

# Demonstration
This patcher has been featured in the following places:


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
