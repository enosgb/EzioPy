import os
from tkinter import *
Outputfileobject=os.popen('qwinsta /server:RDESK02.unifeso.lan')
Output=Outputfileobject.read()
Outputfileobject.close()
root=Tk()
root.title("Output text")
Text=Label(root,text=Output).pack()
root.mainloop()