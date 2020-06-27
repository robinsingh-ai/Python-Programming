"""
Author : Robin Singh
Implementaion Of Minimumb Number Of coins Required To get The sum of Given Value

Time Complexity : O(Coins*Sum)

"""
def coins_change(c, sum):
    size = len(c)
    arr = [[0 for x in range(sum+1)]for x in range(size+1)]
    for i in range(size + 1):
        arr[i][0] = 0
    for j in range(sum + 1):
        arr[0][j] = 99999999
    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if c[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = min(1 + arr[i][j - c[i - 1]], arr[i - 1][j])
    return arr[size][s]

if __name__ == '__main__':

    coins = [1,5,6,9]
    s = 11
    ans = coins_change(coins,s)
    print(f"Minimum Number Of Coins Required to get the sum of {s} = {ans} Coins")