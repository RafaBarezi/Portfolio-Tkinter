print("\nBotões e labels:\n")

from tkinter import *

def bt_click(): 
    print("bt_click")
    lb["text"] = "Você clicou no botão!"    
    lb.place(x=600, y=400)

janela = Tk()
janela.title("Janela principal")
janela["bg"] = "dark green"
janela.geometry("1200x700+0+0")

bt = Button(janela, width = 20, text= "Clique neste botão", command= bt_click)
bt.place(x=580, y=200)

lb = Label(janela, text= "Label")
lb.place(x=650, y=300)

janela.mainloop()