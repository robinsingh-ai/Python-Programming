"""
Author : Robin Singh
Implementation of Linear  Search Algorithm
"""
pos = -1
def linear_search(list,n):
    i = 0
    while i < len(list):
        if n == list[i]:
            globals()['pos'] = i
            return True
        i +=1

    return False



if __name__ == '__main__':

    list = [4,9,8,71,3,24,56,89,90,12,1,2,10]
    n = int(input("Entre Search Value"))
    if linear_search(list,n):
        print("Found at Index ",pos)

    else:
        print("not Found")