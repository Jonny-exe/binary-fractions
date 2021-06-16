#!/usr/bin/python3
import helpers

class BFraction:
    def __init__(self, number="0.0"):
        self.number = (
            helpers.float2bin(number)
            if type(number) == int or type(number) == float
            else number
        )

    def __str__(self):
        return self.number

    def __len__(self):
        return len(self.number) - 2

    def __add__(self, other):
        # Fraction
        rest = 0
        a, b = other.get_half("fraction"), self.get_half("fraction")
        if a > b:
            b = b + (len(a) - len(b)) * "0"
        else:
            a = a + (len(b) - len(a)) * "0"

        result, rest = self.add(a, b, "fraction")

        # Entire
        a, b = other.get_half("entire"), self.get_half("entire")
        if a > b:
            b = (len(a) - len(b)) * "0" + b
        else:
            a = (len(b) - len(a)) * "0" + a
        print("Nums")
        print(a)
        print(b)

        result[0:0] = (self.add(a, b, "entire", rest)[0]) + ["."]

        return "".join(result)


    def add(self, a, b, which, rest=0):
        result = []
        l = len(a)
        for i in range(0, l, 1):
            i1, i2 = len(a) - i - 1, len(b) - i - 1
            a_int, b_int = int(a[i1]), int(b[i2])
            add = a_int + b_int

            rest_value = 0 if rest == 0 else 1

            # TODO: Somehow make this cleaner

            if add + rest_value == 0:
                result.insert(0, "0")
            elif add == 0 and rest_value == 1:
                result.insert(0, "1")
                rest -= 1

            elif add == 1 and rest_value == 0:
                result.insert(0, "1")

            elif add == 2 and rest_value == 1:
                result.insert(0, "1")

            elif add == 2 and rest_value == 0:
                result.insert(0, "0")
                rest += 1

            elif add == 1 and rest_value == 1:
                result.insert(0, "0")

        if which == "entire":
            print(rest)
            result[0:0] = rest * ["1"]
            rest = 0


        return result, rest


    def get_half(self, which):
        if which == "entire":
            return self.number[:self.number.find(".")]
        elif which == "fraction":
            return self.number[self.number.find(".") + 1:]

if __name__ == "__main__":
    bf1 = BFraction(1234.5)
    bf2 = BFraction(1.5)
    print(bf1)
    print(bf2)
    ba = bf1 + bf2
    print(ba)
