#!working with time

import random
import keyboard
import time

"""
Task 1
Basic Assignment:
Create a program to display 10 characters on screen, one at a time,
to the user.  They have to press that key to advance to the next character.
Tell the user how long it took them to press all 10 characters.

Alternately, you can select a random word from a list of words that you provide.
Have the user type in the word before the next word is selected.  This version
is easier because you can use the existing input() command that you are more
familiar with.

Your assignment should make appropriate use of functions to break the
code up into more manageable sections.  

Your assignment will be graded on the following criteria:

functionality (does it work the way it is intended)
modularity (is it broken up into functions to make your main block momre readable)
appropriate use of return values and input parameters

"""

# The code shown below is one way to read a single 
# keystroke from the keyboard and store it into 
# a variable. We will use it as the basis for this 
# assignment.

B = 'T'
Value = 0
Loop = True

Start = time.time()
print('|------------------------------|')
print("| * Press [Enter] to advance   |")
print('|------------------------------|')

while Loop == True:
    keyboard.wait('enter')
    Value = Value + 1
    print(B)

    if Value == 0:
        B = 'T'
    elif Value == 1:
        B = 'Te'
    elif Value == 2:
        B = 'Ten'
    elif Value == 3:
        B = 'Tenn'
    elif Value == 4:
        B = 'Tenna'
    elif Value == 5:
        B = 'Tenna '
    elif Value == 6:
        B = 'Tenna M'
    elif Value == 7:
        B = 'Tenna Mi'
    elif Value == 8:
        B = 'Tenna Mik'
    elif Value == 9:
        B = 'Tenna Mike'
    else:
        Loop = False

End = time.time()
Time_Took = End - Start
Time_Took = round(Time_Took,2)
print('|-------------------------------------------')
print("| * You took", Time_Took, "seconds")
print('|-------------------------------------------')


#Done










'''
while True:

    y = keyboard.read_key()
    print(y)

    
   # now = time.now()
   # print(now)
    
   
    t = time.ctime()
    print(t)

    a = time.strftime(t)

    print(a)
    break
'''


