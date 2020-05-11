#Author:Robin Singh
#Problem on selection sort algorithm
# selection sort:in selection sort we consider two sub array list
# 1.)selection sort  algorithm divides the input array list into two parts:
# 2.)a sorted sublist of items which is built in from left to right at the front (left side) of the array list
# 3.)and a sublist of the remaining unsorted items that occupy the rest of the array list
# 4.)Initially, the sorted sublist is empty and the unsorted sublist is the entire input array list
# 5.)Selection sort iterates all the elements and if the smallest element
# 6.)in the list is found then that number is swapped with the first
# 7.)and moving the sublist boundaries one element to the right

# this sorting technique is similar to insertion sort
#Time complexity has also been calculated both in BEST case and WORST case
#BEST CASE:O(n^2)
#WORST CASE :O(n^2)

def selectionsort(a,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        if min !=i:
            t=a[i]
            a[i]=a[min]
            a[min]=t

a =[5,3,2,6,89,42,11,75,2,8,9,0]
selectionsort(a,len(a))
print(a)
