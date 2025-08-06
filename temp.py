import pyautogui
import time

# pixels_per_cm = 40 # Примерное количество пикселей в 1 см

while True:
    x, y = pyautogui.position()
    # Двигаем мышь вправо
    # pyautogui.moveTo(x + pixels_per_cm, y, duration=0.2)
    # time.sleep(0.2)

    # Клик мышью
    pyautogui.click()
    time.sleep(240)