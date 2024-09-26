("\nPropriedade side:\n")

# Ela vincula uma propriedade a um componente

 # side / botton (alinhados na horizontal) left / right (alinhado na vertical - A largura determina o espaço)

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="RIGHT",bg="yellow")
lb2 = Label(janela,text="BOTTOM",bg="red")
lb3 = Label(janela,text="LEFT",bg="blue")
lb4 = Label(janela,text="TOP",bg="green")

lb1.pack(side=RIGHT)
lb2.pack(side=BOTTOM)
lb3.pack(side=LEFT)
lb4.pack(side=TOP)

janela["bg"] = "black"
janela.geometry("1200x700+0+0")
janela.mainloop()