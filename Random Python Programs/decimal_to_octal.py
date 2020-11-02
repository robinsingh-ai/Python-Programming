"""
Decimal To octal

"""


def decimal_to_binary(n):

    temp = 1
    main = 0
    while (temp <= n):
        temp *= 8

    temp //= 8

    while (temp > 0):

        lastdigit = n // temp
        n -= lastdigit * temp
        temp //= 8
        main = main * 10 + lastdigit

    return main


if __name__ == "__main__":

    n = int(input("Entre number"))
    print(decimal_to_binary(n))
