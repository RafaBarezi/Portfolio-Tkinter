print("Propriedade sticky:")

# Essa é uma propriedade é como se fosse uma rosa dos ventos. Podemos colocar o componente em qualquer sentido de uma célula:

from tkinter import* 

janela = Tk()

lb1 = Label (janela, text="Espaço", width="15", height=3, bg= "blue")
lbHorizontal = Label(janela, text="Horizontal", bg ="yellow")
lbvertical = Label(janela, text="vertical", bg="green")

lb1.grid(row=0, column=0)
lbHorizontal.grid(row=1, column=0, sticky=E)
lbvertical.grid(row=2, column=0, sticky=SW)


janela.geometry("200x100+0+0")
janela.mainloop()