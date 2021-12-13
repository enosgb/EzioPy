from tkinter import *
#from conversor_caracteres import Conversor

__version__ = '1.0.0'

#xbm, ppm, pgm, gif
#Checkbutton
#partial
#insert
#delete

class Email(object):
  def __init__(self,tk):
    self.tk = tk
    self.tk.title('Gerador de Email GUI')

    self.font = ('Verdana', '20', 'bold')
    self.font2 = ('Verdana', '14', 'bold')
    mainFont=('Verdana','15','bold')

    self.msg=Label(self.tk,text='Por favor, informe uma Versão!',font=mainFont)
    self.msg.grid(row=0, column=1, columnspan=3)

    Label(self.tk,text='Versão:', font=mainFont).grid(row=1, column=0,sticky=W, pady=16)
    self.inputVersao=Entry(self.tk, width=20, fg='darkgray',font=mainFont)
    self.inputVersao.grid(row=1, column=1, sticky=E+W, pady=3, columnspan=3)

    self.criarVersao=Button(self.tk, width=8,text='+', font=mainFont, command=self.criarVersao)
    self.criarVersao.grid(row=1, column=4, padx=15, pady=3)

    Label(self.tk,text='Tópico:', font=mainFont).grid(row=2, column=0, sticky=W, pady=16)
    self.inputTopico=Entry(self.tk, width=30, fg='darkgray')
    self.inputTopico.grid(row=2,column=1, sticky=E+W, pady=3, columnspan=3)
    self.inputTopico.config(state='readonly')

    self.criarTopico=Button(self.tk, width=8,text='+', font=mainFont, command=self.criarTopico)
    self.criarTopico.grid(row=2, column=4, padx=15, pady=3)

    Label(self.tk,text='Subtópico:', font=mainFont).grid(row=3, column=0, sticky=W, pady=16)
    self.inputSubtopico=Entry(self.tk, width=40, fg='darkgray',font=mainFont)
    self.inputSubtopico.grid(row=3,column=1, sticky=E+W, pady=3, columnspan=3)
    self.inputSubtopico.config(state='readonly')

    self.criarSubTopico=Button(self.tk, width=8,text='+',font=mainFont,command=self.criarSubTopico)
    self.criarSubTopico.grid(row=3, column=4, padx=15, pady=3)

    Label(self.tk,text='Descrição:', font=mainFont).grid(row=4, column=0, sticky=W, pady=16)
    self.inputDescricao=Entry(self.tk, width=40, fg='darkgray',font=mainFont)
    self.inputDescricao.grid(row=4,column=1, sticky=E+W, pady=3, columnspan=3)
    self.inputDescricao.config(state='readonly')

    self.criarDescricao=Button(self.tk, width=8,text='+',font=mainFont, command=self.criarDescricao)
    self.criarDescricao.grid(row=4, column=4, padx=15, pady=3)

    self.preview=Button(self.tk, width=10,text='Preview Email', bg="gray", fg="white",font=mainFont)
    self.preview.grid(row=5, column=0, padx=0, pady=3, ipadx =20,sticky=SW)

    self.alterar=Button(self.tk, width=10,text='Alterar Dados', bg="gray", fg="white",font=mainFont)
    self.alterar.grid(row=5, column=1, padx=0, pady=3, ipadx =20, sticky=SW)

    self.gerarEmail=Button(self.tk, width=10, command=self.gerarEmail, text='Gerar Email',bg="green", fg="white", font=mainFont)
    self.gerarEmail.grid(row=5, column=2, padx=(20,0), pady=3, ipadx =20, sticky=SW)

    self.resetarEmail=Button(self.tk, width=10,command=self.resetarEmail, text='Resetar Email', bg="red", fg="white", font=mainFont)
    self.resetarEmail.grid(row=5, column=3, padx=0, pady=3, ipadx=20, sticky=SW)

  def criarVersao(self):
    print("entrei")

  def gerarEmail(self):
    pass

  def resetarEmail():
    pass

  def criarHeader(self):
    pass

  def criarFooter(self):
    pass

  def criarTopico(self):
    pass

  def criarSubTopico(self):
    pass

  def criarDescricao(self):
    pass

i = Tk()
Email(i)
i.title('Gerador de Email')
global email 
email = []
global preview 
preview = []
global conv 
#conv = Conversor
global arquivo
global versaoDig
versaoDig = False   
i.mainloop()