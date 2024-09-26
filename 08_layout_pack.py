print("\nGerenciador de layout pack:\n")

# Serve para empacotar os widget na horizontal ou vertical

# Side > lado em que deseja empacotar os componentes (top, right, bottom, left)

from tkinter import *

janela = Tk()

# agora vamos criar quatro labels e atribuir as instâncias de cada um á lb1, lb2. lb3, lb4:

lb1 = Label(janela, text = "Label 1", bg = "green")
lb2 = Label(janela, text = "Label 2", bg = "red")
lb3 = Label(janela, text = "Label 3", bg = "yellow")
lb4 = Label(janela, text = "Label 4", bg = "blue")

# Para definir o gerenciador de layout pack: 

# O que define a ordem é a ordem que definimos o gerenciador 

lb3.pack()
lb2.pack(side=RIGHT)
lb1.pack(side=LEFT)
lb4.pack(side=BOTTOM)

# Quando não definimos a propriedade defaulté a top

janela.geometry("1200x700+0+0")
janela.mainloop()