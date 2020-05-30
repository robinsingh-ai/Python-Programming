"""
FACTORIAL USING RECURSION
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        print(f"{n}*",end=" ")
        return n* factorial(n-1)

num = int(input("Entre Your Number"))
print("=",factorial(num))

