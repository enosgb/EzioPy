from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter as tk
import os


window = Tk()
window.resizable(height=None,width=None)
window.title('Ezio Killer')


#FUNCTIONS



def return_usuario(event):
    #usuario = txt_usuario.get("1.0","end")
    usuario ='065765'
    return usuario
        
def busca_usuario(usuario):
    if(os.system('quser '+usuario+' /server:10.1.0.19'))==0:
        contacts = os.popen('quser '+usuario+' /server:10.1.0.19').read()
        contacts = contacts.split()
        tree.insert('',tk.END, values=(contacts[9],contacts[8],contacts[10],contacts[11]))
    else:
        print('usuario nao encontrado')




#define txt box
txt_usuario = tk.Text(window,height=1,width=50)
txt_usuario.grid(row=1,column=0,padx=10,pady=10)
window.bind('<Return>', return_usuario)




#define buttons
btn_buscar = ttk.Button(window,text='Buscar')
btn_buscar.grid(row=1,column=4,padx=5,pady=15)
btn_buscar.bind('<Button-1>', return_usuario)
btn_finalizar = ttk.Button(window,text='Finalizar')
btn_finalizar.grid(row=3,column=4,padx=10,pady=10)


#define table treeview
tree = Treeview(window, selectmode="extended", columns=("SESSIONNAME", "USERNAME","ID","ESTATE"),show='headings')
tree.grid(row=2,column=0,padx=10,pady=10)

#define columns and headings
tree.heading("#1", text="Nome da Sessão")
tree.column("#1", minwidth=0, width=100, stretch=NO)
tree.heading("#2", text="Usuário")
tree.column("#2", minwidth=0, width=100, stretch=NO) 
tree.heading("#3", text="ID da Sessão")
tree.column("#3", minwidth=0, width=100, stretch=NO)
tree.heading("#4", text="Estado")
tree.column("#4", minwidth=0, width=100, stretch=NO)

print(return_usuario)
window.mainloop()