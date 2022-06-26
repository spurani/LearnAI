import time
import pyautogui as gui
time.sleep(0.5)
hotkey = 'ctrl'
gui.hotkey(hotkey,'t')
time.sleep(2)
gui.write("https://www.linkedin.com/in/shlok-purani-4b5884126/",0.1)
time.sleep(5)
gui.hotkey(hotkey,'1')
gui.press("enter")