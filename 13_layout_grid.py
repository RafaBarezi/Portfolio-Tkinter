print("\nGerenciador de layout grid\n") 

# Este é o terceiro gerenciador (temos o place, pack e o grid), sendo o grid é o mais utilizado.

# Atenção pois ele é sempre exibido sempre na posição mais próxima do topo e da esquerda possível 

# row significa linha, column significa coluna

from tkinter import*

janela = Tk()

# Label será exibido na linha 1, coluna 1:
lb1 = Label(janela, text= "Label1")
lb2 = Label(janela, text= "Label2")
lb1.grid(row=1, column=1) 
# Mesmo com a distância da label anterior o espaço é desconsiderado
lb2.grid(row=1000, column=2000) 

janela.geometry("1200x700+0+0")
janela.mainloop()