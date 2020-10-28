"""
Hexadecimal to Decimal Conversion
"""


def __getdecimaldigits(digit):
    digits = ['0', '1', '2', '3', '4', '5', '6',
              '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x


def hexadecimal_to_decimal(n):
    main = 0
    temp = 0

    inputsize = len(n)

    for i in range(inputsize, 0, -1):
        main = main + 16 ** temp * __getdecimaldigits(n[i-1])
        temp += 1

    return str(main)


if __name__ == "__main__":

    n = input("enter number")
    print(hexadecimal_to_decimal(n))
