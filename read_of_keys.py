import tkinter as tk
from tkinter.constants import ANCHOR, CENTER, LEFT, RIGHT, TOP
from tkinter import Widget, ttk
import types
import os

window = tk.Tk()
window.geometry("700x500")
window.title("Ezio Kill Users")

#def getTextInput():
 #   result=textExample.get(1.0, tk.END+"-1c")
  #  print(result)


columns = ('user','session','name')

tree = ttk.Treeview(window,height=20,columns=columns,show='headings')
tree.heading('user',text='Usuário')

tree.insert('', 'end', text='user', values=(os.system('qwinsta /server:RDESK02.unifeso.lan')))


tree.grid(column=0,row=1)


txt_usuario = tk.Text(window, height=1.5, width=75)
txt_usuario.grid(column = 0, row = 0)

btn_buscar_usuario = tk.Button(window, height = 1, width = 10, text="Buscar",padx = 10)
btn_buscar_usuario.grid(column = 1, row = 0)
btn_gerar_lista_usuarios = tk.Button(window, height = 1 , width = 10, text="Gerar Usuarios")
btn_gerar_lista_usuarios.grid(column = 0, row = 2,padx=1,pady=1)
btn_finalizar_sessao = tk.Button(window, height = 1, width = 10, text="Finalizar")
btn_finalizar_sessao.grid(column = 1,row = 2,padx = 10)

#btnRead=tk.Button(root, height=1, width=10, text="Read", 
#                    command=getTextInput)

#btnRead.pack()

window.mainloop()