from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
	root.destroy()
	
def count_down():
	timeleft = endTime - datetime.datetime.now()
	timeleft = timeleft -datetime.timedelta(microseconds=timeleft.microseconds)
	
	txt.set(timeleft)
	
	root.after(1000,count_down)
	
root = Tk()
root.attributes("-fullscreen",False)
root.configure(background='black')
root.bind("x",quit)
root.after(1000,count_down)

a=int(input("Enter the year"))
b=int(input("Enter the month"))
c=int(input("Enter the date"))
h=int(input("Enter the hour of event"))
m=int(input("Enter the minunte of event"))

endTime = datetime.datetime(a,b,c,h,m,0)


fnt =font.Font(family='Helvetica',size=120,weight='bold')
txt =StringVar()
lbl=ttk.Label(root, textvariable=txt ,font=fnt,foreground="white", background="black")
lbl.place(relx=0.5,rely=0.5, anchor=CENTER)

mainloop()
