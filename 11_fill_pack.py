print("\nPropriedade fill:\n")

# Ele ocupa a área no sentido indicado

from tkinter import *

janela = Tk()

lb1 = Label(janela, text ="horizontal", bg ="white")
lb1.pack(side=TOP, fill=X) # Esse X se refere ao plano cartesiano
lb2 = Label(janela, text ="", bg ="black")
lb2.pack(side=LEFT, fill=Y) # Esse Y se refere ao plano cartesiano
lb3 = Label(janela, text ="", bg ="black")
lb3.pack(side=RIGHT, fill=Y) 

janela.geometry("1200x700+0+0")
janela.mainloop()