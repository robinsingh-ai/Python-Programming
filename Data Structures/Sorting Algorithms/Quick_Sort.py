#Author:Robin Singh
#Problem on quicksort (DC Approch)
#Quicksort works by selecting an element called a pivot and splitting
#the array around that pivot such that all the elements in, say, the
#left sub-array are less than pivot and all the elements in the right
#sub-array are greater than pivot. The splitting continues until the
#array can no longer be broken into pieces. That's it. Quicksort is done.

#Complexity
#Best Case = Average Case = O(nLogn)- Each partition splits array into equal halves
#Worst Case = O(n^2) - Each partition gives unbalanced split




def partition(a,lb,ub):
    pivot = a[lb]
    start = lb
    end = ub

    while start < end:
        while a[start] <= pivot:
            start+=1
        while a[end] > pivot:
            end-=1
        if start < end:
            t=a[start]
            a[start]=a[end]
            a[end]=t

    a[lb]=a[end]
    a[end]=pivot
    return end

def quicksort(a,lb,ub):
    if lb < ub:
        p= partition(a,lb,ub)
        quicksort(a,lb,p-1)
        quicksort(a,p+1,ub)



a = [2,5,8,3,1,7,9,11,21,0]
quicksort(a,0,len(a)-1)
print(a)


