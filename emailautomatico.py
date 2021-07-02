# automatização para mandar e-mail automático!

import pyautogui
import time
import pyperclip

pyautogui.alert("Automação irá iniciar")
# abrir gmail
pyautogui.hotkey('win')
pyautogui.write("chrome")
pyautogui.press('enter')
time.sleep(4)
pyautogui.write("gmail.com")
pyautogui.press('enter')
time.sleep(8)

# clicar em escrever email
pyautogui.click(62, 198)
time.sleep(10)

# preencher informações do e-mail
pyautogui.write('xxxxxxxxx@gmail.com; yyyyyy@hotmail.com') #EDITAR EMAILS
pyautogui.press('tab')  # aqui seleciona o email
pyautogui.press('tab')  # parte para o campo de assunto
assunto = "XXXXXXXXXXX" #EDITAR ASSUNTO
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", 'v')
pyautogui.press("tab")
texto = """
XXXXXXXXXXXXXXXXXXXXXXXXX""" #EDITAR TEXTO DO E-AMIL
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", 'v')

# enviar o email
pyautogui.hotkey('ctrl', 'enter')

# fechar programação
pyautogui.alert("Fim da automação. Seu computador já voltou a ser seu rs")