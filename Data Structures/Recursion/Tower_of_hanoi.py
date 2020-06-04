"""
Author: Robin Singh
IMPLEMENTATION OF TOWER OF HANOI
"""

def Tower_of_hanoi(n,s,d,aux):
    if n == 1:
        print("Move Disk From Source ",s,"To Destination",d)
    else:
        Tower_of_hanoi(n-1,s,aux,d)
        Tower_of_hanoi(1,s,d,aux)
        Tower_of_hanoi(n-1,aux,d,s)

if __name__ == '__main__':
    n = int(input("Entre Number Of Disks"))
    Tower_of_hanoi(n,'A','B','C')

