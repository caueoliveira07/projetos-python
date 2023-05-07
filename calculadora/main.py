# Importando tkinter
from tkinter import *
from tkinter import ttk
# ttk é uma parte mais avançada do tkinter

# Definindo as cores
cor1 = "#181f1e" # Preto
cor2 = "#feffff" # Branco
cor3 = "#5681c4" # Azul
cor4 = "#eceff1" # Cinza

# Criando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.minsize(235, 310)
janela.maxsize(235, 310)
janela.config(bg=cor1)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor4)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

# Criando funções
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    #Passando o valor para tela
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))
    
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Criando label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 17'), bg=cor4, fg=cor1)
app_label.place(x=0, y=0)

# Criando botões
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor3, fg=cor2, bd=2, highlightcolor=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor3, fg=cor2, bd=2, highlightcolor=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor3, fg=cor2, bd=2, highlightcolor=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor3, fg=cor2, bd=2, highlightcolor=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor1, fg=cor2, bd=2, highlightcolor=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor3, bd=2, highlightcolor=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

janela.mainloop()

# O método .title() é usado para definir o título da janela da GUI (Graphical User Interface).

# O método .geometry() é usado para definir as dimensões e a posição da janela da GUI.

# O método .config() é usado para personalizar a aparência e o comportamento dos widgets de acordo com as necessidades da aplicação. Ele pode ser usado para definir uma ampla variedade de opções de configuração para cada widget, permitindo que o programador crie uma interface de usuário personalizada e atraente.

# O Frame() é semelhante a uma janela, mas não possui barra de título e é usada principalmente como um recipiente para agrupar outros widgets relacionados. Ele pode ser usado para organizar a interface gráfica em áreas separadas, com cada área contendo widgets relacionados que executam funções semelhantes.

# A função eval() da linguagem Python permite avaliar e executar uma expressão ou código Python passado como uma string. Ela retorna o resultado da expressão avaliada como um objeto Python.

# O método .place() é útil para criar interfaces de usuário personalizadas com layouts precisos e exatos. No entanto, deve-se ter cuidado ao usar este método, pois se o tamanho da janela for alterado ou se outros widgets forem adicionados ou removidos da janela, os widgets posicionados com .place() podem ficar desalinhados ou podem ficar fora da janela. Além disso, não é recomendado usar o método .place() em conjunto com o método .pack() ou .grid(), pois pode levar a resultados inesperados.

# O Label() é um widget que permite exibir texto ou imagem na interface gráfica do usuário. Ele é usado principalmente para exibir informações, como rótulos, títulos ou mensagens, na janela de interface gráfica do usuário. 

# Os botões criados com o Button() são uma forma comum de permitir que o usuário interaja com a aplicação, clicando no botão para realizar uma ação específica. Quando o botão é clicado, ele pode executar uma função, executar uma ação pré-definida ou exibir uma mensagem.

# lambda é uma palavra-chave da linguagem Python que é usada para definir funções anônimas. Essas funções são chamadas de anônimas porque não têm um nome definido como as funções normais definidas com a palavra-chave def. As funções lambda são usadas para criar pequenas funções que são usadas apenas uma vez e que não precisam de um nome.

# O método .mainloop() é responsável por executar o loop principal da interface gráfica de usuário, permitindo que a janela da GUI receba e responda a eventos enquanto permanece aberta e em execução.
