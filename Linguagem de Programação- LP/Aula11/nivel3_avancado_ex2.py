import pyautogui
import time

pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("you tube")
pyautogui.press("enter")


time.sleep(5)

pyautogui.click(x=1270, y=155)

pyautogui.write("Musica relaxante", interval= 0.1)
pyautogui.press("enter")