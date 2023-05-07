import PySimpleGUI as sg
from cotacao import pegar_cotacoes
# Geralmente é importado como sg (sg é só um apelido para não ter que ficar escrevendo PySimpleGUI toda hora).

layout = [
    [sg.Text('Pegar Cotação de Moeda')],
    [sg.InputText(key='nome_cotacao')],
    [sg.Button('Pegar Cotação'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')]
]
# O PySimpleGUI considera a tela como uma coluna e nós devemos configurar as linhas. A variável layout vai receber 4 linhas (exemplo acima).
# O key é como um identificador.

janela = sg.Window("Sistema de Cotações", layout)
# Cria a janela, escolhe o título e qual o layout.

while True:
    evento, valores = janela.read()
    # Armazena os eventos (ações) e os valores () quando eles acontecem.
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        # Se o evento for igual a fechar a janela ou clicar no botão cancelar...
        break
    if evento == 'Pegar Cotação':
        # Se o evento for igual a clicar no botao pegar cotação...
        codigo_cotacao = valores['nome_cotacao']
        # codigo_cotacao vai receber o valor do input nome_cotacao que foi armazenado em valores.
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].update(f'A cotação do {codigo_cotacao} é de R${cotacao}')
        # O texto_cotacao que está vazio será atualizado para...
# O código da janela geralmente fica em um while True (Loop "infinito").

janela.close()
# Fecha a janela ao final do código.
