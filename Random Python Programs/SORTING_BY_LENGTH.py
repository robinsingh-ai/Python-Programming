#SORTING BY LENGTH OF ELEMENT
a=[]
n=int(input("enter number of elements"))
for i in range(1,n+1):
	e=input("enter element")
	a.append(e)
a.sort(key=len)
print(a)
