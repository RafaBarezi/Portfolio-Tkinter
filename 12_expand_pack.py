print("\nPropriedade expand:\n")

# Faz com que todos os widgets tenham o mesmo tamanho em um determinado sentido

from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Linha 1", bg="white") 
lb2 = Label(janela, text="Linha 2", bg="yellow") 
lb3 = Label(janela, text="Linha 3", bg="blue") 
lb4 = Label(janela, text="Linha 4", bg="yellow") 

lb1.pack(side=TOP, fill=BOTH, expand=1) # Fill vai preencher em ambas as direções quando se usa o BOTH
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry("1200x700+0+0")
janela.mainloop()