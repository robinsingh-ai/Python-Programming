#Author : Robin Singh
#Problem on bubble sort algorithm(modified)
#Bubble Sort: it is a simple sorting algorithm that repeatedly steps through the list and
#compares adjacent elements and swaps them if they are in the wrong order,
#and these passes in the list will be repeated until the list is sorted.
#To check if the array is sorted or not, we can check if any element is getting swapped in the iteration or not.
#If none of the elements are getting swapped, then it means that the array is sroted and we can stop the process of Bubble Sort.
#So, let's use a variable to keep the record of swapping
#Here, we are using an extra variable 'flag' to store whether we are swapping in the middle of the algorithm or not
#We are setting the 'flag' value to 1 after swapping something - Flag = 1
#and at last, we are checking if something was swapped or not in the process 'if flag == 0'
#then we are breaking the loop if nothing was swapped and hence meaning that the loop is already sorted.


#Complexity : Worst case = Average Case = O(n^2)- Worst case occurs when array is reverse sorted
#Best case = O(n) -  Best case occurs when array is already sorted
#


def bubblesort(a,n):

    for i in range(0,n-1):
        flag =0


        for j in range(0,n-1-i):
            if a[j] > a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                flag = 1

        if flag == 0:
            break



a = [2,5,7,77,4,2,8,0,1,7,9,65]
n=len(a)
bubblesort(a,n)
print(a)




