import pyautogui
import time
import pyperclip as text

chrome = (40,532)

#เสิร์จแบบภาษาEng
'''
def brows(word):
	pyautogui.doubleClick(chrome)
	time.sleep(3)                           
	pyautogui.write(word)
	pyautogui.press(['Enter'])
	time.sleep(2)
	image = pyautogui.screenshot(word + '.png')

brows('Thailand')
'''

#เสิร์จแบบภาษาTH
def browsth(word):
	text.copy(word)
	pyautogui.doubleClick(chrome)
	time.sleep(3)
	pyautogui.hotkey('ctrl','v')
	pyautogui.press(['Enter'])
	time.sleep(2)
	
browsth('ท้องฟ้า')


