#Write a program to calculate factorial of a number
def factorial_recursive(n):
    if n ==1:
        return  1
    else:
        return n * factorial_recursive(n-1)

n = int(input("entre ur number"))
ans = factorial_recursive(n)
print(ans)




