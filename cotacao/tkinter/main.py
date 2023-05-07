import requests
from tkinter import *
# O * é para pegar tudo da biblioteca tkinter (biblioteca é um pacote de códigos que alguém construiu). Ao importar dessa maneira nós podemos utilizar apenas Tk quando formos usar a biblioteca tkinter.

def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}
    '''

    texto_cotacoes['text'] = texto# O parâmetro text de texto_cotacoes vai receber a variável texto.

# Sempre que for usar o tkinter, nós começamos o código com o janela = Tk() e terminamos com o janela.mainloop(). O nome não precisa ser necessariamente "janela".
janela = Tk()# Cria a janela inicial.
janela.title('Cotação Atual das Moedas')# Adiciona um título a janela.
# janela.geometry('400x400')# Aumenta o tamanho da janela.
texto_orientacao = Label(janela, text='Clique no botão para exibir a cotação das moedas') # Label é um campo de texto. O primeiro parâmetro é a janela que ele fará parte. O segundo é o texto desejado.
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)# O grid configura a linha e a coluna que o texto vai estar. O padx e pady configura o padding (espaço) no eixo x e no eixo y.
botao = Button(janela, text='Buscar cotações Dólar/Euro/BTC', command=pegar_cotacoes)# Os dois primeiros parâmetros são os mesmos do label, já o command é qual função (sem parênteses) esse botão irá executar.
botao.grid(column=0, row=1, padx=10, pady=10)
texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()
# Faz com que a janela continue sendo exibida.
