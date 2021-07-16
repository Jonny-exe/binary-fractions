# Floating-point Binary Fractions: Do math in base 2!

![logo](https://raw.githubusercontent.com/Jonny-exe/binary-fractions/master/binary-fractions.svg)

```
 ████       ███
░░███      ░░░
 ░███████  ████  ████████    ██████   ████████  █████ ████
 ░███░░███░░███ ░░███░░███  ░░░░░███ ░░███░░███░░███ ░███
 ░███ ░███ ░███  ░███ ░███   ███████  ░███ ░░░  ░███ ░███
 ░███ ░███ ░███  ░███ ░███  ███░░███  ░███      ░███ ░███
 ████████  █████ ████ █████░░████████ █████     ░░███████
░░░░░░░░  ░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░       ░░░░░███
                                                 ███ ░███
                                                ░░██████
                                                 ░░░░░░

    ██████                                 ███      ███
   ███░░███                               ░███     ░░░
  ░███ ░░░  ████████   ██████    ██████  ███████   ████   ██████  ████████    █████
 ███████   ░░███░░███ ░░░░░███  ███░░███░░░███░   ░░███  ███░░███░░███░░███  ███░░
░░░███░     ░███ ░░░   ███████ ░███ ░░░   ░███     ░███ ░███ ░███ ░███ ░███ ░░█████
  ░███      ░███      ███░░███ ░███  ███  ░███ ███ ░███ ░███ ░███ ░███ ░███  ░░░░███
  █████     █████    ░░████████░░██████   ░░█████  █████░░██████  ████ █████ ██████
 ░░░░░     ░░░░░      ░░░░░░░░  ░░░░░░     ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░ ░░░░░░
```

[![PyPi](https://img.shields.io/pypi/v/binary-fractions)](https://pypi.org/project/binary-fractions/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An implementation of a floating-point binary fractions class and module
in Python. Work with binary fractions and binary floats with ease!

This module allows one to represent integers, floats and fractions as
binary strings.
- e.g. the integer 3 will be represented as string '0b11'.
- e.g. the float -3.75 will be represented as string '-0b11.11'.
- e.g. the fraction 1/2 will be represented as string '0b0.1'
- Exponential representation is also possible:
'-0b0.01111e3', '-0b11.1e1' or '-0b1110e-2' all represent float -3.75.
- two's complement representation is possible too:
'11.11' for -1.25 in decimal, or '-0b1.01' in binary fraction.

Many operations and transformations are offered.
You can sum, subtract, multiply, and divide long floating-point binary
fractions. You can compute power of them, shift them left, shift them right,
etc.

Basic representation of binary fractions and binary floats:
A binary fraction is a subset of binary floats. Basically, a binary fraction
is a binary float without an exponent (e.g. '-0b101.0101').
Let's have a look at an example binary float value to see how it is represented.

```
     prefix '0b' to indicate "binary" or "base 2"
     ||
     ||   decimal point
     ||   |
     ||   |    exponent separator
     ||   |    |
     ||   |    | exponent in base 10 (not in base 2!)
     ||   |    | ||
    -0b101.0101e-34  <-- example floating-point binary fraction
    |  ||| |||| |
 sign  ||| |||| exponent sign
       ||| ||||
       ||| fraction bits in base 2
       |||
       integer bits in base 2
```

If you are curious about floating point binary fractions, have a look at:
- https://en.wikipedia.org/wiki/Computer_number_format#Representing_fractions_in_binary
- https://www.electronics-tutorials.ws/binary/binary-fractions.html
- https://ryanstutorials.net/binary-tutorial/binary-floating-point.php
- https://planetcalc.com/862/
If you are curious about Two's complement:
- https://janmr.com/blog/2010/07/bitwise-operators-and-negative-numbers/
- https://en.wikipedia.org/wiki/Two%27s_complement

## License:
- GPL v3 or later

## Features:
- Python 3
- constructors for various types: int, float, Fraction, str, TwosComplement, Binary
- supports many operators: +, -, *, /, //, %, **, <<, >>, ~, &, ...
- supports many methods: not, abs, round, floor, ceil, ...
- very high precision
- many operations are lossless, i.e. with no rounding errors or loss of precision
- supports very long binary fractions
- supports exponential representations
- well documented
    - Please read the documentation inside the source code
  ([binary.py](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/binary.py)).
    - Or look at the pydoc-generated documentation in
  [README.md](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/README.md).
- well tested
    - over 1500 test cases


## Sample usage, Example calls:

Please have a look at the short example program that uses the
`Binary` class and module. See file
[binary_sample.py](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/binary_sample.py).

The sample source code looks like this:
```
#!/usr/bin/python3

# Sample program using the Binary class and module.

# Install with: pip3 install --upgrade binary-fractions
if __name__ == "__main__":
    from binary_fractions import TwosComplement, Binary
    from math import ceil, floor

    bf1str: str = "-1.01"  # -1.25
    bf2str: str = "10.1"  # 2.5
    bf3str: str = "10.1e-3"  # 2.5/8
    tcstr1: str = "10.1"  # -1.5 in two's complement, '-0b1.1' as binary fraction
    tcstr2: str = "100001001000.1"  # -1975.5 in two's complement, '-0b11110111000.1'
    fl1: float = 2.3
    fl2: float = -1975.5

    bf1: Binary = Binary(bf1str)
    bf2: Binary = Binary(bf2str)
    bf3: Binary = Binary(bf3str)
    tc1: TwosComplement = TwosComplement(tcstr1)
    tc2: TwosComplement = TwosComplement(tcstr2)
    tc3: TwosComplement = TwosComplement(fl2)

    print("Sample program demonstrating binary fractions class and module:")
    print(f"Binary({fl1}) = {Binary(fl1)}")
    print(f"Binary({fl2}) = {Binary(fl2)}")
    print(f"Binary({bf3str}) = {Binary(bf3str)}")
    print(f"{bf1} = {bf1}")
    print(f"{bf1} + {bf2} = {bf1+bf2}")
    print(f"{bf1} - {bf2} = {bf1-bf2}")
    print(f"{bf1} * {bf2} = {bf1*bf2}")
    print(f"{bf1} / {bf2} = {bf1/bf2}")
    print(f"{bf1} // {bf2} = {bf1//bf2}")
    print(f"{bf1} % {bf2} = {bf1%bf2}")
    print(f"{bf2} ** {bf1} = {bf2**bf1}")
    print(f"{bf1} >> {1} = {bf1>>1}")
    print(f"{bf1} << {1} = {bf1<<1}")
    print(f"abs({bf1}) = {abs(bf1)}")
    print(f"round({bf1}) = {round(bf1)}")
    print(f"ceil({bf1}) = {ceil(bf1)} (int)")
    print(f"Binary('{bf1}').ceil() = {bf1.ceil()} (Binary)")
    print(f"floor({bf1}) = {floor(bf1)} (int)")
    print(f"Binary('{bf1}').floor() = {bf1.floor()} (Binary)")
    print(f"int({bf1}) = {int(bf1)}")
    print(f"float({bf1}) = {float(bf1)}")
    print(f"str({bf1}) = {str(bf1)}")
    print(f"str({bf3}) = {str(bf3)}")
    print(f"Fraction({bf1}) = {bf1.fraction()}")
    print(f"{bf1} & {bf2} = {bf1&bf2}")
    print(f"{bf1} | {bf2} = {bf1|bf2}")
    print(f"{bf1} ^ {bf2} = {bf1^bf2}")
    print(f"~(floor({bf2})) = {~(floor(bf2))}")
    print(f"type({bf1}) = {type(bf1)}")
    print(f"type({tc1}) = {type(tc1)}")
    print(f"Binary('{bf3}').to_no_exponent() = {bf3.to_no_exponent()}")
    print(f"Binary('{bf3}').to_no_mantissa() = {bf3.to_no_mantissa()}")
    # scientific notation
    print(f"Binary('{bf3}').to_sci_exponent() = {bf3.to_sci_exponent()}")
    # engineering notation
    print(f"Binary('{bf3}').to_eng_exponent() = {bf3.to_eng_exponent()}")
    print(f"Binary('{bf1}').to_twos_complement() = {bf1.to_twoscomplement()}")
    print(f"Binary(TwosComplement('{tcstr1}')) = {Binary.from_twoscomplement(tc1)}")
    print(f"Binary(TwosComplement('{tcstr2}')) = {Binary.from_twoscomplement(tc2)}")
    print(f"Binary(TwosComplement({fl2})) = {Binary.from_twoscomplement(tc3)}")
    print(f"TwosComplement({fl2}) = {TwosComplement(fl2)}")
    print("And there are more operands, more methods, more functions, ...")
    print("For more information read the documentation at:")
    print("https://raw.githubusercontent.com/Jonny-exe/binary-fractions")
```

When executed with the command `python3 binary_sample.py`, it returns these
results:

```
Sample program demonstrating binary fractions class and module:
Binary(2.3) = 0b10.01001100110011001100110011001100110011001100110011
Binary(-1975.5) = -0b11110110111.1
Binary(10.1e-3) = 0b10.1e-3
-0b1.01 = -0b1.01
-0b1.01 + 0b10.1 = 0b1.01
-0b1.01 - 0b10.1 = -0b11.11
-0b1.01 * 0b10.1 = -0b11.001
-0b1.01 / 0b10.1 = -0b0.1
-0b1.01 // 0b10.1 = -0b1
-0b1.01 % 0b10.1 = 0b1.01
0b10.1 ** -0b1.01 = 0b0.010100010110111110001011100001001001101110110100110011
-0b1.01 >> 1 = -0b0.101
-0b1.01 << 1 = -0b10.1
abs(-0b1.01) = 0b1.01
round(-0b1.01) = -0b1
ceil(-0b1.01) = -1 (int)
Binary('-0b1.01').ceil() = -0b1 (Binary)
floor(-0b1.01) = -2 (int)
Binary('-0b1.01').floor() = -0b10 (Binary)
int(-0b1.01) = -1
float(-0b1.01) = -1.25
str(-0b1.01) = -0b1.01
str(0b10.1e-3) = 0b10.1e-3
Fraction(-0b1.01) = -5/4
-0b1.01 & 0b10.1 = 0b10.1
-0b1.01 | 0b10.1 = -0b1.01
-0b1.01 ^ 0b10.1 = -0b11.11
~(floor(0b10.1)) = -3
type(-0b1.01) = <class 'binary.Binary'>
type(10.1) = <class 'binary.TwosComplement'>
Binary('0b10.1e-3').to_no_exponent() = 0b0.0101
Binary('0b10.1e-3').to_no_mantissa() = 0b101e-4
Binary('0b10.1e-3').to_sci_exponent() = 0b1.01e-2
Binary('0b10.1e-3').to_eng_exponent() = 0b101000000e-10
Binary('-0b1.01').to_twos_complement() = 10.11
Binary(TwosComplement('10.1')) = -1.1
Binary(TwosComplement('100001001000.1')) = -11110110111.1
Binary(TwosComplement(-1975.5)) = -11110110111.1
TwosComplement(-1975.5) = 100001001000.1
```

## Requirements:
- Python 3
- requires no `pip` packages (uses built-in `math` and `fractions` modules for
    math operations, uses `unittest` for unit testing)

## Installation:
- see [https://pypi.org/project/binary-fractions/](https://pypi.org/project/binary-fractions/)
- `pip install binary-fractions`

## Testing, Maturity
- run `python3 binary_sample.py` to execute a simple sample program
- run `python3 binary_test.py` to execute all unit tests
- `Binary` is relatively mature, more than 1500 test cases have been written and all
    passed.

## Contributions:
- PRs are welcome and very much appreciated! :+1:
- Please run and pass all existing 1500+ test cases in
    [binary_test.py](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/binary_test.py)
    before issuing a PR.
- File Format: linted/beautified with [black](https://github.com/psf/black)
- Test case format: [unittest](https://docs.python.org/3/library/unittest.html)
- Documentation format: [pydoc](https://docs.python.org/3/library/pydoc.html)

Enjoy :heart: !