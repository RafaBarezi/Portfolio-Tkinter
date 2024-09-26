print("Propriedade anchor:")

# Vincula um sentido a um componente. A região da extremidade fica reservada a esse componete

from tkinter import *

janela = Tk()

# A propriedade anchor() define os lados como uma bússula - Norte, Sul, Leste, Oeste, Nordeste, Sudeste, Sudoeste, Noroeste e Centro (N, S, E, W, NE, SE, SW, NW). Ela coloca o componente na posição máxima do lado definido

lb1 = Label(janela,text="SIDE1",bg="white")
lb2 = Label(janela,text="SIDE2",bg="red")
lb3 = Label(janela,text="ANCHOR1",bg="white")
lb4 = Label(janela,text="ANCHOR2",bg="red")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(side=LEFT, anchor=NW)
lb4.pack(side=LEFT, anchor=SW)

janela["bg"] = "black"
janela.geometry("1200x700+0+0")
janela.mainloop()