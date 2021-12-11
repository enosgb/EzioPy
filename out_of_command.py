import os
from tkinter import *
Outputfileobject=os.popen("ipconfig /all")
Output=Outputfileobject.read()
Outputfileobject.close()
root=Tk()
root.title("Output text")
Text=Label(root,text=Output).pack()
root.mainloop()