import pyautogui
import time

pyautogui.hotkey("win","r")
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")


time.sleep(2)
pyautogui.write("Linha 1 : Automatizando com PyAutoGui\n")
pyautogui.write("Linha 2 : Criando scripts incriveis\n")
pyautogui.write("linha 3 : Salvando anotações automaticamente\n")

#salvar arquivo
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.write("anotacao.txt")
pyautogui.press("enter")