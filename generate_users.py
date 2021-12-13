import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os

root = tk.Tk()
root.title('Ezio Killers')
root.geometry('620x200')

# define columns
columns = ('SESSIONNAME', 'USERNAME', 'ID','STATE','TYPE','DEVICE')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('SESSIONNAME', text='Nome da sessão')
tree.heading('USERNAME', text='Username')
tree.heading('ID', text='ID')
tree.heading('STATE', text='Estado')
tree.heading('TYPE', text='Tipo')
tree.heading('DEVICE', text='Dispositivo')

# generate sample data
contacts = []
#for n in range(1, 100):
contacts.append(os.system('qwinsta /server:RDESK02.unifeso.lan'))

print('teste',contacts)
# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()