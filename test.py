import random
import keyboard
import time
import pyautogui
Upgrade1 = 0
Upgrade2 = 0

def Upgrade01():
    
    while not Upgrade1 == 11:
        try:
            loc = pyautogui.locateCenterOnScreen('Upgrade1.png',confidence =1)
            pyautogui.moveTo(loc)
            pyautogui.mouseDown()
            time.sleep(0.000001)
            pyautogui.mouseUp()
            Upgrade1 == 0 + 1
            return True
        except Exception as e:
            return False
        
def Upgrade02():
    
    while not Upgrade2 == 11:
        try:
            loc = pyautogui.locateCenterOnScreen('Upgrade2.png',confidence =0.98)
            pyautogui.moveTo(loc)
            pyautogui.mouseDown()
            time.sleep(0.000001)
            pyautogui.mouseUp()
            Upgrade1 == 0 + 1
            return True
        except Exception as e:
            return False
        
while True:
    Upgrade01()