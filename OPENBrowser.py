import pyautogui
import time
import webbrowser
import pyperclip as text

chrome = (40,532)

def brows(word):
    pyautogui.doubleClick(chrome)
    time.sleep(3)                           
    pyautogui.write(word)
    pyautogui.press(['Enter'])
    time.sleep(2)
    image = pyautogui.screenshot(word + '.png')

text.copy('you')

def browsth():
    pyautogui.doubleClick(chrome)
    time.sleep(3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press(['Enter'])
    time.sleep(2)
    image = pyautogui.screenshot('y.png')
    
browsth()


