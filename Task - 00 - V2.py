import random
import keyboard
import time
import pyautogui
import os

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)
Attack1 = True
CLICK = False
Upgrade1 = 0
Upgrade2 = 0
ClickTime = 0.0000000000000001
block_con = 0.977
upgrade_con = 0.98
TIME = False
a = 0

#https://kodiqi.itch.io/idle-breakout

def start():
    os.startfile(("H:\profile\desktop\Google Chrome.lnk"))
    time.sleep(0.5)
    pyautogui.hotkey('f11',interval=0.1)
    

    try:
        x, y = pyautogui.locateCenterOnScreen('00 - GuestMode.png',confidence =0.97, grayscale=True)
        pyautogui.click(x, y)
    except Exception as e:
        #print(str(e) + "not found")
        pass

    pyautogui.write('https://kodiqi.itch.io/idle-breakout')  
    pyautogui.hotkey('enter',interval=0.1)
    pyautogui.hotkey('f11',interval=0.1)

def Upgrade01():
        try:
            loc = pyautogui.locateCenterOnScreen('Upgrade1.png',confidence = 0.97)
            pyautogui.moveTo(loc)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()
            return True
        except Exception as e:
            return False
            
def Upgrade02():
        try:
            loc = pyautogui.locateCenterOnScreen('Upgrade2.png',confidence = 0.96)
            pyautogui.moveTo(loc)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()
            return True
        except Exception as e:
            return False
        
def Upgrade03():
        try:
            loc = pyautogui.locateCenterOnScreen('Upgrade3.png',confidence = 0.96)
            pyautogui.moveTo(loc)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()
            return True
        except Exception as e:
            return False

'''
def Level10():
    if a == 0:
        try:
            pyautogui.locateCenterOnScreen('Level10.png',confidence = 1)
            return True
        except:
            return False
    if True:
        try:
            pyautogui.moveTo(924, 60)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()

            pyautogui.moveTo(367, 175)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()

            pyautogui.moveTo(389, 332)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()

            pyautogui.moveTo(387, 394)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()

            pyautogui.moveTo(392, 565)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()


            pyautogui.moveTo(698, 628)
            pyautogui.mouseDown()
            time.sleep(ClickTime)
            pyautogui.mouseUp()
            a = 1

            return True
        except Exception as e:
            return False
'''


def Block01():
    try:
        loc = pyautogui.locateCenterOnScreen('Block1.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(ClickTime)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block02():
    try:
        loc = pyautogui.locateCenterOnScreen('Block2.png',confidence = 0.99)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(ClickTime)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block03():
    try:
        loc = pyautogui.locateCenterOnScreen('Block3.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(ClickTime)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        print(str(e))
        return False

def Block04():
    try:
        loc = pyautogui.locateCenterOnScreen('Block4.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(ClickTime)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block05():
    try:
        loc = pyautogui.locateCenterOnScreen('Block5.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block06():
    try:
        loc = pyautogui.locateCenterOnScreen(f'Block{x}.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block07():
    try:
        loc = pyautogui.locateCenterOnScreen('Block7.png',confidence = 0.98)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block08():
    try:
        loc = pyautogui.locateCenterOnScreen('Block8.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block09():
    try:
        loc = pyautogui.locateCenterOnScreen('Block9.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block10():
    try:
        loc = pyautogui.locateCenterOnScreen('Block10.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block11():
    try:
        loc = pyautogui.locateCenterOnScreen('Block11.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block12():
    try:
        loc = pyautogui.locateCenterOnScreen('Block12.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block13():
    try:
        loc = pyautogui.locateCenterOnScreen('Block13.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block14():
    try:
        loc = pyautogui.locateCenterOnScreen('Block14.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block15():
    try:
        loc = pyautogui.locateCenterOnScreen('Block15.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block16():
    try:
        loc = pyautogui.locateCenterOnScreen('Block16.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block17():
    try:
        loc = pyautogui.locateCenterOnScreen('Block17.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block18():
    try:
        loc = pyautogui.locateCenterOnScreen('Block18.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block19():
    try:
        loc = pyautogui.locateCenterOnScreen('Block19.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False

def Block20():
    try:
        loc = pyautogui.locateCenterOnScreen('Block20.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block21():
    try:
        loc = pyautogui.locateCenterOnScreen('Block21.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block22():
    try:
        loc = pyautogui.locateCenterOnScreen('Block22.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block23():
    try:
        loc = pyautogui.locateCenterOnScreen('Block23.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block24():
    try:
        loc = pyautogui.locateCenterOnScreen('Block24.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block25():
    try:
        loc = pyautogui.locateCenterOnScreen('Block25.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block26():
    try:
        loc = pyautogui.locateCenterOnScreen('Block26.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block27():
    try:
        loc = pyautogui.locateCenterOnScreen('Block27.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block28():
    try:
        loc = pyautogui.locateCenterOnScreen('Block28.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block29():
    try:
        loc = pyautogui.locateCenterOnScreen('Block29.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False
    
def Block30():
    try:
        loc = pyautogui.locateCenterOnScreen('Block30.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False











start()

while True:
        if Upgrade01() == False:
            if Upgrade02() == False:
                if Upgrade03() == False:
                    if Block01() == False:
                        if Block02() == False:
                            if Block03() == False:
                                if Block04() == False:
                                    if Block05() == False:
                                        if Block06() == False:
                                            if Block07() == False:
                                                if Block08() == False:
                                                    if Block09() == False:
                                                        if Block10() == False:
                                                            if Block11() == False:
                                                                if Block12() == False:
                                                                    if Block13() == False:
                                                                        if Block14() == False:
                                                                            if Block15() == False:
                                                                                if Block16() == False:
                                                                                    if Block17() == False:
                                                                                        if Block18() == False:
                                                                                            if Block19() == False:
                                                                                                if Block20() == False:
                                                                                                      if Block21() == False:
                                                                                                            if Block22() == False:
                                                                                                                  if Block23() == False:
                                                                                                                        if Block24() == False:
                                                                                                                              if Block25() == False:
                                                                                                                                    if Block26() == False:
                                                                                                                                          if Block27() == False:
                                                                                                                                              if Block28() == False:
                                                                                                                                                  if Block29() == False:
                                                                                                                                                      if Block30() == False:
                                                                                                                                                          pass
                                                                                                                                                            


'''
def Block(x):
    try:
        loc = pyautogui.locateCenterOnScreen(f'Block{x}.png',confidence = block_con)
        pyautogui.moveTo(loc)
        pyautogui.mouseDown()
        time.sleep(0.000001)
        pyautogui.mouseUp()
        return True
    except Exception as e:
        return False                      
'''


#fix block 3















        




        




