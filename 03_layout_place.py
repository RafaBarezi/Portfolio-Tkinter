print("\nGerenciador de layout place:\n")

from tkinter import *

janela = Tk() 

Lb = Label(janela, text = "conteúdo da janela")
Lb.place(x=600, y=300) 

janela.geometry("1200x520+0+0")
janela.mainloop()