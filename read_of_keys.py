import tkinter as tk
from tkinter.constants import LEFT, RIGHT, TOP
from tkinter import Listbox, StringVar, ttk


window = tk.Tk()
window.geometry("320x250")
window.title("Ezio Kill Users")

#def getTextInput():
 #   result=textExample.get(1.0, tk.END+"-1c")
  #  print(result)

lista = Listbox(height=10)
choices = ["apple", "orange", "banana"]
choicesvar = StringVar(value=choices)
lista = Listbox(listvariable=choicesvar)
#choices.append("peach")
#choicesvar.set(choices)
lista.grid(column = 0, row=1)




txt_usuario = tk.Text(window, height=1.5, width=25)
txt_usuario.grid(column = 0, row = 0, padx = 10, pady = 10)

btn_buscar_usuario = tk.Button(window, height = 1, width = 10, text="Buscar")
btn_buscar_usuario.grid(column = 1, row = 0, padx = 10, pady = 10)
btn_gerar_lista_usuarios = tk.Button(window, height = 1 , width=10, text="Gerar Usuarios")

#btnRead=tk.Button(root, height=1, width=10, text="Read", 
#                    command=getTextInput)

#btnRead.pack()

window.mainloop()