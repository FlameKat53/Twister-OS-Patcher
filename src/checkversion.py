import subprocess as sp
import resources as rs
import os
import wget
from tkinter import messagebox as msb
import urllib.request
versions = []
verbuff = ""
def other():
	msb.showinfo(title="TwistPatch", message='Extracting zip... Press OK to begin extraction.')
	os.system('unzip patch.zip')
	os.system('rm patch.zip')
	msb.showinfo(title="TwistPatch", message='The patcher will begin updating your system\npress OK to continue')
	os.system('chmod +x *patchinstall.sh')
	os.system('xfce4-terminal -e ./*patchinstall.sh')


	
def update():
	if os.path.exists('/usr/local/bin/twistver') == False:
		if os.path.exists('/usr/bin/xscreensaver') == False:
			answer = msb.askyesno(title="TwistPatch", message='You appear to be running Twister OS version 1.0\nIs this correct?')
			if answer == True:
				msb.showinfo(title="TwistPatch", message='Downloading 1.1.0 Patch in the background...\nPress OK to begin downloading.')
				wget.download('https://twisteros.com/Patches/TwisterOSv1-1Patch.zip', out='/home/pi/patcher/src/patch.zip')
				other()

		if os.path.exists('/usr/bin/com.github.libredeb.lightpad') == False:
			answer =  msb.askyesno(title="TwistPatch", message='You appear to be running Twister OS version 1.1\nIs this correct?')
			if answer == True:
				msb.showinfo(title="TwistPatch", message='Downloading 1.2.0 Patch in the background...\nPress OK to begin downloading.')
				wget.download('https://twisteros.com/Patches/TwisterOSv1-2Patch.zip', out='/home/pi/patcher/src/patch.zip')
				other()

		if os.path.exists('/home/pi/WebApps/Discord/discord.sh') == False:
			answer = msb.askyesno(title="TwistPatch", message='You appear to be running Twister OS version 1.2\nIs this correct?')
			if answer == True:
				msb.showinfo(title="TwistPatch", message='Downloading 1.3.0 Patch in the background...\nPress OK to begin downloading.')
				wget.download('https://twisteros.com/Patches/TwisterOSv1-3Patch.zip', out='/home/pi/patcher/src/patch.zip')
				other()

		if os.path.exists('/usr/share/ThemeSwitcher/Raspbian95/splash.png') == False:
			answer = msb.askyesno(title="TwistPatch", message='You appear to be running Twister OS version 1.4.0\nIs this correct?')
			if answer == True:
				msb.showinfo(title="TwistPatch", message='Downloading 1.4.1 Patch in the background...\nPress OK to begin downloading.')
				wget.download('https://archive.org/download/twister-osv-1-4-1-patch/TwisterOSv1-4-1Patch.zip', out='/home/pi/patcher/src/patch.zip')
				other()

		if os.path.exists('/usr/share/ThemeSwitcher/RaspbianXP/splash.png') == False:
			answer = msb.askyesno(title="TwistPatch", message='You appear to be running Twister OS version 1.4.1\nIs this correct?')
			if answer == True:
				msb.showinfo(title="TwistPatch", message='Downloading 1.5.0 Patch in the background...\nPress OK to begin downloading.')
				wget.download('https://twisteros.com/Patches/TwisterOS1-5Patch.zip', out='/home/pi/patcher/src/patch.zip')
				other()

		if os.path.exists('/usr/local/bin/twistver') == False:
			answer = msb.askyesno(title="TwistPatch", message='You appear to be running Twister OS version 1.5.0 or 1.5.1\nIs this correct?')
			if answer == True:
				msb.showinfo(title="TwistPatch", message='Downloading 1.5.2 Patch in the background...\nPress OK to begin downloading.')
				wget.download('https://twisteros.com/Patches/TwisterOSv1-5-2Patch.zip', out='/home/pi/patcher/src/patch.zip')
				other()

	else:
			my_ver = rs.twistver[19:]
			my_ver = my_ver+" "
			
			print(my_ver)
			
			xverbuff = ""
			xver = [] #every element is a number from x.x.x sketch 3 - size
			for c in my_ver:
				print(xverbuff)
				if c.isnumeric():
					print('it is a number')
					xverbuff = xverbuff+c
				else:
					print(c)
					xver.append(xverbuff)
					xverbuff = ""
			version_link = ""
			for x in xver:
				print(x)
				
			versions = []
			url = "https://twisteros.com/Patches/latest.txt"
			with urllib.request.urlopen(url) as f:
				xcontent = f.read().decode('utf-8')
				xcontent = xcontent.splitlines()
				xversion = ""
				for line in xcontent:
					if "Twister OS version" in line:
						versions.append(line)	

			versions_reverse = versions[::-1]
			for d in versions_reverse:
				print(d)
			for ver in versions_reverse:
				print(ver)
				nmy_ver = ver[19:]
				nmy_ver = nmy_ver+" "
				print("It works")
				print(nmy_ver)
			
				xnverbuff = ""
				xnver = [] #every element is a number from x.x.x sketch 3 - size
				for c in nmy_ver:
					print(xnverbuff)
					if c.isnumeric():
						print('it is a number')
						xnverbuff = xnverbuff+c
					else:
						print(c)
						xnver.append(xnverbuff)
						xnverbuff = ""
				if (xver[2] == None) and (xnver[1]!=xver[1]) or (xnver[0]!=xver[0]):
					version_link = 'https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'Patch.zip'
					if (((xnver[0]>=xver[0]) and (xnver[1]>xver[1]))):
						msb.showinfo(title="TwistPatch", message='Downloading '+xnver[0]+'.'+xnver[1]+' Patch in the background...\nPress OK to begin downloading.')
						wget.download('https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'Patch.zip', out='/home/pi/patcher/src/patch.zip')
						other()
						break
				elif (xnver[2] != xver[2]) or (xnver[1]!=xver[1]) or (xnver[0]!=xver[0]):
					version_link = 'https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'-'+xnver[2]+'Patch.zip'
					if (((xnver[0]>=xver[0]) and (xnver[1]>=xver[1]) and (xnver[2]>xver[2]))):
						msb.showinfo(title="TwistPatch", message='Downloading '+xnver[0]+'.'+xnver[1]+'.'+xnver[2]+' Patch in the background...\nPress OK to begin downloading.')
						wget.download('https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'-'+xnver[2]+'Patch.zip', out='/home/pi/patcher/src/patch.zip')
						other()
						break
			msb.showinfo(title="TwistPatch", message='You have already the newest version of TwisterOS: '+str(xver[0])+'.'+str(xver[1])+'.'+str(xver[2]))	

			
			
