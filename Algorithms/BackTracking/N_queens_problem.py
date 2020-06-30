"""
Author : Robin Singh
Implementation Of N queen Problem

"""
def place_checker(board , i , col,n):
    for k in range(col):
        if board[i][k] == 1:
            return False

    for k,j in zip(range(i,-1,-1),range(col,-1,-1)):
        if board[k][j] == 1:
            return False

    for k,j in zip(range(i,n,-1),range(col,-1,-1)):
        if board[k][j] == 1:
            return False

    return True
def n_queen(board,n,col):
    if col >= n:
        return True
    for i in range(n):
        if place_checker(board,i,col,n):
            board[i][col] = 1
            if n_queen(board,n,col+1) == True:
                return True
            board[i][col] = 0
    return False

def print_board(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print(f"Q",end=" ")
            else:
                print(0,end=" ")
        print("")

if __name__ == '__main__':
    n = int(input("Entre Value Of N"))
    board = [[0 for x in range(n)]for x in range(n)]

    ans = n_queen(board,n,0)
    if ans == False:
        print("Not exists")
    else:
        print_board(board,n)


