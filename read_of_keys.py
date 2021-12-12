import tkinter as tk
from tkinter.constants import ANCHOR, CENTER, LEFT, RIGHT, TOP
from tkinter import Widget, ttk
import types


window = tk.Tk()
window.geometry("700x400")
window.title("Ezio Kill Users")

#def getTextInput():
 #   result=textExample.get(1.0, tk.END+"-1c")
  #  print(result)


columns = ('user','session','name')

tree = ttk.Treeview(window,height=15,columns=columns,show='headings')
tree.heading('user',text='Usuário')
tree.heading('session',text='Sessão')
tree.heading('name',text='Nome')

tree.insert('', 'end', text='user', values=('073933','443','Enos Gabriel'))


tree.grid(column=0,row=1)


txt_usuario = tk.Text(window, height=1.5, width=75)
txt_usuario.grid(column = 0, row = 0)

btn_buscar_usuario = tk.Button(window, height = 1, width = 10, text="Buscar")
btn_buscar_usuario.grid(column = 1, row = 0, padx = 10, pady = 10)
btn_gerar_lista_usuarios = tk.Button(window, height = 1 , width=10, text="Gerar Usuarios")

#btnRead=tk.Button(root, height=1, width=10, text="Read", 
#                    command=getTextInput)

#btnRead.pack()

window.mainloop()