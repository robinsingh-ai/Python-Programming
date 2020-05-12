#Author : Robin Singh
#Shell sort is an algorithm that first sorts the elements far apart from each other and successively reduces
#the interval between the elements to be sorted. It is a generalized version of insertion sort
#In shell sort, elements at a specific interval are sorted. The interval between the elements is gradually decreased
#based on the sequence used. The performance of the shell sort depends on the type of sequence used for a given input array
#We can use different sequences methods
#Shell's original sequence: N/2 , N/4 , …, 1
#Knuth's increments: 1, 4, 13, …, (3k – 1) / 2
#Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1

#Complexity : Best Case = Average Case = O(nLogn)
# Worst Case = O(n*n)





def shellsort(a,n):

    g = n // 2
    while g > 0:
        for i in range(g, n):
            t = a[i]
            j = i
            while j >= g and a[j - g] > t:
                a[j] = a[j - g]
                j -= g

            a[j] = t
        g =g// 2

if __name__ == '__main__':
    a = [8,76,65,5,8,95,3,2,1,0]
    shellsort(a,len(a))
    print(a)
