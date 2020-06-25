"""
Author : Robin Singh
Implementation Of LCS(Dynamic Approch)

Time Complexity : O(MN)
"""
def lcs(s1, s2):
    len_s1 = len(s1) #M
    len_s2 = len(s2) #N
    arr = [['' for i in range(len_s2)]for x in range(len_s1)]

    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    arr[i][j] = s1[i]
                else:
                    arr[i][j] = arr[i-1][j-1] + s1[i]
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1], key=len)

    s3 = arr[-1][-1]
    return len(s3), s3

if __name__ == '__main__':
    s1 = input("Entre Your First String")
    s2 = input("Entre your Second String")
    #example
    # s1 = "ABCDAADERCD"
    # s2 = "ABEWASCDVVE"
    size , string = lcs(s1,s2)
    print(f"Lenth Of Sequence : {size}, And Sequence is : {string}")
