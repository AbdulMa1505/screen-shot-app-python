import time
import pyautogui as ss
import tkinter as tk

def ScreenShot():
    # time.sleep(5)
    name=int(round(time.time()*100))
    name='C://Users//Abdul Malik//Desktop//PYTHON//screenshots{}.png'.format(name)
    img=ss.screenshot(name)
    img.show()
    
def quit():
    window.destroy()


window=tk.Tk()
window.title("Screenshot App")
frame=tk.Frame(window)
frame.pack()
button=tk.Button(frame, text="take screenshot",command=ScreenShot)
button.pack(side=tk.LEFT)
close=tk.Button(frame,text="QUIT",command=quit)
close.pack(side=tk.LEFT)

window.mainloop()