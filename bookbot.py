import pyautogui
from pynput.keyboard import Key, Controller
from time import sleep
from tkinter import Tk
import os

keyboard = Controller()

print('[BookBot] Started program. Waiting for 3 seconds...')
sleep(3)
cords = pyautogui.locateCenterOnScreen('arrow.png')

if cords == None:
    print('[BookBot] Couldn\'t find arrow! Please ensure default texture pack is used & book menu is visible then try again.')
    print('[BookBot] Exiting program.')
    os.system('pause')
    quit()

else:
    print('[BookBot] Found arrow button successfully!')

def press(letter):
    keyboard.press(letter)
    keyboard.release(letter)

def next_page():
    pyautogui.click(cords)

try:
    f = open('text.txt', "r")
except:
    print('[BookBot] Could not find "text.txt" file!')
    print('[BookBot] Exiting program.')
    os.system('pause')
    quit()

print('[BookBot] Found "text.txt" file successfully. Starting typing!')

text = f.read()
count = 0
page = 0

for word in text.split(' '):
    if (page >= 99):
        print('[BookBot] Ran out of pages!')
        os.system('pause')
        quit()

    if (count + len(word) >= 256):
            count = 0
            next_page()
            page += 1
    
    for char in word:
        press(str(char))
        count += 1
    press(' ')
    count += 1

print('[BookBot] Program complete!')
os.system('pause')
quit()