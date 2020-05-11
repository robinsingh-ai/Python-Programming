#Author : Robin Singh
#Heap sort happens in two phases. In the first phase, the array is transformed into a heap. A heap is a binary tree where
#-each node is greater than each of its children
#-the tree is perfectly balanced
#-all leaves are in the leftmost position available.
#2nd phase
#In 2nd phase the heap is continuously reduced to a sorted array:
#while the heap is not empty
#remove the top of the head into an array
#fix the heap.

#Complexity : Best Case = Worst Case = Average Case = O(nlogn)
#Time complexity of heapify() is O(n)


def heapify(a, n, i):
    largest = i
    l = 2 * i
    r = 2 * i + 1


    if l < n and a[i] < a[l]:
        largest = l
    if r < n and a[largest] < a[r]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)




def heapSort(a,n):



    for i in range(n, -1, -1):
        heapify(a, n, i)


    for i in range(n-1 , 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)



if __name__ == '__main__':
    a = [56,78,98,34,21,4,7,9,4,0,1]
    heapSort(a,len(a))

    print(a)
