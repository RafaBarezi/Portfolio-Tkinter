print("Propriedade rowspan e columnspan:")

# Mesclagem de guias

from tkinter import *

janela = Tk()

lb1 = Label(janela, bg="lightgreen", width=15, height=7)
lb2 = Label(janela, bg="black", width=15, height=7)
lb3 = Label(janela, bg="red", width=15, height=7)
lb4 = Label(janela, bg="green", width=15, height=7)
lb5 = Label(janela, bg="darkblue", height=7)
lb6 = Label(janela, bg="yellow", width=15)
lb7 = Label(janela, bg="pink", width=15, height=7)

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=0, column=1)
lb4.grid(row=1, column=1)
# Mesclaremos 2 colunas:
lb5.grid(row=2, column=0, columnspan=2, sticky= W + E)
lb6.grid(row=0, column=2, rowspan=2, sticky= N + S)
lb7.grid(row=2, column=2)

janela.geometry("600x600+0+0")
janela.mainloop()