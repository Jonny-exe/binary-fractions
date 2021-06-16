#!/usr/bin/python3
import math
def float2bin(number, places=50):

    entire_number = math.floor(number)
    i = math.floor(math.log2(entire_number))
    result = ["0"] * (i + 1)
    current_number = 0
    while i >= 0:
        result[len(result) - 1 - i] = str(int(entire_number >= 2 ** i + current_number))
        current_number += (2 ** i) * int(result[len(result) - 1 -i])
        print(result)
        i -= 1

    print(result)
    # cleanup
    i = 0
    while True:
        if result[i] == "0":
            result = result[i + 1:]
        else:
            break

    del current_number

    result.append(".")

    rest = 0
    i = 1
    zeros = 0
    fraction_number = number - math.floor(number)
    while i < places:
        b = 2 ** -i
        if b + rest <= fraction_number:
            result.extend(["0"] * zeros + ["1"])
            rest += b
            zeros = 0

        else:
            zeros += 1
        i += 1

    return "".join(result)


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


n = 2.625
b = float2bin(n)
f = bin2float(b)
print(n, b, f)
