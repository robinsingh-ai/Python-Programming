import tkinter
from tkinter import *
import os
import time

def new_game(r):
    if r == 0:
        sys.exit()
    elif r == 2:
        if player == 'X':
            win_game.configure(text ='O',fg = 'red')
        else:
            win_game.configure(text='X', fg='red')
    else:
        pass


def new_game_t():
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    matrix_1 = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            matrix[i][j] = Button(font=("Times", 80, "bold", 'italic'), width=4, bg='pink',
                                  command=lambda r=i, c=j: callback(r, c))
            matrix[i][j].grid(row=i, column=j)








def callback(r,c):
    global player
    if player == 'X' and matrix_1[r][c]==0 and stop_game == False :
        matrix[r][c].configure(text = 'X',fg = 'blue',bg = 'white')
        matrix_1[r][c] = 'X'
        player='O'

    if player == 'O' and matrix_1[r][c] ==0 and stop_game ==False :
        matrix[r][c].configure(text='O', fg='red', bg='white')
        matrix_1[r][c] = 'O'
        player = 'X'


    winner()
    # new_game(player)

def winner():
    global stop_game
    for i in range(3):
        if matrix_1[i][0] == matrix_1[i][1] == matrix_1[i][2] != 0:
            matrix[i][0].configure(bg = 'yellow')
            matrix[i][1].configure(bg = 'yellow')
            matrix[i][2].configure(bg = 'yellow')
            stop_game = True

    for i in range(3):
        if matrix_1[0][i] == matrix_1[1][i] == matrix_1[2][i] != 0:
            matrix[0][i].configure(bg = 'yellow')
            matrix[1][i].configure(bg = 'yellow')
            matrix[2][i].configure(bg = 'yellow')
            stop_game = True

    if matrix_1[0][0]==matrix_1[1][1]==matrix_1[2][2]!=0:
        matrix[0][0].configure(bg='yellow')
        matrix[1][1].configure(bg='yellow')
        matrix[2][2].configure(bg='yellow')
        stop_game = True

    if matrix_1[2][0]==matrix_1[1][1]==matrix_1[0][2]!=0:
        matrix[2][0].configure(bg='yellow')
        matrix[1][1].configure(bg='yellow')
        matrix[0][2].configure(bg='yellow')
        stop_game = True


    return stop_game

if __name__ == '__main__':


    canvas = Tk()
    canvas.title("TIC TAC TOE")

    matrix = [[0,0,0],
              [0,0,0],
              [0,0,0]]

    matrix_1 = [[0,0,0],
                [0,0,0],
                [0,0,0]]

    for i in range(3):
        for j in range(3):
            matrix[i][j] = Button(font=("Times",80,"bold",'italic'),width = 4,bg = 'pink',command = lambda r=i,c=j:callback(r,c))
            matrix[i][j].grid(row = i,column = j)


    quit_game = Button(text = 'EXIT',font = ('Times',20,'bold'),width = 10,height = 6,fg = 'red',bg = 'yellow',command =lambda r =0,:new_game(r))
    quit_game.grid(row = 0,column = 4)

    win_game = Button(text = 'Winner',font = ('Times',20,'bold'),width = 10,height = 6,fg = 'red',bg = 'yellow',command =lambda r =2:new_game(r))
    win_game.grid(row = 2,column = 4)

    New_game = Button(text = 'NEW GAME',font = ('Times',20,'bold'),width = 10,height = 6,fg = 'red',bg = 'yellow',command = new_game_t)
    New_game.grid(row = 1,column = 4)


    player = 'O'
    stop_game =False

    mainloop()

