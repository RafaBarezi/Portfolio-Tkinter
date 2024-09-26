print("\nHello world tkinter:\n")

from tkinter import * 

janela = Tk() 
janela.title("Janela principal")

Label(janela, text = "Hello world!").pack() 
janela.geometry("600x500+0+0")

janela.mainloop() 