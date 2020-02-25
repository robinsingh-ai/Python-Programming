#EVEN ODD ELEMENTS
list1=list(range(1,20))
list2=[]
list3=[]
print("Items in list 1 are\t",list1)
for x in list1:
	if x%2==0:
		list2.append(x)
	else:
		list3.append(x)
print("even elements are\t",list2)
print("odd elements are\t",list3)
