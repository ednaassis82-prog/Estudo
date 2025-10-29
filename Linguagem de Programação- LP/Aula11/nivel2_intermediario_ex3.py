import pyautogui
import time
time.sleep(5)


lado = 200
espaco = 20

for i in range(3):
    pyautogui.dragRel(lado, 0, duration=0.5)
    pyautogui.dragRel(0,lado,duration=0.5)
    pyautogui.dragRel(-lado,0,duration=0.5)
    pyautogui.dragRel(0,-lado,duration=0.5)
    pyautogui.moveReal( lado + espaco, 0, duration=0.5)
                       
