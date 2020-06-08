"""
Author : Robin Singh
Implementation of Fibonacci Search Algorithm
"""
def fibonacci(n):
    if n < 1:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def fibo_search(list,key):
    m = 0
    while fibonacci(m) < len(list):
        m = m+1


    offset = -1#Main

    while (fibonacci(m)>1):
         i = min(offset + fibonacci(m-2),len(list)-1)

         if key > list[i]:
             m = m-1
             offset = i

         elif key<list[i]:
             m = m-2

         else:

              return i

    if (fibonacci(m - 1) and list[offset + 1] == key): #if m =2 then this case will be executed
        return offset + 1
    return -1

list = [2,4,6,8,10,23,45,67,89,90,123,345,567,789,900]
key = int(input("Entre Key"))
print("Found at Index",fibo_search(list,key))

