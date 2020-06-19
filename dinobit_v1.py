import pyautogui
from PIL import Image, ImageGrab
import time
import keyboard


def isCollide(data):
    # Draw the rectangle for birds
    fa=0
    for i in range(f, a):
        for j in range(450, 480):
            if data[i, j] > 170 and data[i, j] < 173:
                pyautogui.press("up")
                return 1
            else:
                fa=1     
    for i in range(f, a):
        for j in range(410, 430):
            if data[i, j] > 170 and data[i, j] < 173 and fa==1:
                pyautogui.press("down")
                return 1
    return 0

if __name__ == "__main__":
    print("starting in 3s")
    time.sleep(2)
    f=275
    a=325
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        ans=isCollide(data)
      

