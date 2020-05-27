"""
Author : Robin Singh
INTEGER TO BINARY USING STACKS

"""
from Sstacks import Stack


def div_by_2(num):
    s=Stack()

    while num > 0:
        r = num % 2
        s.push(r)
        num = num //2

    bin_num = ""
    while not s.isEmpty():
        bin_num+=str(s.pop())

    return bin_num

if __name__ == '__main__':
    number = int(input("Entre Your Number"))
    print(div_by_2(number))


