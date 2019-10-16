import PySimpleGUI as sg
from random import choice
from random import shuffle

sg.ChangeLookAndFeel('GreenTan')

# ------ Ustawienia kolumn ------
column1 = [[sg.Text('Zakres', background_color='lightblue', justification='center', size=(10, 1), text_color='red')],
           [sg.Text(('767456'), size=(8, 2)), sg.Spin(values=('1', '2', '3', '4', '5', '6', '7', '8', '9')
                                                      , initial_value='1', size=(5, 2), key='numbers')],
           [sg.Text(('ABficg'), size=(8, 2)), sg.Spin(values=('1', '2', '3', '4', '5', '6', '7', '8', '9')
                                                      , initial_value='1', size=(5, 2), key='letters')],
           [sg.Text(('!#$%&'), size=(8, 2)), sg.Spin(values=('1', '2', '3', '4', '5', '6', '7', '8', '9')
                                                     , initial_value='1', size=(5, 2), key='signs')]]
# ----- Wygląd programu ----
layout = [

    [sg.Text('Generator haseł', size=(30, 1), justification='center', font=("Helvetica", 15)
             , relief=sg.RELIEF_RIDGE, text_color="blue")],
    [sg.Frame('', [[sg.Column(column1, background_color='lightblue')]]),
     sg.Button('Generuj', size=(20, 1), key='generate')],
    [sg.Text('Wygenerowane hasło', size=(20, 1), auto_size_text=True, justification='right'),
     sg.InputText('', background_color='Red', key='Wygenerowane')],
    [sg.Text('Podaj nazwę', size=(20, 1), auto_size_text=False, justification='right'),
     sg.InputText('')],
    [sg.Save('Zapis'), sg.Button('Odczyt'), sg.Cancel('Wyjście')]]

window = sg.Window('pierwszy program', layout, default_element_size=(30, 1), grab_anywhere=False)

event, values = window.Read()


# ----- Losowe liczby i znaki -----
def generate(number, letter, sign):
    number = int(values['numbers'])
    x = 0
    letter = int(values['letters'])
    y = 0
    sign = int(values['signs'])
    z = 0
    password = []

    le = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
          'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r',
          't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
          'x', 'c', 'v', 'b', 'n', 'm']
    nu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    si = ['!', '@', '#', '%', '^', '&', '*']
    if event in ('generate'):

        while True:
            if y >= letter:
                break
            yy = choice(le)
            y += 1
            password += yy

        while True:
            if z >= sign:
                break
            zz = choice(si)
            z += 1
            password += zz
        while True:
            if x >= number:
                break
            xx = choice(nu)
            x += 1
            password += str(xx)

    shuffle(password)
    finish = ''.join(password)
    return finish


sg.InputText('Wygenerowane').update(44)
# print(finish)
generate(1, 1, 1)

# ------Zamkniecie programu-----
while True:
    if event in (None, 'Wyjście'):
        break
# '''Wygenerowane hasło ma wypisać w polu wygenerowane'''

# '''Zapis do bazy danych z nazwa'''
# elif event in ('Zapis'):
#     pass
#
# # '''odczyt do bazy danych'''
# elif event in ('Odczyt'):
#     pass
