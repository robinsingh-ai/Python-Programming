"""
Author : Robin Singh
Implementation of Binary Search Algorithm(Iterative Method)
"""
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


if __name__ == '__main__':

    arr = [2,5,7,9,12,23,45,78,89,90,123,345,567,7890,12345,56789]
    x = int(input("Entre key"))
    result = binary_search(arr, x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present")