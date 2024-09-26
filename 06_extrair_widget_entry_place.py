print("\nExtraindo valores do widget entry:\n")

from tkinter import *

def bt_onclick():
    print(edit.get())

janela = Tk()
janela.title("Janela principal")
janela["bg"] = "dark green"

edit = Entry(janela, width=16, background="grey")
edit.place(x=610, y=200)

bt = Button(janela, width=16, text="Texto escolhido", command=bt_onclick)
bt.place(x=600, y=300)

lb = Label(janela, text="Este é o label")
lb.place(x=630, y=400)

janela.geometry("1200x700+0+0")
janela.mainloop()
