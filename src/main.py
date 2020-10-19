#!/usr/bin/python
import gui as g
import cliupdate as cup
import tkinter as tk
import resources as rs
from tkinter import *

version = 4.0
if sys.argv[3] == "1":
	def main():
		cup.update()
else:
	def main():
		g.Window()

main()
