import PySimpleGUI as sg
from random import choice
from random import shuffle
import  string


def window():

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
    [sg.Text('Podaj nazwę/klucz', size=(20, 1), auto_size_text=False, justification='right'),
     sg.InputText('')],
    [sg.Save('Zapis'), sg.Button('Odczyt'), sg.Cancel('Wyjście')]]

    window = sg.Window('pierwszy program', layout, default_element_size=(30, 1), grab_anywhere=False)



    while True:
        event, values = window.Read()
        if event in (None, 'Wyjście'):
            break
# ----- Losowe liczby i znaki -----

        if event in 'generate':
            number = int(values['numbers'])
            x = 0
            letter = int(values['letters'])
            y = 0
            sign = int(values['signs'])
            z = 0
            password = []
            si = ['!', '@', '#', '%', '^', '&', '*']

            while True:
                if y >= letter:
                    break
                yy = choice(string.ascii_letters)
                y += 1
                password += yy

                if z >= sign:
                    break
                zz = choice(si)
                z += 1
                password += zz

                if x >= number:
                    break
                xx = choice(string.digits)
                x += 1
                password += str(xx)

            shuffle(password)
            finish = ''.join(password)
            print(finish)

            window.Element('Wygenerowane').Update(finish)

    window.Close()


    while True:
        if event in (None, 'Wyjście'):
            break

window()

