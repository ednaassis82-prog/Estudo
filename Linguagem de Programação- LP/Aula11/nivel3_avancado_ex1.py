import pyautogui
import time
import webbrowser

webbrowser.open("https://www.wikipedia.org")
time.sleep(5)

import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("https://www.wikipedia.org")
pyautogui.press("enter")