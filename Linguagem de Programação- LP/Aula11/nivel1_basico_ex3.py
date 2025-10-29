import pyautogui
import time

print("Posicione o mouse no local desejado! Você tem tres segundos...")
time.sleep(3)
x,y= pyautogui.position()
pyautogui.click(x,y)
print(f"Clique realizado em: x={x},y={y}")