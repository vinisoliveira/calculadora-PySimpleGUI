from tkinter import font
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Menu

sg.theme('random')

#TAMANHO DA TELA
WIN_W = 30
WIN_H = 50

#MENU LAYOUT
menu_layout = [
    ['File', ['Save', 'Exit']],
    [ 'Tools', ['Waiting']],
    ['Help', ['About']]]

#ELEMENTOS DENTRO DA NOSSA TELA - ROW 1
layout = [
    [sg.Menu(menu_layout)],
    [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='-BOX-'),
     sg.Button('←', font=('Consolas', 20), key='-BACKARROW-'),
     sg.Button('C', font=('Consolas', 20), key='-CLEAR-')],
    #ROW 2
    [sg.Button('7', font=('Consolas', 20), key='-SEVEN-'),
     sg.Button('8', font=('Consolas', 20), key='-EIGHT-'),
     sg.Button('9', font=('Consolas', 20), key='-NINE-'),
     sg.Button('+', font=('Consolas', 20), key='-PLUS-'),
     sg.Button('*', font=('Consolas', 20), key='-TIMES-')],
    #ROW 3
    [sg.Button('4', font=('Consolas', 20), key='-FOUR-'),
     sg.Button('5', font=('Consolas', 20), key='-FIVE-'),
     sg.Button('6', font=('Consolas', 20), key='-SIX-'),
     sg.Button('-', font=('Consolas', 20), key='-MINUS-'),
     sg.Button('/', font=('Consolas', 20), key='-DIVIDED-')],
    #ROW 4
    [sg.Button('1', font=('Consolas', 20), key='-ONE-'),
     sg.Button('2', font=('Consolas', 20), key='-TWO-'),
     sg.Button('3', font=('Consolas', 20), key='-THREE-'),
     sg.Button('0', font=('Consolas', 20), key='-ZERO-'),
     sg.Button('=', font=('Consolas', 20), key='-RESULT-')]]

class App():
    def __init__(self):
        self.window = sg.Window('Calculator PyGUI', layout=layout, margins=(0,0),
        resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(1, 5):
            for button in layout[i]:
                button.expand(expand_x = True, expand_y = True)

    #FUNÇÕES DO MENU_LAYOUT
    def about(self):
        sg.popup('Calculator made using Python with PySimpleGui(https://pysimplegui.readthedocs.io/en/latest/)')

    #FUNÇÃO QUE MOSTRA O RESULTADO NO VISOR
    def resulter(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['-BOX-'])
        if self.oper == '-':
            return float(self.result) - float(self.values['-BOX-'])
        if self.oper == '*':
            return float(self.result) * float(self.values['-BOX-'])
        if self.oper == '/':
            return float(self.result) / float(self.values['-BOX-'])
    
    #FUNÇÃO QUE MANTÉM O PROGRAMA RODANDO
    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None, 'Exit', sg.WIN_CLOSED):
                break

            #CLICANDO EM ABOUT MENU, ATIVA ESSA FUNÇÃO
            if event in ('About'):
                self.about()

            if event in ('-ONE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='1')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '1')

            if event in ('-TWO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='2')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '2')

            if event in ('-THREE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='3')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '3')
                
            if event in ('-FOUR-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='4')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '4')

            if event in ('-FIVE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='5')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '5')

            if event in ('-SIX-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='6')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '6')

            if event in ('-SEVEN-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='7')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '7')

            if event in ('-EIGHT-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='8')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '8')

            if event in ('-NINE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='9')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '9')
            
            if event in ('-ZERO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='0')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '0')

            #DEFINIÇÕES DE APAGAR ÚLTIMO DIGITO E LIMPAR TUDO
            if event in ('-CLEAR-'):
                self.result = 0
                self.window['-BOX-'].update(value= self.result)

            if event in ('-BACKARROW-'):
                self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])

            #FUNÇÕES +, -, *, /
            if event in ('-PLUS-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value = '')

            if event in ('-MINUS-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '-'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value = '')

            if event in ('-TIMES-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '*'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value = '')

            if event in ('-DIVIDED-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '/'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value = '')

            if event in('-RESULT-'):
                self.result = self.resulter()
                self.window['-BOX-'].update(value= self.result)
                self.result = 0
                self.oper = ''

Sapp = App()
Sapp.start()