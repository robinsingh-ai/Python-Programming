"""
Author : Robin Singh
Implementation of Jump Search Algorithm
"""
import math
def jump_search(arr,search):
    low = 0
    jump = int(math.sqrt(len(arr)))
    for i in range(0,len(arr),jump):
        if arr[i] < search:
            low = i
        elif arr[i] == search:
            return i
        else:
            break
    c=low
    for j in arr[low:]:
        if j==search:
            return c
        c+=1
    return "Not found"

arr = [1,4,7,9,12,23,25,28,30,35,40,50,56,58,60,78,89,95,100,150]
key = int(input("Entre Key"))
print(f"{key} Found At Index {jump_search(arr, key)}")