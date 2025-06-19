import random
import keyboard
import time
import pyautogui 


def auto_clicker(clicks, interval):
    
    for i in range(clicks):
        pyautogui.click()
        time.sleep(interval)
while True:
    auto_clicker(0, 1)