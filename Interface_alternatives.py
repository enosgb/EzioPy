from tkinter import *
import os
 
#window
mywin=Tk()
 
#function about to close window
def close_window (root): 
    root.destroy()
 
#function about to read fstab
def fstab():
    os.system("ipconfig")
 
#size window
mywin.geometry("600x400+600+100")
mywin.title('WINDOW')
 
#text in window
mytext=Label(text='View', fg='white', bg='black', font=('Helvetica',30)).pack()
 
#button GO!
gobutton=Button(text='GO!', command = fstab).pack()
 
#frame for my output
myframe=Frame(width=300, height=300).pack()
 
#button Exit
exitbutton=Button (mywin, text="Exit", command = lambda: close_window(mywin)).pack()
 
#go mainloop
mywin.mainloop()