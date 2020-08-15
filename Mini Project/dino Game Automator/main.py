"""
Author : Robin Singh

"""
import pyautogui
import PIL
from PIL import Image,ImageGrab
import time

def key_hit(key):
    pyautogui.keyDown(key)
    return

def take_screenShot():
    image = ImageGrab.grab().convert('L')#Converts RGB scale To grey Scale
    return image

def is_collide(data):
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                key_hit("down")
                return

    for i in range(320, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                key_hit("up")
                return
    return


if __name__ == '__main__':
    print("Dino game will start in just few secs")
    time.sleep(3)
    key_hit('up')
    while True:
        img = take_screenShot()
        data = img.load() #will return pixel date as in the form of array
        is_collide(data)
        # key_hit("up")
        
        
        # # drawing rectangle fr cactus
        # for i in range(310, 415):
        #     for j in range(563, 650):
        #         data[i,j] = 0
        # # drawing rectagle for birds
        # for i in range(300, 415):
        #     for j in range(410, 563):
        #         data[i,j] = 171
        
        
        
        # img.show()
        # break
