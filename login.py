#!/usr/bin/env python
import PySimpleGUI as sg
import hashlib
from sys import exit as exit

# Use this GUI to get your password's hash code
def login():
    layout = [[sg.Text('Podaj imię i hasło', size=(30, 1), justification='center', font=("Helvetica", 15)
             , relief=sg.RELIEF_RIDGE, text_color="blue")],
              [sg.Text('Imię', size=(10, 1), auto_size_text=True, justification='left'),
               sg.InputText('', size=(20,1), background_color='lightblue', key='name')],
              [sg.Text('Hasło', size=(10, 1), auto_size_text=True, justification='left'),
               sg.Input('', size=(20,1), background_color='lightblue', key='password')],
              [sg.Ok('Zapis'), sg.Cancel('Wyjście')]
              ]

    window = sg.Window('Logowanie', auto_size_text=False, default_element_size=(10,1),
                       text_justification='r', return_keyboard_events=True, grab_anywhere=False).Layout(layout)

    while True:
        event, values = window.Read()
        if event is None:
              exit(69)

        password = values['password']
        try:
            password_utf = password.encode('utf-8')
            sha1hash = hashlib.sha1()
            sha1hash.update(password_utf)
            password_hash = sha1hash.hexdigest()
            window.FindElement('hash').Update(password_hash)
        except:
            pass
login()
# ----------------------------- Paste this code into your program / script -----------------------------
# determine if a password matches the secret password by comparing SHA1 hash codes
def PasswordMatches(password, hash):
    password_utf = password.encode('utf-8')
    sha1hash = hashlib.sha1()
    sha1hash.update(password_utf)
    password_hash = sha1hash.hexdigest()
    return password_hash == hash


login_password_hash = 'e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4'
password = sg.PopupGetText('Password', password_char='*')
if password == 'gui':                # Remove when pasting into your program            # Remove when pasting into your program
    login()
    exit(69)                         # Remove when pasting into your program
if PasswordMatches(password, login_password_hash):
    print('Login SUCCESSFUL')
else:
    print('Login FAILED!!')