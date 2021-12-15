import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os

root = tk.Tk()
root.title('Ezio Killers')
root.geometry('970x300')

# define columns
columns = ('SESSIONNAME', 'USERNAME', 'ID','STATE')

tree = ttk.Treeview(root,height=10,columns=columns, show='headings')

# define headings
tree.heading('SESSIONNAME', text='Nome da sessão')
tree.heading('USERNAME', text='Username')
tree.heading('ID', text='ID')
tree.heading('STATE', text='Estado')
#tree.heading('TYPE', text='Tipo')
#tree.heading('DEVICE', text='Dispositivo')

# generate sample data
#contacts = []
#for n in range(1, 100):
#lista = os.popen('qwinsta /server:RDESK02.unifeso.lan')
teste = 'quser'
contacts = os.popen(teste+" /server:10.1.0.29").read()
contacts = contacts.split()
print(contacts)
tree.insert('', tk.END, values=(contacts[9],contacts[8],contacts[10],contacts[11]))




# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=(contacts))


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        print(contacts[10])

txt_usuario = tk.Text(root, height=1.5, width=100)
txt_usuario.grid(column = 0, row = 0,padx=10,pady=10)
btn_buscar_usuario = tk.Button(root,width=15,text="Buscar")
btn_buscar_usuario.grid(column=2,row=0, sticky='nsew',padx=2,pady=3)


tree.bind('<<TreeviewSelect>>', item_selected)
tree.grid(row=1, column=0, sticky='nsew',padx=10,pady=0)

btn_finalizar_usuario = tk.Button(root,width=15,text='Finalizar')
btn_finalizar_usuario.grid(column=2,row=1,padx=2,pady=3)

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='nsew',pady=0,padx=0)

# run the app
root.mainloop()