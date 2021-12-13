'''
import os
from tkinter import *

lista = []

if (os.system('quser 062613 /server:10.1.0.29')== 0):
   print('Usuario encontrado')
   Outputfileobject=os.popen('quser 062613 /server:10.1.0.29')
   lista.append(Outputfileobject.read())
   Outputfileobject.close()
  # lista.append(Output.split('                                    '))
   lista.remove('USERNAME')
   print(lista)
else:
   print('Usuario nao encontrado')

'''

import os

retvalue = os.popen("quser /server:10.1.0.29").read()

print(retvalue)