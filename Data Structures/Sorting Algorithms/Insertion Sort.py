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


def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > temp :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                arr[j + 1] = temp

                break




arr = input('Enter ur list').split()
arr = [int(x) for x in arr]
insertionSort(arr)
print('Sorted list of entred numbers == ', end='')
print(arr)