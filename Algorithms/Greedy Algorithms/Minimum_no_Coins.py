"""
Author : Robin Singh
Implementation of Minimum Coin Exchange Problem

"""

def change(rs,changes,n):
    c= []
    i = n-1
    while i>=0:
        while rs >=changes[i]:
            rs = rs - changes[i]
            c.insert(0,changes[i])

        i-=1

    return c


if __name__ == '__main__':
    rs = int(input("Entre Your Money"))
    Notes_coin = [.50,1,2,5,10,20,50,100,200,500,2000]
    _change = change(rs,Notes_coin,len(Notes_coin))
    print("Following are the Minimum Change :")
    for i in range (0,len(_change)):
        print(f" {_change[i]} ",end="")

