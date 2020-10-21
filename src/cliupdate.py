import resources as rs
import os
import wget
import urllib.request
versions = []
verbuff = ""
def other():
	print('Extracting zip...')
	os.system('rm *patchinstall.sh')
	os.system('unzip patch.zip')
	os.system('rm patch.zip')
	print('The patcher will begin updating your system')
	os.system('chmod +x *patchinstall.sh')
	os.system('xfce4-terminal -e ./*patchinstall.sh')


	
def update():
	if os.path.exists('/usr/local/bin/twistver') == False:
		if os.path.exists('/usr/bin/xscreensaver') == False:
			os.system('bash -c "read -p \'You appear to be running Twister OS version 1.0 [Enter] for Yes, otherwise press [CTRL C]\'"')
			print('Downloading 1.1.0 Patch...')
			wget.download('https://twisteros.com/Patches/TwisterOSv1-1Patch.zip', out='/home/pi/patcher/src/patch.zip')
			other()

		if os.path.exists('/usr/bin/com.github.libredeb.lightpad') == False:
			os.system('bash -c "read -p \'You appear to be running Twister OS version 1.1 [Enter] for Yes, otherwise press [CTRL C]\'"')
			print('Downloading 1.2.0 Patch...')
			wget.download('https://twisteros.com/Patches/TwisterOSv1-2Patch.zip', out='/home/pi/patcher/src/patch.zip')
			other()

		if os.path.exists('/home/pi/WebApps/Discord/discord.sh') == False:
			os.system('bash -c "read -p \'You appear to be running Twister OS version 1.2 [Enter] for Yes, otherwise press [CTRL C]\'"')
			print('Downloading 1.3.0 Patch...')
			wget.download('https://twisteros.com/Patches/TwisterOSv1-3Patch.zip', out='/home/pi/patcher/src/patch.zip')
			other()

		if os.path.exists('/usr/share/ThemeSwitcher/Raspbian95/splash.png') == False:
			os.system('bash -c "read -p \'You appear to be running Twister OS version 1.3 [Enter] for Yes, otherwise press [CTRL C]\'"')
			print('Downloading 1.4.1 Patch...')
			wget.download('https://archive.org/download/twister-osv-1-4-1-patch/TwisterOSv1-4-1Patch.zip', out='/home/pi/patcher/src/patch.zip')
			other()

		if os.path.exists('/usr/share/ThemeSwitcher/RaspbianXP/splash.png') == False:
			os.system('bash -c "read -p \'You appear to be running Twister OS version 1.4.1 [Enter] for Yes, otherwise press [CTRL C]\'"')
			print('Downloading 1.5.0 Patch...')
			wget.download('https://twisteros.com/Patches/TwisterOS1-5Patch.zip', out='/home/pi/patcher/src/patch.zip')
			other()

		if os.path.exists('/usr/local/bin/twistver') == False:
			os.system('bash -c "read -p \'You appear to be running Twister OS version 1.5.0 or 1.5.1, [Enter] for Yes, otherwise press [CTRL C]\'"')
			print('Downloading 1.5.2 Patch...')
			wget.download('https://twisteros.com/Patches/TwisterOSv1-5-2Patch.zip', out='/home/pi/patcher/src/patch.zip')
			other()

	else:
			my_ver = rs.twistver[19:]
			my_ver = my_ver+" "

			xverbuff = ""
			xver = [] #every element is a number from x.x.x sketch 3 - size
			for c in my_ver:
				if c.isnumeric():
					xverbuff = xverbuff+c
				else:
					xver.append(xverbuff)
					xverbuff = ""
			version_link = ""
			url = "https://twisteros.com/Patches/latest.txt"
			with urllib.request.urlopen(url) as f:
				xcontent = f.read().decode('utf-8')
				xcontent = xcontent.splitlines()
				xversion = ""
				for line in xcontent:
					if "Twister OS version" in line:
						versions.append(line)	

			versions_reverse = versions[::-1]
			for ver in versions_reverse:
				nmy_ver = ver[19:]
				nmy_ver = nmy_ver+" "
			
				xnverbuff = ""
				xnver = [] #every element is a number from x.x.x sketch 3 - size
				for c in nmy_ver:
					if c.isnumeric():
						xnverbuff = xnverbuff+c
					else:
						xnver.append(xnverbuff)
						xnverbuff = ""
				if (xver[2] == None) or (xnver[1]!=xver[1]) or (xnver[0]!=xver[0]):
					version_link = 'https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'Patch.zip'
					if (((xnver[0]>=xver[0]) and (xnver[1]>xver[1]))):
						print('Downloading '+xnver[0]+'.'+xnver[1]+'.'+xnver[2]+' Patch...')
						wget.download('https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'Patch.zip', out='/home/pi/patcher/src/patch.zip')
						other()
						break
				elif (xnver[2] != xver[2]) or (xnver[1]!=xver[1]) or (xnver[0]!=xver[0]):
					version_link = 'https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'-'+xnver[2]+'Patch.zip'
					if (((xnver[0]>=xver[0]) and (xnver[1]>=xver[1]) and (xnver[2]>xver[2]))):
						print('Downloading '+xnver[0]+'.'+xnver[1]+'.'+xnver[2]+' Patch...')
						wget.download('https://twisteros.com/Patches/TwisterOSv'+xnver[0]+'-'+xnver[1]+'-'+xnver[2]+'Patch.zip', out='/home/pi/patcher/src/patch.zip')
						other()
						break
			print('You already have the newest version of TwisterOS: version '+str(xver[0])+'.'+str(xver[1])+'.'+str(xver[2]))	

			
			
