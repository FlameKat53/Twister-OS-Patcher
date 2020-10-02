# TwistPatch
![](https://media.discordapp.net/attachments/738534235194916884/759921733825462322/TwisterOSPatcherLogo.png?width=960&height=186)<br>
An updater for Twister OS that downloads, unzips, and runs the latest patch for Twister OS. It is fine if you run the patcher more than once as it auto-detects your version. when you run the patcher, you must reboot your computer after patching completes.<br>


#### Go support Twister OS!</br>
### <a href="https://twisteros.com/">>Twister OS<</a>

# Install/Update
`wget https://raw.githubusercontent.com/FlameKat53/Twister-OS-Patcher/master/install.sh && chmod +x ./install.sh && ./install.sh && rm install.sh`<br>
If you notice the repo has been changed, run `twistpatch-update` to update your current version of the patcher.

# Uninstall
`twistpatch-remove`

# Usage
[![Screenshot-2020-09-21-11-40-47.png](https://i.postimg.cc/JzSG6D3p/Screenshot-2020-09-21-11-40-47.png)](https://postimg.cc/NK7sL0zX) [![Screenshot-2020-09-21-11-41-29.png](https://i.postimg.cc/0NmrLkcP/Screenshot-2020-09-21-11-41-29.png)](https://postimg.cc/CZhF8V3Q)<br>
There are 3 ways to open the patcher. Firstly, you can click on the "Twister OS Patcher" in your applications menu. Secondly, you can type "twistpatch" into terminal, and thirdly, you can use the "Patch Twister OS" button in notificationcenter. it will take a while to open, but once you open the patcher, make sure nothing important is running(compiling, unsaved mc worlds, etc)because you have to reboot after the patch. Once it is open, click the big button labeled "Update Twister OS" to download the latest scripts to check for updates. It will either start downloading patches and rebooting, or say you are on the latest patch and exit, or say you're offline and then exit. 
If you have missed out on more than 1 patch, then you will have to run the patcher after each reboot due to the nature of how the patches install updates.

### Commands
```
twistpatch:           Runs the main patcher script to patch Twister OS
twistpatch-update:    Removes and reinstalls TwistPatcher to get the latest code
twistpatch-remove:    Uninstalls TwistPatcher from your system
```

# Icon
![twister-update-blue.png](https://i.postimg.cc/65RvYzJG/twister-update-blue.png) [![twister-update.png](https://i.postimg.cc/8kxvR93S/twister-update.png)](https://postimg.cc/G9J9r7d7)<br>
If you don't like the default icon, then right-click on the application icon and select 'Edit application', then click on either one of the two other icons that are in the folder, which are displayed above.<br>
[![18-08-2020-12-08-17-REC.png](https://i.postimg.cc/mkVFbMwh/18-08-2020-12-08-17-REC.png)](https://postimg.cc/8fJC47xV)<br>
[![18-08-2020-12-08-49-REC.png](https://i.postimg.cc/MZYBb2Sx/18-08-2020-12-08-49-REC.png)](https://postimg.cc/pypyRSr1)

# Support
We have tested the code extensively, but mistakes do happen. If you have any problems, make an issue in this repository or go to the Pi Labs discord to connect with us at https://discord.gg/ttxhYrX

# Demonstration
The patcher has been featured in these places:<br>
[Raspberry Pi News](https://www.youtube.com/watch?v=bTTF0VT_ClM)<br>
[leepspvideo on Youtube](https://www.youtube.com/watch?v=EP1KWsvT4ME)

# Credits
[FlameKat53](https://github.com/FlameKat53): Main patch.sh and logic behind automatic patching. Started developing the code first.<br>
[Raspberry Pi News](https://www.youtube.com/channel/UCmp6JswV90SV5agNFGQuWkw): The idea of an automatic patcher, install.sh and various other pieces of code.<br>
[grayduck](https://www.youtube.com/channel/UCgfQjdc5RceRlTGfuthBs7g): Lending us his bash expertise and all graphics in this patcher.<br>
[phoenixbyrd](https://github.com/phoenixbyrd): Uploading files for us to the website.<br>
[kreal](https://github.com/krishenriksen): making checkforupdates.sh, modifying install.sh, and cron code.<br>
[vlevit](https://github.com/vlevit/): https://github.com/vlevit/notify-send.sh<br>
[Jack477](https://github.com/Jack477): Letting us steal GUI code from CommanderPi and lending us python help. https://github.com/Jack477/CommanderPi

# Changes
Dev phase
- [x] Can install patch
- [x] Automatically update in order from current release to latest release
- [x] Uninstall script
- [x] Prefixes

Alpha/Beta
- [x] Make sure it works

Official release
- [x] Release program to public and inclusion in patch 1.6
- [x] Release the Python3 patcher to public and inclusion in patch 1.8.2
