import time
import pyautogui


def ScreenShot():
    time.sleep(5)
    name=int(round(time.time()*100))
    name='{}.png'.format(name)
    img=pyautogui.screenshot(name)
    img.show()
    
ScreenShot()