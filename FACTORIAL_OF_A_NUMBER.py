#Write a program to calculate factorial of a number
num=int(input(" Enter a No:"))
fact=1
if num<0:
    print("Factorial of -ve number doesnt exist")
elif num==0:
    print("fact(0)==1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of ",num,"is",fact)
