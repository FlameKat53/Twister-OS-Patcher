import os
import resources as rs
import schedule
import time

def job():
    if rs.twistver != rs.webversion:
        os.system('WEBVERSION=$(curl https://twisteros.com/Patches/latest.txt) && /home/pi/patcher/notify-send.sh --urgency=normal --expire-time=20000 --app-name=TwistPatch --icon=/home/pi/patcher/icons/src/arrow-white.png --action=Update:/home/pi/patcher/src/start.sh "A new Twister OS update is now avaliable, click [Update] to update to" "$WEBVERSION"')

schedule.every().saturday.at("12:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(604800)
