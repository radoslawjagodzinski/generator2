#!/usr/bin/env python
import PySimpleGUI as sg


def login():
    layout = [[sg.Text('Podaj imię i hasło', size=(30, 1), justification='center', font=("Helvetica", 15)
                       , relief=sg.RELIEF_RIDGE, text_color="blue")],
              [sg.Text('Imię', size=(10, 1), auto_size_text=True, justification='left'),
               sg.InputText('', size=(20, 1), background_color='lightblue', key='name')],
              [sg.Text('Hasło', size=(10, 1), auto_size_text=True, justification='left'),
               sg.Input('', size=(20, 1), background_color='lightblue', key='password')],
              [sg.Ok('Zapis'), sg.Cancel('Wyjście', key='wyjscie')]
              ]

    window = sg.Window('Logowanie', auto_size_text=False, default_element_size=(10, 1),
                       text_justification='r', return_keyboard_events=True, grab_anywhere=False).Layout(layout)

    event, values = window.Read()
    if event is (None, 'Wyjscie'):
        window.Close()


login()
