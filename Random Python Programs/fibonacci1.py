def fibbonacchiseries(n):
    if n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbonacchiseries(n-1)+fibbonacchiseries(n-2)

n= int(input("entre ur number"))
print("fibbonacchi series : ",fibbonacchiseries(n))
