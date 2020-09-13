#!/usr/bin/python
import sys
import os
import resources as rs
import update as up
import tkinter as tk
import theme as th
import importlib
import webbrowser
from tkinter import messagebox as msb
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

### TODO: Move change_theme function to theme.py?
### split resources.py into smaller files
### move window_list from theme.py to resources
home_path = sys.argv[1]
def change_theme(master):
	if int(th.color_mode)==0:
		print("Setting color theme to 1")
		th.color_mode=1
	else:
		th.color_mode=0
	rs.config.set('DEFAULT', 'color_mode', str(th.color_mode))
	with open(home_path+'/patcher/src/pat.config', 'w') as configfile:
		rs.config.write(configfile)
	th.set_theme(master)
	#print(th.color_mode)

### Use in window class: master.protocol("WM_DELETE_WINDOW", lambda:on_Window_Close(master))
def on_Window_Close(master):
	if isinstance(master, tk.Tk):
		window_name = master.__class__
		print(window_name)
		th.window_list.pop()
	master.destroy()

### Using to keybind window kill
def killwindow(event, master):
	on_Window_Close(master)

### Open new window with it's own master
def bopen(window):
	x = window()			

class Proc_Info_Window:

	def __init__(master):
	
		master = tk.Tk()
		master.geometry("350x400")
		master.title("TwistPatch")
		th.window_list.append(master)
		th.set_theme(master)
		mainframe = Frame(master)
		mainframe.pack(padx=10, pady=10)	
		
		titleframe = Frame(mainframe)
		titleframe.pack(fill=X)
				
		image = Image.open(home_path+"/patcher/src/icons/update.png")
		photo = ImageTk.PhotoImage(image, master=titleframe) 

		title_label = tk.Label( titleframe, text = "Update Twister OS", font=("TkDefaultFont", 18, "bold"), image = photo, compound=LEFT, anchor='w')
		title_label.image = photo
		title_label.pack(side=BOTTOM)
		title_labell = Button(mainframe, text="Check for updates", command=lambda:up.update_twist(), cursor="hand2", font=("TkDefaultFont", 11, "bold"))
		title_labell.pack()

		def update_ou():
			up.update_twister()
	
		separator = ttk.Separator(mainframe, orient='horizontal')
		separator.pack(fill=X, expand=True, pady=15)
		
		separator2 = ttk.Separator(mainframe, orient='horizontal')
		separator2.pack(fill=X, expand=True, pady=15)	
		
		bind_label = tk.Label( mainframe, text="Press [Esc] to close", font=("TkDefaultFont", 11, "bold") )
		bind_label.pack(side=BOTTOM)
		master.bind('<Escape>', lambda e:killwindow(e, master))
		master.protocol("WM_DELETE_WINDOW", lambda:on_Window_Close(master))	
		master.mainloop()

class About_Window:

	def __init__(master):
	
		master = tk.Tk()
		master.geometry("400x450")
		master.title("TwistPatch")
		th.window_list.append(master)
		mainframe = Frame(master)
		mainframe.pack(padx=10, pady=10)	
		
		titleframe = Frame(mainframe)
		titleframe.pack(fill=X)
				
		image = Image.open(home_path+"/patcher/src/icons/logo.png")
		photo = ImageTk.PhotoImage(image, master=titleframe) 

		title_label = tk.Label( titleframe, text = "About Application", font=("TkDefaultFont", 18, "bold"), image = photo, compound=LEFT, anchor='w')
		title_label.image = photo
		title_label.pack(side=LEFT)
	
		separator = ttk.Separator(mainframe, orient='horizontal')
		separator.pack(fill=X, expand=True, pady=15)		

		content_frame = Frame(mainframe)
		content_frame.pack()
		
		about_label = tk.Label( content_frame, text = "TwistPatch, Commander Pi 2020\n", justify=CENTER, font=("TkDefaultFont", 11, "bold"))
		about_label.pack()
		
		text_label = tk.Label( content_frame, text="By Jack477\nFor Twister OS\n\nGraphic elements by grayduck\nApp idea by Salva\nTwistPatch (Python3 edition) coded by setLillie", justify=CENTER)
		text_label.pack(fill=X)
		
		version_label = tk.Label( content_frame, text=rs.get_app_version(), font=("TkDefaultFont", 11, "bold"), justify=CENTER)
		version_label.pack()
		
		link = tk.Label( content_frame, text="Changelog", cursor="hand2", fg="#1D81DA", pady=5)
		link.pack(fill=X)
		mlink = 'https://github.com/FlameKat53/Twister-OS-Patcher/blob/master/CHANGELOG.md'
		link.bind("<Button-1>", lambda e: rs.cpi_open_url(mlink))
		
		separator2 = ttk.Separator(mainframe, orient='horizontal')
		separator2.pack(fill=X, expand=True, pady=15)
		
		update_button = Button(mainframe, text="Check for patcher updates", command=lambda:update_x(), cursor="hand2", font=("TkDefaultFont", 11, "bold"))
		update_button.pack()

		color_buton = Button(mainframe, text="Change theme color", command=lambda:change_theme(master), cursor="hand2", font=("TkDefaultFont", 11, "bold"))
		color_buton.pack()

		def update_x():
			up.update_cpi()

		
		bind_label = tk.Label( mainframe, text="Press [Esc] to close", font=("TkDefaultFont", 11, "bold") )
		bind_label.pack(side=BOTTOM)
		master.bind('<Escape>', lambda e:killwindow(e, master))
		th.set_theme(master)
		master.protocol("WM_DELETE_WINDOW", lambda:on_Window_Close(master))		
		master.mainloop()

### Main window		
class Window:
	def __init__(master):

		master = tk.Tk()
		master.geometry("420x500")
		master.title("TwistPatch")
		master.resizable(False, False)
		th.window_list.append(master)
		mainframe = Frame(master)
		mainframe.pack(padx=10, pady=10)
		
		
		titleframe = Frame(mainframe)
		titleframe.pack()
		
		loadimg = Image.open(home_path+"/patcher/src/icons/title_logo.png")
		img = ImageTk.PhotoImage(image=loadimg)

		img_label = tk.Label ( titleframe, image=img)
		img_label.image = img
		img_label.grid(row=0, column=0, columnspan=2)
		
		#title_label = tk.Label( titleframe, text = "TwistPatch", font=("TkDefaultFont", 22, "bold") )
		#title_label.grid(row=0, column=1)
		
		separator = ttk.Separator(mainframe, orient='horizontal')
		separator.pack(fill=X, expand=True, pady=10)
		
		infoframe = Frame(mainframe)
		infoframe.pack(fill=X)
		
		twistver = tk.Label( infoframe, text= rs.twistver, fg="red", anchor='w')
		twistver.grid(row=1, column=0, columnspan=2, sticky=W)
		
		separator2 = ttk.Separator(mainframe, orient='horizontal')
		separator2.pack(fill=X, expand=True, pady=10)

		#REFRESH CPU USAGE, MEMORY USAGE AND TEMPERATURE
		def refresh():
			master.after(1000, refresh)
			
		refresh()
		
		btn_frame = Frame(mainframe)
		btn_frame.pack(fill=X)
		
		photo1 = PhotoImage(file = home_path+"/patcher/src/icons/update.png") 
		#photoimage1 = photo1.subsample(15, 15) 
		
		proc_info_button = Button ( btn_frame, text="Update Twister OS", command = lambda:bopen(Proc_Info_Window), width=180, height=200, cursor="hand2", image = photo1, compound=TOP)
		proc_info_button.grid(row=0, column=0, padx=0)
		proc_info_button.pack(side=BOTTOM, pady=5)
		
		btn3 = Button( mainframe, text="About/Update the Patcher", command = lambda:bopen(About_Window), font=("TkDefaultFont", 11, "bold"), cursor="hand2")
		btn3.pack(side=BOTTOM, pady=5)
		
		#d = Info_Window()
		master.protocol("WM_DELETE_WINDOW", lambda:on_Window_Close(master))
		th.set_theme(master)
		#up.check_update()
		master.mainloop()
		
