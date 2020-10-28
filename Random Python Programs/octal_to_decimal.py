"""
Octal to Decimal Conversion
"""


def octal_to_decimal(n):
    main = 0
    temp = 1

    while (n > 0):

        y = n % 10
        main += temp * y
        temp *= 8
        n //= 10

    return main


if __name__ == "__main__":

    n = int(input("Entre number"))
    print(octal_to_decimal(n))
