print("\ntela de login e senha grid:\n")

from tkinter import *

janela = Tk()

lb1 = Label(janela, text="login: ")
lb2 = Label(janela, text="senha: ")
edit1 = Entry(janela,)
# Usamos a propriedade show para mostrar * na senha:
edit2 = Entry(janela, show="*")
bt1 = Button(janela, text="Confirmar")

lb1.grid(row = 0, column= 0)
lb2.grid(row = 1, column= 0)
edit1.grid(row = 0, column= 1)
edit2.grid(row = 1, column= 1)
bt1.grid(row=2, column=1)

janela.geometry("")
janela.mainloop()