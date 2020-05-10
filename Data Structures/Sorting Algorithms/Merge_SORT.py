#Author:Robin Singh
#Problem on merge SOrt algorithm (DC approach)
#Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
#It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves
#Time complexity of Merge Sort is O(nLogn)in all 3 cases (worst, average and best)
# as merge sort always divides the array into two halves and take linear time to merge two




def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:

                arr[k] = left[i]

                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [4, 6, 4, 2, 4, 47, 8, 65, 32, 1, 9]
mergeSort(arr)
print(arr)

