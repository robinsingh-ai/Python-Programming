"""
Author : Robin Singh
Implementation Of Rabin Karp Algorithm

Time Complexity : Average Case = Best Case = O(length(Patter)+(length(String)))
                  Worst Case = O(length(Patter)*length(String))

"""
def rabin_karp(s1, pattern, d, q):
    h = pow(d,len(pattern)-1)%q
    p = 0
    t = 0
    index = []
    for i in range(len(pattern)):
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(s1[i]))%q
    for s in range(len(s1)-len(pattern)):
        if p == t:
            found = True
            for i in range(len(pattern)):
                if pattern[i] != s1[s+i]:
                    found = False
                    break
            if found:
                index = index + [s]
        if s < len(s1)-len(pattern): #calculate hash value for next pattern
            t = (t-h*ord(s1[s]))%q #will remove first alphabet value
            t = (t*d+ord(s1[s+len(pattern)]))%q #will add next alphabet
            t = (t+q)%q
    return index
if __name__ == '__main__':
    string1 = input("Entre String")
    pattern = input("Entre Pattern")
    l1 = rabin_karp(string1,pattern,10,7)#choose a prime number (here 7) in such a way that we can perform all the calculations with single-precision arithmetic
    if len(l1) != 0:                     #Here We have take base =10
        for i in range(len(l1)):
            print(f"Pattern Found At : {l1[i]}")
    else:
        print("Pattern Not Exists")