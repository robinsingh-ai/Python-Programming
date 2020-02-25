#Author:Robin Singh
#Problem on bubble sort algorithm
#Bubble Sort: it is a simple sorting algorithm that repeatedly steps through the list and
#compares adjacent elements and swaps them if they are in the wrong order,
#and these passes in the list will be repeated until the list is sorted.

#Time complexity has also been calculated both in BEST case and WORST case
#BEST CASE:O(n^2)
#WORST CASE :O(n^2)




def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


arr = input('Enter ur array').split()
arr = [int(x) for x in arr]
bubbleSort(arr)
print('Sorted list of entred numbers == ', end='')
print(arr)