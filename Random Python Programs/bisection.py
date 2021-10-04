def equation(x):
    return (x**3 - 4*x - 9)

a = float(input("Enter the inital range value: ")) 
b = float(input("Enter the final range value: "))  

iteration = int(input("Enter the number of Iteration: "))

if(equation(a)*equation(b) > 0):
    print("Wrong Input! Root does not exits")
else:
    while(iteration != 0):
        x = (a+b)/2
        if(equation(x)<0):
            a = x
        elif(equation(x)>0):
            b = x
        else:
            print("Root is Zero")
        print("Root : "+str(x))
        iteration -= 1
