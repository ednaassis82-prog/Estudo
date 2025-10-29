import pyautogui
import time

pyautogui.PAUSE=0.6


pyautogui.press("win")
pyautogui.write("Bloco de notas")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("Automatizando com o PyAutoGui e divertido!",interval=0.2)
time.sleep(2)


