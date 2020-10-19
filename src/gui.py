#!/usr/bin/python
import sys
import os
import checkversion as cv
import resources as rs
import update as up
import tkinter as tk
import importlib
import webbrowser
from tkinter import messagebox as msb
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
home_path = sys.argv[1]
### Use in window class: master.protocol("WM_DELETE_WINDOW", lambda:on_Window_Close(master))
def on_Window_Close(master):
	master.destroy()

### Using to keybind window kill
def killwindow(event, master):
	on_Window_Close(master)

### Open new window with it's own master
def bopen(window):
	x = window()		


### Main window		
class Window:
	def __init__(master):

		master = tk.Tk()
		
		width = master.winfo_screenwidth()
		height = master.winfo_screenheight()
		
		xw = int(width)/2-210
		xw = int(xw)
		xh = int(height)/2-250
		xh = int(xh)
		
		xsize = "420x500+"+str(xw)+"+"+str(xh)
		#master.attributes('-type','dock')
		master.geometry(xsize)
		
		master.title("TwistPatch")
		master.resizable(False, False)
		#master.focus_force()

		mainframe = Frame(master)
		mainframe.pack(padx=10, pady=10)
		titleframe = Frame(mainframe)
		titleframe.pack()

		loadimg = Image.open(home_path+"/patcher/src/icons/title_logo.png")
		img = ImageTk.PhotoImage(image=loadimg)

		img_label = tk.Label ( titleframe, image=img)
		img_label.image = img
		img_label.grid(row=0, column=0, columnspan=2)

		separator = ttk.Separator(mainframe, orient='horizontal')
		separator.pack(fill=X, expand=True, pady=10)

		infoframe = Frame(mainframe)
		infoframe.pack(fill=X)

		twistver = tk.Label( infoframe, text= rs.twistver, fg="red", anchor='w')
		twistver.grid(row=1, column=0, columnspan=2, sticky=W)

		separator2 = ttk.Separator(mainframe, orient='horizontal')
		separator2.pack(fill=X, expand=True, pady=10)

		content_frame = Frame(mainframe)
		content_frame.hidden = 0
		content_frame.pack(fill=X)

		photo1 = PhotoImage(file = home_path+"/patcher/src/icons/update.png") 

		update_button = Button( content_frame, text="Update Twister OS", command = lambda:up.update_twist(), width=180, height=200, cursor="hand2", image = photo1, compound=TOP)
		update_button.grid(row=0, column=0, padx=0)
		update_button.pack(side=BOTTOM, pady=5)

		btn = Button( mainframe, text="About", command = lambda:change_frame(), font=("TkDefaultFont", 11, "bold"), cursor="hand2")
		btn.pack(side=BOTTOM, pady=5)

		content_frame2 = Frame(mainframe)

		about_label = tk.Label( content_frame2, text = "TwistPatch, Commander Pi 2020\n", justify=CENTER, font=("TkDefaultFont", 11, "bold"))
		about_label.pack()
		
		text_label = tk.Label( content_frame2, text="By Jack477\nFor Twister OS\n\nGraphic elements by grayduck\nApp idea by Raspberry Pi News\nTwistPatch by setLillie (FlameKat53) and Raspberry Pi News", justify=CENTER)
		text_label.pack(fill=X)
		
		version_label = tk.Label( content_frame2, text=rs.get_app_version(), font=("TkDefaultFont", 11, "bold"), justify=CENTER)
		version_label.pack()
		#cv.update()
		def on_click(self, event):
			self.focus_force()

		def change_frame():
			if content_frame.hidden == 0:
				content_frame.pack_forget()
				content_frame2.pack()
				btn['text'] = 'Back to main window'
				content_frame.hidden = 1
			else:
				content_frame2.pack_forget()
				content_frame.pack()
				btn['text'] = 'About/Update Patcher'
				content_frame.hidden = 0

		bind_label = tk.Label( mainframe, text="Press [Esc] to close", font=("TkDefaultFont", 11, "bold" ))
		bind_label.pack(side=BOTTOM)
		master.bind('<Escape>', lambda e:killwindow(e, master))
		master.bind("<Button>", lambda event:on_click(master, event))
		master.protocol("WM_DELETE_WINDOW", lambda:on_Window_Close(master))


		if sys.argv[2] == "1":
			up.update_twist()

		if up.check_online() == False:
			msb.showinfo(title="TwistPatch", message="Network is disconnected\nThe patcher will now close")
			sys.exit(0)

		master.mainloop()
