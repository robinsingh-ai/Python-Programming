"""
Author : Robin Singh
Implementation of Subset Sum problem Which will Return true if at least one sub set exists of the reqd sum

Time Complexity : O(N*Sum)
"""
def subset_sum(arr,sum):
    size = len(arr)
    table = [[0 for x in range(sum+1)]for x in range(size+1)]#this
    for i in range(size+1):
        table[i][0] = True

    for j in range(1,sum+1):
        table[0][j] = False
        for i in range(1,size+1):
            for j in range(1,sum+1):
                if table[i-1][j] == True:
                    table[i][j]= True

                else:
                    if arr[i-1]>j:
                        table[i][j] = False
                    else:
                        table[i][j] = table[i-1][j-arr[i-1]]
    return table[size][sum]


if __name__ == '__main__':

    arr = [2,3,5,7,10]
    sum = 14
    if (subset_sum(arr,sum)):
        print(f"Yes,There Exists At least One Sub-Set whose sum of the elements is {sum}")
    else:
        print(f"No Sub-Set Exists ")

