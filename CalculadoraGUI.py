#interface gráfica

import PySimpleGUI as psg

import calc2
from calc2 import div

layout =     [
                 [psg.Text('Informe o Primeiro Número: '), psg.InputText(key='num1')],
                 [psg.Text('Informe o Segundo Número: '), psg.InputText(key='num2')],
                 [psg.Text(' >>>>>> '), psg.Text('', key='total'), psg.Text(' <<<<<< ')],
                 [psg.Button('Calcular'), psg.Button('Limpar')],
             ]

janela = psg.Window('Calculadora Simples', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['num1'].update('')
        janela['num2'].update('')
        janela['total'].update('')
        janela['num1'].set_focus()
    else:
        num1 = float(valores['num1'])
        num2 = float(valores['num2'])
        janela ['total'].update(calc2.div(num1, num2))

janela.close()