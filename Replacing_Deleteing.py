#Replacing List Element with new one in Python
my_list = ["zero", "one", "two", "three", "four"]
print("Elements of the list, my_list are:")
for ml in my_list:
    print(ml);
my_list[0] = "hundered"
my_list[4] = 500
print("\nNow elements of the list, my_list are:")
for ml in my_list:
    print(ml)


#Deleting Element from List in Python
my_list = ["zero", 1, "two", 3, "four"]
print("Elements of the list, my_list are:")
for ml in my_list:
    print(ml)
index = input("\nEnter index no:")
index = int(index)
print("Deleting the element present at index number",index)
del my_list[index]
print("\nNow elements of the list, my_list are:")
for ml in my_list:
    print(ml)
