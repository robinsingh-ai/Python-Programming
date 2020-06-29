"""
Author : Robin Singh
Implementation Of Subset Sum Probelm Using Backtracking

"""
def sum_of_subset(list1, sum):
    if sum < 0:
        return
    if len(list1) == 0:
        if sum == 0:
            yield []
        return False
    for i in sum_of_subset(list1[1:], sum):
        yield i
    for i in sum_of_subset(list1[1:], sum - list1[0]):
        yield [list1[0]] + i
if __name__ == "__main__":
    n = int(input("Entre Sum Value"))
    list1 = list(map(int,input("Entre Set Value : ").split()))
    sub_sets = sum_of_subset(list1,n )
    list2 = list(sub_sets)
    q = len(list2)
    if q == 0:
        print("No Subsets Exists")
    else:
        print(f"Following Are The Subsets To give The Sum : {n}")
        for i in list2:
            print(i)

