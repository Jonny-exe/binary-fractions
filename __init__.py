#!/usr/bin/python3
def float2bin(number, places=50):
    rest = 0
    result = ""
    consecutive_zeros = 0
    b = 1
    i = 1
    while i < places:
        b = 2 ** -i
        if b + rest <= number:
            result += "1"
            rest += b
        else:
            result += "0"
        i += 1
    return result


def bin2float(number):
    result = 0
    number_entire = number[: number.find(".")]
    l = len(number_entire)
    # Entire number
    for i in range(l - 1, -1, -1):
        c = number_entire[i]
        if c == "1":
            result += 2 ** (l - i - 1)

    number_fraction = number[number.find(".") + 1 :]
    l = len(number_fraction)
    # Fraction number
    for i in range(l):
        c = number_fraction[i]
        if c == "1":
            result += 2 ** -(i + 1)
    return result
