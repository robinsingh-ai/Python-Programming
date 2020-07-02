"""
Author : Robin Singh
Implementation Of Naive Pattern Matching Algorithm

"""
def BF(pattern, string1):
    index = []
    for i in range(len(string1)):
        j = 0
        while (j < len(pattern)):
            if (string1[i + j] != pattern[j]):
                break
            j += 1

        if (j == len(pattern)):
            index.append(i)
    return index
if __name__ == '__main__':
    l1 = BF("in", "robin singh")
    for i in range(len(l1)):
       print(f"Found At Index : {l1[i]}")




