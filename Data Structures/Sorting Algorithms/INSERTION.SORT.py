#Author:Robin Singh
#Problem on insertion sort algorithm
#Insertion sort:This is an in-place comparison-based sorting algorithm
# here two  sub-list is formed like in selection sort but here approch is different
# in selection sort the left sub list has been kept empty but here instead of being kept empty we kept only 1st element  in it
# For example the left part of an array is maintained to be sorted
# An element which is to be 'insert'ed in this sorted sub-list
# has to find its appropriate place and then it has to be inserted there
# thats why its name is  insertion sort.

#Time complexity has also been calculated both in BEST case and WORST case
#BEST CASE:O(n)
#WORST CASE :O(n^2)





def insertionsort(a,n):
    for i in range(1,n):      #right unsorted sub array
        t=a[i]
        j=i-1

        while j >= 0 and a[j] > t :     #lef sorted sub array
            a[j+1] = a[j]
            j-=1

        a[j + 1] = t



a = [67,54,23,12,4,6,8,90,87,54,21,1,0]

insertionsort(a,len(a))
print(a)
