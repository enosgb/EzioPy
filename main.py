from tkinter import *
import os

#janela.geometry(“400×400”)
janela = Tk()
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

def pegar_cotacoes():
   texto.grid(column=0, row=2, padx=10, pady=10)

texto=Tk.Text(janela, height=10)
texto.pack()
#botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
#botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()

