import pyautogui
import time
while True:


    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX,currentMouseY)
    time.sleep(5)

