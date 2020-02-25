list1=["Python","Robin",5846,'X',7.89]
list2=["this","is","another","list"]

print(list1)

print(list2)              # this will print the complete list
print(list1[1:4])         # this will print the elements starting from 2nd till 4th
print(list1[1:])          # this will print the elements starting from the 2nd element
print(list1[0])           # this wil print the first element of the list
print(list1 * 2)          # this will print the list two times
print(list1 + list2)      # this will print the concatenated list


print("Elements of the list, List1 are:")
for ml in list1+list2:
    print(ml)
