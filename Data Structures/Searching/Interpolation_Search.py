"""
Author : Robin Singh
Implementation of Interpolation Search Algorithm
"""

def interpolation_search(list,n,key):
    l = 0
    h = n-1

    while l <= h and key >= list[l] and key <= list[h]:
        if l == h:
            if list[l] == key:
                return l
            return -1

        # To find the position to be searched, it uses following formula
        pos = l + int(((float(h-l)/(list[h]-list[l]))*(key-list[l])))

        if list[pos] == key:
            return pos

        if list[pos]<key:
            l=pos+1

        else:
            h = pos-1

    return -1

if __name__ == '__main__':
    list = [i for i in range(1,50,4)]
    key = int(input("Entre your key"))
    index = interpolation_search(list,len(list),key)

    if index != -1:
        print("Element found at index : ",index)
        print(list)

    else:
        print("Not Found")
