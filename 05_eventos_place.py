print("\nEventos place:\n")

from tkinter import *
from functools import partial

# Veremos como trabalhar com uma função genérica em vários botoes

# def button_click1():
#     print("button_click 1 foi clicado e aparece no prompt")

# def button_click2():
#     print("button_click 2 foi clicado e aparece no prompt")

# # Estamos distinguindo o botão clicado, então invocamos 2 funções com parâmetros diferentes

# janela = Tk()
# janela.geometry("1200x700+0+0")
# bt1 = Button(janela, width=20, text="Botão 1", command=button_click1)

# bt1.place(x=100, y=100)
# bt2 = Button(janela, width=20, text="Botão 2", command=button_click2)
# bt2.place(x=100, y=200)

# janela.mainloop()

# Ou podemos definir assim: 

def bt_click(botao):
    print(botao["text"],"\n")  # imprimindo o texto de cada botão

janela = Tk()

bt1 = Button(janela, width=20, text="botão 1")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=600, y=200)
bt2 = Button(janela, width=20, text="botão 2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=600, y=300)

janela.geometry("1200x700+0+0")
janela.mainloop()