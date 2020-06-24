"""
Author : Robin Singh
Implementaion of Number Of Coins Change(Number Of ways to get reqd Sum)
Time Complexity : O(Coins*Sum)
"""
def number_of_coins(coins, sum):
    size = len(coins)
    arr = [[0 for x in range(sum+1)]for x in range(size+1)]
    for i in range(size + 1):
        arr[i][0] = 1
    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if coins[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]
    return arr[size][sum]

if __name__ == '__main__':
    coins = [2,3,5,10]
    sum = 15
    ans=number_of_coins(coins,sum)
    print(f"Number Of Ways To get Sum {sum} = {ans}")