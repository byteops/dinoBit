import numpy as np
from PIL import ImageGrab
import cv2
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
start_time = time.time()
last_time=0
n=-10
while 1:
    start = time.time()
    pos1 =  np.array(ImageGrab.grab(bbox=(320+n,470,322+n,472)))
    cv2.imshow('up',cv2.cvtColor(pos1, cv2.COLOR_BGR2RGB))
    pixel_values1 = np.array(pos1).reshape((2, 2, 3))
    if pixel_values1[0][1][1] != 33:
        n=n+1
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
    #pos1 =  np.array(ImageGrab.grab(bbox=(320+l,470,322+l,472)))
    #pos2 =  np.array(ImageGrab.grab(bbox=(320+m,470,322+m,472)))
    #pos3 =  np.array(ImageGrab.grab(bbox=(320+n,470,322+n,472)))
    #down =  np.array(ImageGrab.grab(bbox=(466,315,500,350)))
    #cv2.imshow('up',cv2.cvtColor(pos1, cv2.COLOR_BGR2RGB))
    #cv2.imshow('down',cv2.cvtColor(down, cv2.COLOR_BGR2RGB))
    #pixel_values1 = np.array(pos1).reshape((2, 2, 3))
    #pixel_values2 = np.array(pos2).reshape((2, 2, 3))
    #pixel_values3 = np.array(pos3).reshape((2, 2, 3))
    #print(pixel_values[0][1][1])
    #if pixel_values1[0][1][1] != 33:
    #    keyboard.press(Key.up)
    #    keyboard.release(Key.up)
    #elif pixel_values2[0][1][1] != 33:
    #    keyboard.press(Key.up)
    #    keyboard.release(Key.up)
    #elif pixel_values3[0][1][1] != 33:
    #    keyboard.press(Key.up)
    #    keyboard.release(Key.up)
