"""
Author : Robin Singh
Implementation Of KMP string Matching Algorithm
"""
def KMP(pattern, string1):
    index = []
    m = 0
    n = 0
    prefix = prefix_generator(pattern,m+1,n)
    while m != len(string1):
        if string1[m] == pattern[n]:
            m+= 1
            n+= 1
        else:
            n = prefix[n - 1]
        if n == len(pattern):
            index.append(m - n)
            n = prefix[n - 1]
        elif n == 0:
            m+= 1
    return index
def prefix_generator(pattern,m,n):
    prefix = [0] * len(pattern)
    while m !=len(pattern):
        if pattern[m] == pattern[n]:
            n+= 1
            prefix[m] = n
            m+= 1
        elif n != 0:
            n = prefix[n - 1]
        else:
            prefix[m] = 0
            m+= 1
    return prefix
if __name__ == '__main__':
    index = KMP("in","robin singh")
    for i in index:
        print(f"Pattern Found At Index :{i}")