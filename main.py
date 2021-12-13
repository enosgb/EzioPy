import os
from tkinter import *


if (os.system('quser 070580 /server:RDESK02.unifeso.lan')== 0):
   print('Usuario encontrado')
   Outputfileobject=os.popen('quser 070580 /server:RDESK02.unifeso.lan')
   Output=Outputfileobject.read()
   Outputfileobject.close()
   print(Output.)
else:
   print('Usuario nao encontrado')