"""
IMPLEMENTATION OF FIBONACCI
"""

def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1)+fibonacci1(n-2)

num = int(input("Entre Range"))
print("Fibonacci Series  ")
for i in range(1,num+1):
    print(fibonacci1(i),end=" ")


