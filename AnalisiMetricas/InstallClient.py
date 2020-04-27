import pyautogui
import time

#print (pyautogui.position())
# Point(x=893, y=592)
pyautogui.FAILSAFE = False


print ("Iniciar instalador")
pyautogui.click (x=324, y=128, clicks=2)
time.sleep(10)
print (" Click 1")
pyautogui.click (x=893, y=592)
time.sleep(10)
print (" Click 2")
pyautogui.click (x=893, y=592)
time.sleep(10)
print (" Click 3")
pyautogui.click (x=893, y=592)
time.sleep(10)
pyautogui.click (x=718, y=606)
time.sleep(10)
pyautogui.press('tab') 
time.sleep(3)
pyautogui.press('enter')  