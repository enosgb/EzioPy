from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter as tk
import os


window = Tk()
window.resizable(height=None,width=None)
window.title('Ezio Killer')





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

# add a scrollbar
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=2, column=1, sticky='nsew',pady=0,padx=0)

#FUNCTIONS

def busca_usuario(usuario):
    cont = 0
    username = 9
    sessionname = 8
    id = 10
    state = 11
    if(os.system('quser '+usuario+' /server:RDESK02.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:RDESK02.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdsh1.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdsh1.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdsh2.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdsh2.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdsh3.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdsh3.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdsh4.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdsh4.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdsh5.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdsh5.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdsh6.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdsh6.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:SH1-HCTCO'))==0:
        contacts = os.popen('quser '+usuario+' /server:SH1-HCTCO').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:SH2-HCTCO'))==0:
        contacts = os.popen('quser '+usuario+' /server:SH2-HCTCO').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:SH3-HCTCO'))==0:
        contacts = os.popen('quser '+usuario+' /server:SH3-HCTCO').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdesk02.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdesk02.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    if(os.system('quser '+usuario+' /server:rdeskamb.unifeso.lan'))==0:
        contacts = os.popen('quser '+usuario+' /server:rdeskamb.unifeso.lan').read()
        contacts = contacts.split()
        for contact in contacts:
            username = 9+cont
            sessionname = 8+cont
            id = 10+cont
            state = 11+cont
            tree.insert('',tk.END, values=(contacts[username],contacts[sessionname],contacts[id],contacts[state]))
            cont = cont + 7
    else:
        print('usuario nao encontrado')


def item_selected(event):
    for selected_item in tree.selection():
       item = tree.item(selected_item)
       #print(item['values'][2])
    return (item['values'][2])
  

def return_usuario(event):
    user = txt_usuario.get("1.0","end")
    txt_usuario.delete("1.0","end")
    return busca_usuario(user.rstrip('\n'))

def finalizar_usuario(event):
    sessao = (item_selected(tree.bind('<<TreeviewSelect>>', item_selected)))
    sessao = str(sessao)
    os.system("rwinsta /server:RDESK02.unifeso.lan "+sessao)
    os.system("rwinsta /server:rdsh1.unifeso.lan "+sessao)
    os.system("rwinsta /server:rdsh2.unifeso.lan "+sessao)
    os.system("rwinsta /server:rdsh3.unifeso.lan "+sessao)
    os.system("rwinsta /server:rdsh4.unifeso.lan "+sessao)
    os.system("rwinsta /server:rdsh5.unifeso.lan "+sessao)
    os.system("rwinsta /server:rdsh6.unifeso.lan "+sessao)
    os.system("rwinsta /server:SH1-HCTCO "+sessao)
    os.system("rwinsta /server:SH2-HCTCO "+sessao)
    os.system("rwinsta /server:SH3-HCTCO "+sessao)
    print('sessão finalizada')

#bind select item treeview
tree.bind('<<TreeviewSelect>>', item_selected)

#define txt box
txt_usuario = tk.Text(window,height=1,width=50)
txt_usuario.grid(row=1,column=0,padx=10,pady=10)
window.bind('<Return>', return_usuario)

#define buttons
btn_buscar = ttk.Button(window,text='Buscar')
btn_buscar.bind('<Button-1>', return_usuario)
btn_buscar.grid(row=1,column=4,padx=5,pady=15)

btn_finalizar = ttk.Button(window,text='Finalizar')
btn_finalizar.bind('<Button-1>', finalizar_usuario)
btn_finalizar.grid(row=3,column=4,padx=10,pady=10)

window.mainloop()