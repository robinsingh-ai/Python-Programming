#display common letters
s1=input("Enter first string ")
s2=input("Enter second string ")
a=list(set(s1)&set(s2))
for i in a:
	print(i)
