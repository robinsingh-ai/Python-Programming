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

def selection_sort(set):

     for i in range (len(set)-1):
        min =i
        for j in range (i+1,len(set)):
            if(set[j] < set[min]):
                min = j
            if(min != i):
               set[i], set[min] = set[min], set[i]
     return set


set = input('Enter the list of numbers: ').split()
set = [int(x) for x in set]
selection_sort(set)
print('Sorted list of entred numbers == ', end='')
print(set)


