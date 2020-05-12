#Author : Robin Singh
#Counting sort, like radix sort and bucket sort,
#is an integer based algorithm (i.e. the values of the input
#array are assumed to be integers). Hence counting sort is
#among the fastest sorting algorithms around, in theory. The
#particular distinction for counting sort is that it creates
#a bucket for each value and keep a counter in each bucket.
#Then each time a value is encountered in the input collection,
#the appropriate counter is incremented. Because counting sort
#creates a bucket for each value, an imposing restriction is
#that the maximum value in the input array be known beforehand.
#Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted
#Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.
#It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data.
#It is often used as a sub-routine to another sorting algorithm like radix sort.
#Counting sort uses a partial hashing to count the occurrence of the data object in O(1).
#Counting sort can be extended to work for negative inputs also.

#Complexity :  O(n+k) where n is the number of elements in input array and k is the range of input.



def counting(a,n,k,b):

    c=[0]*(k+1)
    for i in range(0,k):
        c[i]=0
    for j in range(0,n):
        c[a[j]]+=1
    for i in range(1,k+1):
        c[i]+=c[i-1]
    for j in range(n-1,-1,-1):
        b[c[a[j]]-1]=a[j]
        c[a[j]]-=1

if __name__ == '__main__':
    a= [1,4,6,8,3,2,6,9,0,7,4,1,2,5,7,8,9,6,3,5,0]
    k=max(a)
    n=len(a)
    b=[0]*n
    counting(a,n,k,b)
    print(b)

