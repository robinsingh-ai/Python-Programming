"""
Author : Robin Singh
DRS(Decision Review System) Using Python

"""

import tkinter
import time
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils

#main window screen lenth and breath
Screen_width = 650
Screen_height = 400
Software_Window = tkinter.Tk()
img = cv2.cvtColor(cv2.imread("welcome2.png"),cv2.COLOR_BGR2RGB)
Software_Window.title("Decision Review System ")
canvas = tkinter.Canvas(Software_Window,width = Screen_width,height = Screen_height )
pic = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
screen_img = canvas.create_image(0,0,ancho = tkinter.NW,image=pic)
canvas.pack()

video  = cv2.VideoCapture("clip6.mp4")
def play_video(speed):
    # print(f"Speed is {speed}")

    frames = video.get(cv2.CAP_PROP_POS_FRAMES)
    video.set(cv2.CAP_PROP_POS_FRAMES,frames+speed)

    grab ,frame = video.read()
    frame = imutils.resize(frame,width=Screen_width,height=Screen_height)
    frame =  PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # text()





def out():
    thread = threading.Thread(target=pending , args=("out",))
    thread.daemon = 1
    thread.start()
    # print("out")

def notout():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    # print("Not Out")

def text():
    canvas.create_text(155, 25, fill="yellow", font="Times 30 bold", text="Decision Pending")
    canvas.update()

def exit_function():
    new_img = cv2.cvtColor(cv2.imread("thank.png"),cv2.COLOR_BGR2RGB)
    decision_img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(new_img))
    canvas.image = decision_img
    canvas.create_image(0, 0,image=decision_img, anchor=tkinter.NW)
    time.sleep(3)
    exit()

def pending(decision):
    #First we will display Decision Pending Image and will wait for 10 sec and then we will display out or not out depending on decision argument

    new_img = cv2.cvtColor(cv2.imread("Decision.png"),cv2.COLOR_BGR2RGB)
    decision_img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(new_img))
    canvas.image = decision_img
    canvas.create_image(0,0,image = decision_img,anchor = tkinter.NW)
    time.sleep(2)


    video2 = cv2.VideoCapture("countdown.mp4")
    t_end = time.time() + 10 #using t_end we will use this while loop for 10 secs
    while time.time()<t_end:
        frames = video2.get(cv2.CAP_PROP_POS_FRAMES)
        video2.set(cv2.CAP_PROP_POS_FRAMES,frames+8)

        grab ,frame = video2.read()
        frame = imutils.resize(frame,width=Screen_width,height=Screen_height)
        frame =  PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    if decision == 'out':
        new_img = cv2.cvtColor(cv2.imread("out.png"), cv2.COLOR_BGR2RGB)
    else:
        new_img = cv2.cvtColor(cv2.imread("not_out.png"), cv2.COLOR_BGR2RGB)

    decision_img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(new_img))
    canvas.image = decision_img
    canvas.create_image(0, 0, image=decision_img, anchor=tkinter.NW)



button = tkinter.Button(Software_Window,text = " Previous (FAST) ",width = 100, command = partial(play_video ,-15))#partial is used here to pass speed argument alog with function call
button.pack()

button = tkinter.Button(Software_Window,text = " Previous (SLOW) ",width = 100 , command = partial(play_video , -2))
button.pack()

button = tkinter.Button(Software_Window,text = " Next (FAST) ",width = 100 , command = partial(play_video , 15))
button.pack()

button = tkinter.Button(Software_Window,text = " NEXT (SLOW) ",width = 100 , command = partial(play_video , 2))
button.pack()

button = tkinter.Button(Software_Window,text = " OUT ",width = 100,command = out)
button.pack()

button = tkinter.Button(Software_Window,text = " NOT OUT ",width = 100,command = notout)
button.pack()

button = tkinter.Button(Software_Window,text = " EXIT ",width = 100,command = exit_function)
button.pack()

Software_Window.mainloop()







