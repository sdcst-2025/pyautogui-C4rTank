import random
import keyboard
import time
import pyautogui
import os

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)
Attack1 = True

def start():
    os.startfile(('H:\Profile\Desktop\Computers 12\pyautogui-C4rTank\mike-game.html'))
    try:
        x, y = pyautogui.locateCenterOnScreen('Clicky This')
        pyautogui.click(x, y)
    except:
        pass


def StartMenu01():
    try:
        location = pyautogui.locateOnScreen('Menu01.png', confidence=0.2)
        pyautogui.hotkey('down',interval=0.1)
        pyautogui.hotkey('down',interval=0.1)
        pyautogui.hotkey('z',interval=0.1)
        pyautogui.hotkey('z',interval=0.1)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.5)

    
def StartMenu02():
    try:
        location = pyautogui.locateOnScreen('Menu02.png', confidence=0.5)
        pyautogui.hotkey('left',interval=0.1)
        pyautogui.hotkey('z',interval=0.1)
        pyautogui.hotkey('z',interval=0.1)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.5)

def StartingBattle():
    try:
        location = pyautogui.locateOnScreen('Starting_Battle.png', confidence=0.25)
        pyautogui.hotkey('left',interval=0.1)
        pyautogui.hotkey('z',interval=0.1)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.5)


def Attack01():
    try:
        location = pyautogui.locateOnScreen('dialog 1.png', confidence=0.5)
        Attack1 == True
        while Attack1 == True:
            pyautogui.hotkey('z',interval=0.1)
            pyautogui.hotkey('z',interval=0.1)
            pyautogui.hotkey('z',interval=0.1)
            pyautogui.hotkey('z',interval=0.1)
            pyautogui.hotkey('z',interval=0.1)

            pyautogui.keyDown('up')
            time.sleep(0.5)
            pyautogui.keyUp('up')
            pyautogui.hotkey('z',interval=0.1)
            
            time.sleep(0.5)
            pyautogui.keyDown('up')
            time.sleep(0.5)
            pyautogui.keyUp('up')
            pyautogui.hotkey('z',interval=0.1)

            time.sleep(0.5)
            pyautogui.keyDown('up')
            time.sleep(0.5)
            pyautogui.keyUp('up')
            pyautogui.hotkey('z',interval=0.1)

            time.sleep(0.5)
            pyautogui.keyDown('up')
            time.sleep(0.5)
            pyautogui.keyUp('up')
            pyautogui.hotkey('z',interval=0.1)

            print(X)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.5)








start()

while True:
    StartMenu01()
    StartMenu02()
    StartingBattle()
    Attack01()




    




