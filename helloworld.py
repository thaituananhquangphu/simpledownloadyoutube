from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
import youtube_dl
import tkinter as tk

win = tk.Tk()

win.title("youtube_dl")
win.geometry('500x200')

#Download Videos Youtube.
def download():
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([txt.get()])
#Add Button
btn = Button(win, text="Download", command = download)
btn.grid(column = 0, row = 0, sticky = W)
#Add Entry
txt = Entry(win, width=30)
txt.grid(column = 1, row = 0, sticky = W)
#Add Label
lbl = Label(win, text ="Do you want format files?")
lbl.grid(column = 0, row = 1, sticky = W)
#Add Combobox
combo = Combobox(win, width=29)
combo['values']=("best","worst","bestvideo","worstvideo","bestaudio","worstaudio")
combo.current(0)
combo.grid(column=1, row=1, sticky = W)
#Add scrolledtext
scrtxt = scrolledtext.ScrolledText(win, width=60, height=10)
scrtxt.grid(columnspan = 2, row = 2, sticky = W)

win.mainloop()
