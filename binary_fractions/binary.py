#!/usr/bin/python3

"""# Floating-point Binary Fractions: Do math in base 2!

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

from binary import TwosComplement
from binary import Binary
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
ceil(-0b1.01) = -1 (int)
Binary('-0b1.01').ceil() = -0b1 (Binary)
floor(-0b1.01) = -2 (int)
Binary('-0b1.01').floor() = -0b10 (Binary)
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

"""

from __future__ import annotations  # to allow type hinting in class methods
from fractions import Fraction
import math
import re
import sys
import unittest
from typing import Union


_BINARY_WARNED_ABOUT_FLOAT = False
_BINARY_RELATIVE_TOLERANCE = 1e-10
_BINARY_PRECISION = 128  # number of binary digits to the right of decimal point
_PREFIX = "0b"
_EXP = "e"
_NAN = "NaN"
_INF = "Inf"
_NINF = "-Inf"
# _BINARY_VERSION will be set automatically with git hook upon commit
_BINARY_VERSION = "20210716-114757"  # format: date +%Y%m%d-%H%M%S
# _BINARY_TOTAL_TESTS will be set automatically with git hook upon commit
_BINARY_TOTAL_TESTS = 1503  # number of asserts in .py file

# see implementation of class Decimal:
# https://github.com/python/cpython/blob/3.9/Lib/_pydecimal.py
# https://docs.python.org/3/library/decimal.html
# see implementation of class Fraction:
# https://github.com/python/cpython/blob/3.9/Lib/fractions.py
# https://docs.python.org/3/library/fractions.html
# https://github.com/bradley101/fraction/blob/master/fraction/Fraction.py


##########################################################################
# CLASS TWOSCOMPLEMENT
##########################################################################


class TwosComplement(str):
    """Floating point class for representing twos-complement (2's complement).

    If you are curious about Two's complement, read the following:
    - https://en.wikipedia.org/wiki/Two%27s_complement
    - https://janmr.com/blog/2010/07/bitwise-operators-and-negative-numbers/

    The twos-complement format is as follows.
    - there is no sign (-, +)
    - there is no extra sign bit per se
    - positive numbers must have a leading 0 to be recognized as positive
    - hence positive numbers by definition always start with a 0
    - negative numbers always start with a 1
    - negative numbers can have an arbitrary number of additional leading 1s
    - positive numbers can have an arbitrary number of additional leading 0s
    - there must be one or more decimal bits
    - there is an optional decimal point
    - there are 0 or more fractional bits
    - there is an optional exponent in decimal (e.g. e-34), the exponent is not binary

    ```
    Syntax:
    In 'regex' the syntax is
    r"\s*((?=[01])(?P<int>[01]+)(\.(?P<frac>[01]*))?(E(?P<exp>[-+]?\d+))?)\s*\Z".

    In simpler terms, the syntax is as follows:
        [0,1]+[.][0,1]*[e[-,+][0-9]+]
        integer bits (at least 1 bit required, leading bit indicates if pos. or neg.)
            decimal point (optional, one or none)
                fractional bits (optional, zero or more)
                    exponent (optional, possible with sign - or +, in decimal)

        decimal |   binary fraction | twos-complement
        ---------------------------------------------
        -2.5e89 |       -10.1e89    | 101.1e89
        -6      |       -110        | 1010
        -5      |       -101        | 1011
        -0.5e3  |       -0.1e3      | 1.1e3
        -4      |       -100        | 100
        -3      |       -11         | 101
        -2.5    |       -10.1       | 101.1
        -0.25e3 |       -0.01e3     | 1.11e3
        -2      |       -10         | 10
        -1.5    |       -1.1        | 10.1
        -1      |       -1          | 1
        -0.5    |       -0.1        | 1.1
        -0.25   |       -0.01       | 1.11
        -0.125  |       -0.001      | 1.111
        0       |       0           | 0
        1.5e-4  |       1.1e-4      | 01.1e-4
        2.75e-4 |       10.11e-4    | 010.11e-4
        0.25    |       0.01        | 0.01
        0.5     |       0.1         | 0.1
        1       |       1           | 01
        1.5     |       1.1         | 01.1
        2       |       10          | 010
        2.75    |       10.11       | 010.11
        3       |       11          | 011
        4       |       100         | 0100
        5       |       101         | 0101
        6       |       110         | 0110

    ```

    Valid TwosComplement strings are: 0, 1, 01, 10, 0.0, 1.1, 1., 0.1e+34,
    11101.e-56, 0101.01e78. 000011.1000e0 is valid and is the same as 011.1.
    Along the same line, 111101.0100000e-0 is valid and is the same as 101.01.

    Invalid TwosComplement strings are: -1 (minus), +1 (plus),
    .0 (no leading decimal digit),
    12 (2 is not a binary digit),
    1.2.3 (2 decimal points),
    1e (missing exponent number),
    1e-1.1 (decimal point in exponent).

    """

    def __new__(
        cls,
        value: Union[int, float, Fraction, str] = 0,
        length: int = -1,
        rel_tol: float = _BINARY_RELATIVE_TOLERANCE,
        ndigits: int = _BINARY_PRECISION,
        simplify: bool = True,
        warn_on_float: bool = False,
    ) -> TwosComplement:
        """Constructor.

        Use __new__ and not __init__ because TwosComplement is immutable.
        Allows string, float, integer, and Fraction as input for constructor.
        If instance is contructed from a string, by default the string will
        be simplified. With 'simplify' being False, attention is paid to
        *not* modify the string or to modify it as little as possible.
        With simplify being False, if given '1e1' it will remain as '1e1',
        it will not change it to '1'. Same with '1000', which will not change
        to '1e4'. In short, without simplification, attempts are made to keep
        the string representation as close to the original as possible.

        Examples:
        * TwosComplement(4) returns '0100'
        * TwosComplement(-2) returns '10'
        * TwosComplement(-1.5) returns '10.1'
        * TwosComplement(Fraction(-1.5)) returns '10.1'
        * TwosComplement('110.101') returns '110.101'
        * TwosComplement('110.101e-34') returns '110.101e-34'

        Parameters:
        value (int, float, Fraction, str): value of number

        length (int): desired length of resulting string. If default -1, string
            will be presented its normal (shortest) representation. If
            larger, string will be prefixed with leading bits to achieve
            desired length. If length is too short to fit number, an
            exception will be raised.
            Example of length 4 is '01.1'.

        ndigits (int): desired digits after decimal point. 'ndigits' is only
            relevant for Fractions.

        rel_tol (float): relative tolerance that influences precision further.
            A bigger tolerance leads to a possibly less precise result.
            A smaller tolerance leads to a possibly more precise result.
            'rel_tol' is only relevant for floats.

        simplify (bool): If True, try to simplify string representation.
            If False, try to leave the string representation as much as is.
            'simplify' is only relevant for strings.

        warn_on_float (bool): If True print a warning statement to stdout to
            warn about possible loss in precision in case of conversion from
            float to TwosComplement.
            If False, print no warning to stdout.
            'warn_on_float' is only relevant for floats.

        Returns:
        TwosComplement: created immutable instance representing twos-complement
        number as a string of class TwosComplement.


        Testcases:
            model: self.assertIsInstance(TwosComplement(X1), TwosComplement)
            cases: some test cases for return class
                - 1
                - -2
                - -2.5
                - '10'
                - '010'
                - Fraction(3,4)


            model: self.assertEqual(TwosComplement(X1), X2)
            cases: some test cases for equal
                - -2 ==> '10'
                - 2 ==> '010'
                - -1.5 ==> '10.1'
                - 3.5 ==> '011.5'
                - '10.101' ==> '10.101'
                - '0001.00' ==> '01'
                - Fraction(-3,2) ==> '10.1'
                - Fraction(7,2) ==> '011.5'


            model: with self.assertRaises(ValueError):
                TwosComplement(X1)
            cases: some test cases for raising ValueError
                - "102"
                - "nan"
        """
        if isinstance(value, int):
            return str.__new__(cls, TwosComplement._int2twoscomp(value, length))
        if isinstance(value, float):
            return str.__new__(
                cls,
                TwosComplement._float2twoscomp(value, length, rel_tol, warn_on_float),
            )
        if isinstance(value, Fraction):
            return str.__new__(cls, TwosComplement._fraction2twoscomp(value, length))
        if isinstance(value, str):
            return str.__new__(
                cls, TwosComplement._str2twoscomp(value, length, simplify=simplify)
            )
        # any other types
        raise TypeError(
            f"Cannot convert {value} of type {type(value)} to TwosComplement"
        )

    def _int2twoscomp(value: int, length: int = -1) -> str:
        """Computes the two's complement of int value.

        This is a utility function.
        Users should use the constructor TwosComplement(value) instead.

        Parameters:
        value (int): integer to convert into twos-complement string.
        length (int): desired length of string. If default -1, string
            will be presented its normal (shortest) representation. If
            larger, string will be prefixed with leading bits to achieve
            desired length. If length is too short to fit number, an
            exception will be raised.
            Example of length 4 is '01.1'.

        Returns:
        str: string containing twos-complement of value
        """
        if value == 0:
            digits = 1
        elif value > 0:
            # add 1 for leading '0' in positive numbers
            # less precise: digits = math.ceil(math.log(abs(value + 1), 2)) + 1
            digits = len(bin(value).replace(_PREFIX, "")) + 1
        else:  # negative
            # less precise: digits = math.ceil(math.log(abs(value), 2)) + 1
            digits = len(bin(value + 1).replace(_PREFIX, ""))
        # digits = number of bits required to represent this
        # negative number in twos-complement
        if length == -1:
            length = digits
        if length < digits:
            raise OverflowError(f"Argument {value} does not fit into {length} digits.")
        if value == 0:
            result = "0" * length
        elif value < 0:  # negative
            value = value - (1 << length)  # compute negative value
            result = bin(value & ((2 ** length) - 1)).replace(_PREFIX, "")
            result = "1" * (len(result) - length) + result
        else:  # positive
            result = "0" + bin(value).replace(_PREFIX, "")
            result = "0" * (length - len(result)) + result
        if length != -1:
            le = len(result)
            if le > length:
                raise OverflowError
            result = result[0] * (length - le) + result
        return result

    def _frac2twoscomp(
        value: float, length: int = -1, rel_tol: float = _BINARY_RELATIVE_TOLERANCE
    ) -> str:
        """Computes the two's complement of the fractional part (mantissa) of a float.

        This is a utility function.
        Users should use the constructor TwosComplement(f-int(f)) instead.

        The returned string always has one integer digit, followed by a decimal point.
        The integer digit indicates the sign.
        The decimal part consists of at least 1 bit.
        Hence, the shortest values are 0.0, 0.1, 1.0, and 1.1.
        This function has rounding errors as it deals with floats.
        _frac2twoscomp(+1.0000000000000000000000000000000001) returns '0.0'.
        _frac2twoscomp(-0.9999999999999999999999999999999999) returns '1.0'
        because it is rounded to -1.
        Use the method _fraction2twoscomp() using Fractions to avoid rounding
        errors.

        Examples:
        * For -3.5 it computes the twos-complement of -0.5.
            So, _frac2twoscomp(-3.5) returns '1.1'.
        * _frac2twoscomp(+3.5) returns '0.1'.
        * _frac2twoscomp(-3.375) returns '1.101'.
        * _frac2twoscomp(+3.375) returns '1.11'.

        Parameters:
        value (float): number whose mantissa will be converted to twos-complement.
        length (int): desired length of resulting string. If -1, result is neither
            prefixed nor truncated. A shorter length will truncate the mantissa,
            losing precision. A larger length will prefix the decimal digits
            with additional sign bits to produce a resulting string of specified
            lenght.
            Example of length 4 is '01.1'.
        rel_tol (float): relative tolerance that influences precision further.
            A bigger tolerance leads to a possibly less precise result.
            A smaller tolerance leads to a possibly more precise result.

        Returns:
        str: twos-complement string of the mantissa
        """
        if length < 1 and length != -1:
            raise ValueError(f"Argument {length} has be greater than 0, or default -1.")
        fp, ip = math.modf(value)
        afp = abs(fp)
        result = ""
        i = 1
        if value == 0:
            result = "0.0"
        elif fp == 0:
            result = "0.0" if ip >= 0 else "1.0"
        elif fp >= 0:  # Positive
            rest = 0.0
            while not (math.isclose(rest, fp, rel_tol=rel_tol)):
                b = 2 ** -i
                if b + rest <= fp:
                    result += "1"
                    rest += b
                else:
                    result += "0"
                i += 1
            result = "0." + result
        else:  # Negative
            rest = 1.0
            while not (math.isclose(rest, afp, rel_tol=rel_tol)):
                b = 2 ** -i
                if rest - b < afp:
                    result += "0"
                else:
                    rest -= b
                    result += "1"
                i += 1
            result = "0" if result == "" else result
            result = "1." + result
        if length == -1:
            result = result
        elif length > len(result):  # fill
            sign = result[0]
            result = sign * (length - len(result)) + result
        elif length < len(result):  # truncate
            result = result[0:length]
        return result

    def _float2twoscomp(
        value: float,
        length: int = -1,
        rel_tol: float = _BINARY_RELATIVE_TOLERANCE,
        warn_on_float: bool = False,
    ) -> str:
        """Converts float to two's-complement.

        This is a utility function.
        Users should use the constructor TwosComplement(value) instead.

        If maximum precision is desired, use Fractions instead of floats.

        Parameters:
        value (float): number to be converted to twos-complement.
        length (int): desired length of resulting string. If -1, result is neither
            prefixed nor truncated. If length is too short to fit value, an
            exception is raised. A larger length will prefix the decimal digits
            with additional sign bits to produce a resulting string of specified
            lenght.
            Example of length 4 is '01.1'.
        rel_tol (float): relative tolerance that influences precision further.
            A bigger tolerance leads to a possibly less precise result.
            A smaller tolerance leads to a possibly more precise result.

        Returns:
        str: twos-complement string of value
        """
        if math.isnan(value) or math.isinf(value):
            raise ArithmeticError(
                f"ArithmeticError: argument {value} is NaN or infinity."
            )
        global _BINARY_WARNED_ABOUT_FLOAT
        if value != int(value):  # not an integer
            if not _BINARY_WARNED_ABOUT_FLOAT:
                _BINARY_WARNED_ABOUT_FLOAT = True
                if warn_on_float:
                    print(
                        "Warning: possible loss of precision "
                        "due to mixing floats and TwosComplement. "
                        "Consider using Fraction instead of float."
                    )
        # more precise to use Fraction than float
        return TwosComplement._fraction2twoscomp(Fraction(value), length)

    def _float2twoscomp_implementation_with_less_precision(
        value: float, length: int = -1, rel_tol: float = _BINARY_RELATIVE_TOLERANCE
    ) -> str:
        """Converts float to two's-complement.

        This is a utility function.
        Users should use the constructor TwosComplement(value) instead.

        Does the same as _float2twoscomp() but with possibly less precision.
        """
        if math.isnan(value) or math.isinf(value):
            raise ArithmeticError(
                f"ArithmeticError: argument {value} is NaN or infinity."
            )
        fp, ip = math.modf(value)
        if fp == 0:
            return TwosComplement._int2twoscomp(int(ip), length)
        if fp < 0:  # negative
            intresult = TwosComplement._int2twoscomp(math.floor(value), -1)
        else:
            intresult = TwosComplement._int2twoscomp(int(ip), -1)
        if intresult == "0" and fp < 0:  # -0.x
            intresult = "1"
        fracresult = TwosComplement._frac2twoscomp(fp, -1)
        result = intresult + "." + fracresult[2:]
        if length < len(result) and length != -1:
            raise OverflowError(f"Argument {value} does not fit into {length} digits.")
        if length != -1:
            sign = result[0]
            result = sign * (length - len(result)) + result
        return result

    def _fraction2twoscomp(
        value: Fraction,
        length: int = -1,
        ndigits: int = _BINARY_PRECISION,
    ) -> str:
        """Converts fraction to two's-complement.

        This is a utility function.
        Users should use the constructor TwosComplement(value) instead.

        First parameter 'ndigits', then secundarily parameter 'length' will
        be applied to result. 'ndigits' influences digits after decimal point,
        'length' influences digits (sign bits) before the decimal point.

        Parameters:
        value (Fraction): number to be converted to twos-complement.
        length (int): desired length of resulting string. If -1, result is neither
            prefixed nor truncated. If length is too short to fit value, an
            exception is raised. A larger length will prefix the decimal digits
            with additional sign bits to produce a resulting string of specified
            lenght.
            Example of length 4 is '01.1'.
        ndigits (int): desired digits after decimal point.

        Returns:
        str: twos-complement string of value
        """
        if value.denominator == 1:
            result = TwosComplement._int2twoscomp(value.numerator, length=length)
            return result
        # uses Fractions for computation for more precision
        if value.numerator >= 0:  # positive
            # alternative implementation: just call function in Binary:
            # result = Binary.fraction_to_string(value, ndigits, simplify=True)
            # But to keep TwosComplement independent of Binary it was redone
            # here.
            result = bin(int(value)).replace(_PREFIX, "")
            fraction_number = value - int(value)
            if fraction_number > 0:
                result += "."
                rest = Fraction(0)
                ii = 1
                while ii < ndigits + 1:
                    b = Fraction(1, 2 ** ii)
                    if rest + b < fraction_number:
                        result += "1"
                        rest += b
                    elif rest + b > fraction_number:
                        result += "0"
                    elif rest + b == fraction_number:
                        result += "1"
                        break
                    ii += 1
            if result[0] != "0":
                result = "0" + result
        else:  # negative
            absvalue = -value
            digits = len(bin(int(absvalue)).replace(_PREFIX, "")) + 1
            resultintpart = 2 ** digits - math.ceil(absvalue)
            result = bin(resultintpart).replace(_PREFIX, "")
            # remove duplicate 1s on left
            result = "1" + result.lstrip("1")
            fraction_number = absvalue - int(absvalue)
            if fraction_number > 0:
                result += "."
                rest = Fraction(1)
                ii = 1
                while ii < ndigits + 1:
                    b = Fraction(1, 2 ** ii)
                    if rest - b < fraction_number:
                        result += "0"
                    elif rest - b > fraction_number:
                        rest -= b
                        result += "1"
                    elif rest - b == fraction_number:
                        result += "1"
                        break
                    ii += 1
        # remove 0s on right
        if "." in result:
            result = result.rstrip("0")
        if length != -1:
            le = len(result)
            if le > length:
                raise OverflowError
            result = result[0] * (length - le) + result
        return result

    def _str2twoscomp(value: str, length: int = -1, simplify: bool = True) -> str:
        """Converts two's-complement string to possibly refined two's-complement
        string.

        This is a utility function.
        Users should use the constructor TwosComplement(value) instead.

        A possible simplification will be done before a possible length
        extension.

        Parameters:
        value (str): twos-complement string to be converted to twos-complement.
        length (int): desired length of resulting string. If -1, result is
            not prefixed. If length is too short to fit value, an
            exception is raised. A larger length will prefix the decimal digits
            with additional sign bits to produce a resulting string of specified
            length.
            Example of length 4 is '01.1'.
        simplify (bool): If True, result will be simplified. If False, result
            will be left unchanged as much as possible.

        Returns:
        str: twos-complement string of value
        """
        if TwosComplement.istwoscomplement(value):
            if length < len(value) and length != -1:
                raise OverflowError(
                    f"Argument {value} does not fit into {length} digits."
                )
            if simplify:
                value = TwosComplement.simplify(value)
            if length != -1:
                sign = value[0]
                value = sign * (length - len(value)) + value
            return value
        else:
            raise ValueError(f"Argument {value} not a valid twos-complement.")

    def istwoscomplement(value: str) -> bool:
        """Determine if string content has a valid two's-complement syntax.

        Parameters:
        value (str): string to check

        Returns:
        bool: True if value is a valid twos-complement. False otherwise.
        """
        try:
            TwosComplement.components(value)
            # don't catch TypeError
        except ValueError:
            return False
        return True

    def components(
        self_value: Union[str, TwosComplement], simplify: bool = True
    ) -> tuple:
        """Returns sign, integer part (indicates sign in first bit), fractional
        part, and exponent as a tuple of int, str, str, and int.

        This is both a function and a method.

        Examples:
        Here are some examples for `simplify` being False.
        * For 3.25*4, input '11.01e2' returns (1, '11', '01', 2).
        * For 0, input '0' returns (0, '0', '', 0).
        * For -1, input '1' returns (1, '1', '', 0).
        * For 1, input '01' returns (0, '01', '', 0).
        * For -0.5, input 1.1 returns (1, '1', '1', 0).
        * For neg. number, input 101.010e-4 returns (1, '101', '010', -4).
        * For pos. number, input 0101.010e-4 returns (0, '0101', '010', -4).
        * For input 111101.010000e-4 returns (1, '111101', '010000', -4).

        Here are some examples for `simplify` being True.
        * For -3.25*4, input '1111101.11e2' returns (1, '101', '11', 2).
        * For input '11111111.0111e4' returns (1, '1', '0111', 4).
        * For 0, input '0' returns (0, '0', '', 0).
        * For -1, input '1' returns (1, '1', '', 0).
        * For 1, input '01' returns (0, '01', '', 0).
        * For -0.5, input 1.1 returns (1, '1', '1', 0).
        * For neg. number, input 111101.0100e-4 returns (1, '101', '01', -4).
        * For pos. number, input 0000101.0100e-4 returns (0, '0101', '01', -4).

        Parameters:
        self_value (str, TwosComplement): twos-complement from which to
            derive the components.
        simplify (bool): If True simplify output by performing cleanup and
            removing unnecessary digits.
            If False, then produce exact as-is twos-complement components
            without any cleanup or simplifications.

        Returns:
        tuple: tuple of sign (int), integer part (str) including a sign bit,
            fractional part (str), exponent (int). Sign is int 1 for negative (-).
            Sign is int 0 for positive (+).
        """
        if not isinstance(self_value, str) and not isinstance(
            self_value, TwosComplement
        ):
            raise TypeError(
                f"Argument {self_value} must be of type str or TwosComplement."
            )

        # crud for parsing strings
        #
        # Regular expression used for parsing twos-complement strings.  Additional
        # comments:
        #
        # 1. Uncomment the two '\s*' lines to allow leading and/or trailing
        # whitespace.  But note that the specification disallows whitespace in
        # a numeric string.
        #
        # 2. For finite numbers the body of the
        # number before the optional exponent must have
        # at least one binary digit.  The
        # lookahead expression '(?=[01])' checks this.

        _parser = re.compile(
            r"""        # A twoscomplement string consists of:
            \s*
            (
                (?=[01])                 # lookahead: a number (with at least one digit)
                (?P<int>[01]+)           # non-empty integer part with at least 1 digit
                (\.(?P<frac>[01]*))?     # followed by an optional fractional part
                (E(?P<exp>[-+]?\d+))?    # followed by an optional exponent
            )
            \s*
            \Z
        """,
            re.VERBOSE | re.IGNORECASE,
        ).match

        m = _parser(self_value)
        if m is None:
            raise ValueError(
                f"Invalid literal: {self_value}. "
                + "Not a valid twos-complement string."
            )
        intpart = m.group("int")
        fracpart = m.group("frac") or ""
        exp = int(m.group("exp") or "0")
        # according to parser int cannot be empty
        if intpart[0] == "0":
            sign = 0  # "+"
        else:
            sign = 1  # "-"
        if simplify:
            fracpart = fracpart.rstrip("0")
            if sign:  # neg
                intpart = "1" + intpart.lstrip("1")
            else:  # pos
                intpart = "0" + intpart.lstrip("0")
        return (sign, intpart, fracpart, exp)

    def simplify(self_value: Union[str, TwosComplement]) -> Union[str, TwosComplement]:
        """Simplifies two's-complement strings.

        This is a utility function as well as a method.

        Removes leading duplicate 0s or 1s to the left of decimal point.
        Removes trailing duplicate 0s after decimal point.
        Removes unnecessary exponent 0.

        Parameters:
        self_value (str, TwosComplement): twos-complement string to be simplified

        Returns:
        Union[str, TwosComplement]: returns simplied twos-complement. Return type is
            str if input was of class str, return type is
            TwosComplement if input was of class TwosComplement.
        """
        if not isinstance(self_value, str) and not isinstance(
            self_value, TwosComplement
        ):
            raise TypeError(
                f"Argument {self_value} must be of type str or TwosComplement."
            )
        value = str(self_value)
        sign, intpart, fracpart, exp = TwosComplement.components(value)
        if len(intpart) and intpart[0] == "1":
            # remove duplicate 1s on left
            intpart = "1" + intpart.lstrip("1")
        elif len(intpart) and intpart[0] == "0":
            # remove duplicate 0s on left
            intpart = "0" + intpart.lstrip("0")
        # remove duplicate 0s to right of decimal point
        fracpart = fracpart.rstrip("0")
        if fracpart != "":
            fracpart = "." + fracpart
        exppart = "" if exp == 0 else _EXP + str(exp)
        result = intpart + fracpart + exppart
        if isinstance(self_value, TwosComplement):
            result = TwosComplement(result)
        return result

    def to_fraction(self_value: Union[str, TwosComplement]) -> Fraction:
        """Converts two's-complement to Fraction.

        This is a utility function as well as a method.

        Do *NOT* use it on binary fractions strings!

        Parameters:
        self_value (str, TwosComplement): twos-complement string to be
            converted to Fraction

        Returns:
        Fraction: returned value as a Fraction
        """
        if not isinstance(self_value, str) and not isinstance(
            self_value, TwosComplement
        ):
            raise TypeError(
                f"Argument {self_value} must be of type str or TwosComplement."
            )
        value = str(self_value)
        noman = TwosComplement.to_no_mantissa(value)
        sign, intpart, fracpart, exp = TwosComplement.components(noman)
        intpartlen = len(intpart)
        if value[0] == "0":  # positive twos-complement
            intpartnosign = intpart.lstrip("0")
            num = int(intpart, 2)
        else:
            num = -(2 ** intpartlen - int(intpart, 2))
        if exp < 0:
            denom = 2 ** (-exp)
        else:
            num = num * 2 ** exp
            denom = 1
        result = Fraction(num, denom)
        return result

    def to_float(self_value: Union[str, TwosComplement]) -> float:
        """Converts two's-complement to float.

        This is a utility function as well as a method.

        Do *NOT* use it on binary fractions strings!

        Parameters:
        self_value (str, TwosComplement): twos-complement string to be
            converted to float

        Returns:
        float: returned value as a float
        """
        return float(TwosComplement.to_fraction(self_value))

    def to_no_mantissa(
        self_value: Union[str, TwosComplement], length: int = -1
    ) -> Union[str, TwosComplement]:
        """Adjusts exponent such that there is no fractional part, i.e. no mantissa.

        This is a utility function as well as a method.

        Do *NOT* use it on binary fractions strings!

        The value does not change. The precision does not change.
        Only the integer part and the exponent change such that the
        same value is represented but without mantissa.

        Examples:
        * converts 1.1 to 11e-1
        * converts 01.11 to 0111e-2

        Parameters:
        self_value (str, TwosComplement): twos-complement string to be
            converted to representation without mantissa
        length (int): desired length of resulting string. If -1, result is
            not prefixed. If length is too short to fit value, an
            exception is raised. A larger length will prefix the decimal digits
            with additional sign bits to produce a resulting string of specified
            length.
            Example of length 4 is '01.1'.

        Returns:
        Union[str, TwosComplement]: returns twos-complement without mantissa.
            Return type is
            str if input was of class str, return type is
            TwosComplement if input was of class TwosComplement.
        """
        if not isinstance(self_value, str) and not isinstance(
            self_value, TwosComplement
        ):
            raise TypeError(
                f"Argument {self_value} must be of type str or TwosComplement."
            )
        value = str(self_value)
        sign, intpart, fracpart, exp = TwosComplement.components(value)
        fracpartlen = len(fracpart)
        exp -= fracpartlen
        intpart += fracpart
        result = intpart + _EXP + str(exp) if exp else intpart
        if isinstance(self_value, TwosComplement):
            result = TwosComplement(result)
        if length != -1:
            le = len(result)
            # NOTE: this function does not implement shortening or truncating
            if le > length:
                raise OverflowError
            result = result[0] * (length - le) + result
        return result

    def to_no_exponent(
        self_value: Union[str, TwosComplement], length: int = -1, simplify: bool = True
    ) -> Union[str, TwosComplement]:
        """Remove exponent part from twos-complement string.

        This is a utility function as well as a method.

        Do *NOT* use it on binary fractions strings!

        The value does not change. The precision does not change.
        Only the integer part and the mantissa change such that the
        same value is represented but without exponent.

        Any possible simplification will be done before any possible length adjustment.

        It removes the exponent, and returns a fully "decimal" twos-complement string.

        Examples:
        * converts '011.01e-2' to '0.1101'.
        * converts 0.25, '0.1e-1' to '0.01'.
        * converts -0.125, '1.111e0' to '1.111'.
        * converts -0.25, '1.11e0' to '1.11'.
        * converts -0.5, '1.1e0' to '1.1'.
        * converts -1.0, '1.e0' to '1'.
        * converts -2.0, '1.e1' to '10'.
        * converts -3.0, '1.01e2' to '101'.
        * converts -1.5, '1.01e1' to '10.1'.
        * converts -2.5, '1.011e2' to '101.1'.

        Parameters:
        self_value (str, TwosComplement): twos-complement string to be
            converted to representation without exponent
        length (int): desired length of resulting string. If -1, result is
            not prefixed. If length is too short to fit value, an
            exception is raised. A larger length will prefix the decimal digits
            with additional sign bits to produce a resulting string of specified
            length.
            Example of length 4 is '01.1'.
        simplify (bool): If True simplify output by performing cleanup and
            removing unnecessary digits.
            If False, then produce exact as-is twos-complement components
            without any cleanup or simplifications.

        Returns:
        Union[str, TwosComplement]: returns twos-complement without exponent.
            Return type is
            str if input was of class str, return type is
            TwosComplement if input was of class TwosComplement.
        """
        if not isinstance(self_value, str) and not isinstance(
            self_value, TwosComplement
        ):
            raise TypeError(
                f"Argument {self_value} must be of type str or TwosComplement."
            )
        if length <= 0 and length != -1:
            raise ValueError(f"Argumet {length} must be bigger than 0 or -1")
        value = str(self_value)
        if _NAN.lower() in value.lower() or _INF.lower() in value.lower():
            raise ArithmeticError(
                f"ArithmeticError: argument {self} is NaN or infinity."
            )
        if len(value) == 0 or _PREFIX in value or value[0] == "-":
            raise ValueError(
                f"Argument {value} must not contain prefix 0b or negative sign -. "
                "It should be two's complement string such as 10.1e-23."
            )
        sign, intpart, fracpart, exp = TwosComplement.components(value, simplify)
        if exp == 0:
            result = intpart + "." + fracpart
        elif exp > 0:
            l = len(fracpart[:exp])
            result = intpart + (
                fracpart[:exp] if l > exp else fracpart[:exp] + "0" * (exp - l)
            )
            result += "." + fracpart[exp:]
        elif exp < 0:
            l = len(intpart)
            aexp = abs(exp)
            signdigit = "1" if sign else "0"
            if l > aexp:
                result = intpart[: (l - aexp)] + "." + intpart[(l - aexp) :] + fracpart
            else:  # l <= aexp
                result = (
                    intpart[0]
                    + "."
                    + signdigit * (aexp - l + 1)
                    + intpart[1:]
                    + fracpart
                )
        if not "." in value:
            result = result.rstrip(".")
        if _EXP in value:
            result = result.rstrip(".")
        if simplify:
            # result = "1" + result.lstrip("1")
            # result = result.rstrip("0")
            # result = result.rstrip(".")
            result = TwosComplement.simplify(result)

        if length != -1:
            l = len(result)
            if l > length:
                raise OverflowError
            i = length - l
            result = result[: l - i] if i < 0 else result[0] * i + result
        if isinstance(self_value, TwosComplement):
            result = TwosComplement(result)
        return result

    def invert(
        self_value: Union[str, TwosComplement], simplify: bool = True
    ) -> Union[str, TwosComplement]:
        """Inverts (bitwise negates) string that is in two's-complement format.

        This is a utility function as well as a method.

        Do *NOT* use this function on binary fractions strings.

        It negates (flips) every bit in the given twos-complement string.

        Using 'simplify' can lead to a representation that drops
        leading and/or trailing bits for simplification. If no bits
        should be dropped by `invert`, set `simplify` to False.

        `invert` will try to maintain the representation of the input.
        If the input has an exponent, the output will have an exponent.
        If the input has no exponent, the output will have no exponent.


        Examples:
        * invert('01') returns '10' (like decimal: ~1==-2)
        * invert('0') returns 1  (like decimal: ~0==-1)
        * invert('1') returns 0  (like decimal: ~-1==0)
        * invert('10') returns '01'  (like decimal: ~-2==1)
        * invert('101010') returns '010101'
        * invert('0101010') returns '1010101'
        * invert('0101010e-34') returns '1010101e-34'
        * invert('1010101e-34') returns '0101010e-34'
        * invert(invert('0101010e-34')) returns '0101010e-34'
        * invert('010101e34') returns '101010.1111111111111111111111111111111111e34'
        * invert('101010e34') returns '010101.1111111111111111111111111111111111e34'
        * invert(invert('101010e34')) returns '101010e34'
        * invert(invert(n)) == n for all valid n
        * invert('1..1') raises exception, 2 decimal points
        * invert('34') raises exception, not binary
        * invert('1ee2') raises exception, two exponential signs
        * invert('1e') raises exception, missing exponent digit

        Parameters:
        self_value (str, TwosComplement): twos-complement string to be
            inverted
        simplify (bool): If False, try to change the string as little as
            possible in format.
            If True, returned string will also be simplified
            by removing unnecessary digits.

        Returns:
        Union[str, TwosComplement]: returns the bitwise negated string,
            a twos-complement formated string. The
            return type is
            str if input was of class str, return type is
            TwosComplement if input was of class TwosComplement.
        """
        if not isinstance(self_value, str) and not isinstance(
            self_value, TwosComplement
        ):
            raise TypeError(
                f"Argument {self_value} must be of type str or TwosComplement."
            )
        value = str(self_value)
        if _NAN.lower() in value.lower() or _INF.lower() in value.lower():
            raise ArithmeticError(
                f"ArithmeticError: argument {value} is NaN or infinity."
            )
        if not TwosComplement.istwoscomplement(value):
            raise ValueError(f"Argument {value} not a valid twos-complement literal.")

        if _EXP in value:
            sign, intpart, fracpart, exp = TwosComplement.components(value, simplify)
            if exp > 0:
                # # Alternative implementation A: using TwosComplement.to_no_exponent()
                # # simplify = False to not miss any bits on the right
                # value = TwosComplement.to_no_exponent(value, simplify=False)
                # Alternative implementation B: just adding sufficient 0s after decimal point
                fl = len(fracpart)
                fracpart += "0" * (exp - fl)  # if negative, no 0s will be added
                value = intpart + "." + fracpart + _EXP + str(exp)
                # assert len(fracpart) >= exp
        result = ""
        for i in value:
            if i == "0":
                result += "1"
            elif i == "1":
                result += "0"
            elif i == ".":
                result += "."
            elif i.lower() == _EXP:
                result += _EXP + str(exp)
                break
            else:
                raise ValueError(f"Unexpected literal {i} in {value}.")
        if simplify:
            result = TwosComplement.simplify(result)
        if isinstance(self_value, TwosComplement):
            result = TwosComplement(result)
        return result


##########################################################################
# CLASS BINARY
##########################################################################


class Binary(object):
    """Floating point class for binary fractions and arithmetic.

    The class Binary implements a basic representation and basic operations
    of binary fractions and binary floats:
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

    Valid binary fraction of class 'Binary' are:
    0, 1, 10, 0.0, 1.1, 1., 0.1e+34, -1, -10, -0.0, -1.1, -1., -0.1e+34,
    11101.e-56, 101.01e78. 000011.1000e0 is valid and is the same as 11.1.
    Along the same line, 111101.0100000e-000 is valid and is the same as 111101.01.

    Invalid binary fraction of class 'Binary' are: --1 (multiple minus),
    *1 (asterisk),
    12 (2 is not a binary digit),
    1.2.3 (2 decimal points),
    1e (missing exponent number),
    1e-1.1 (decimal point in exponent).

    If you are curious about floating point binary fractions, have a look at:
    - https://en.wikipedia.org/wiki/Computer_number_format#Representing_fractions_in_binary
    - https://www.electronics-tutorials.ws/binary/binary-fractions.html
    - https://ryanstutorials.net/binary-tutorial/binary-floating-point.php
    - https://planetcalc.com/862/

    """

    def __new__(
        cls,
        value: Union[int, float, str, Fraction, TwosComplement] = "0",
        simplify: bool = True,
        warn_on_float: bool = False,
    ) -> Binary:
        """Constructor.

        Use __new__ and not __init__ because Binary objects are immutable.
        Allows string, float, integer, Fraction and TwosComplement
        as input for constructor.
        With 'simplify' being False, if an instance is contructed from a
        string, attention is paid to *not*
        modify the string or to modify it as little as possible.
        For example, if given '1e1' it will remain as '1e1', it will not change it
        to '1'. Same with '1000', it will not change it to '1e4'. We try to keep then
        string representation as close to the original as possible.
        With 'simplify' set to True, simplifications will be performed, e.g.
        '+01e0' will be turned into '1'.

        Examples:
        * Binary(123)
        * Binary(123.456)
        * Binary(Fraction(179, 1024))
        * Binary('-101.0101e-45')
        * Binary(TwosComplement(Fraction(179, 1024)))

        Parameters:
        value (int, float, str): value of number
        simplify (bool): If True try to simplify string representation.
            If False, try to leave the string representation as much as is.
        warn_on_float (bool): if True print a warning statement to stdout to
            warn about possible loss in precision in case of conversion from
            float to Binary.
            If False, print no warning to stdout.

        Returns:
        Binary: created immutable instance
        """
        # crud for parsing strings
        #
        # Regular expression used for parsing numeric strings.  Additional
        # comments:
        #
        # 1. Uncomment the two '\s*' lines to allow leading and/or trailing
        # whitespace.  But note that the specification disallows whitespace in
        # a numeric string.
        #
        # 2. For finite numbers (not infinities and NaNs) the body of the
        # number between the optional sign and the optional exponent must have
        # at least one Binary digit, possibly after the Binary point.  The
        # lookahead expression '(?=\d|\.\d)' checks this.

        _parser = re.compile(
            r"""        # A numeric string consists of:
            \s*
            (?P<sign>[-+])?              # an optional sign, followed by either...
            (
                (?=\d|\.[01])              # ...a number (with at least one digit)
                (?P<int>[01]*)             # having a (possibly empty) integer part
                (\.(?P<frac>[01]*))?       # followed by an optional fractional part
                (E(?P<exp>[-+]?\d+))?    # followed by an optional exponent, or...
            |
                Inf(inity)?              # ...an infinity, or...
            |
                (?P<signal>s)?           # ...an (optionally signaling)
                NaN                      # NaN
                (?P<diag>\d*)            # with (possibly empty) diagnostic info.
            )
            \s*
            \Z
        """,
            re.VERBOSE | re.IGNORECASE,
        ).match

        global _BINARY_WARNED_ABOUT_FLOAT
        self = super(Binary, cls).__new__(cls)
        self._is_special = False
        self._warn_on_float = warn_on_float
        self._fraction = Fraction()
        # indicate if operations were lossless
        # if True it was lossless,
        # if False it might be lossy (but it could also be lossless)
        self._is_lossless = True

        # From a TwosComplement string
        # important that this isinstance check is BEFORE isinstance(str) check!
        if isinstance(value, TwosComplement):
            resultbin = Binary(TwosComplement.to_fraction(value))
            if simplify:
                return resultbin
            else:  # not simplify
                sign, fracpart, intpart, exp = TwosComplement.components(
                    value, simplify
                )
                resultbin = resultbin.to_exponent(exp)
                if _EXP in value and exp == 0:
                    resultstr: str = resultbin._value
                    if _EXP not in resultstr:  # check just in case
                        resultstr += _EXP + "0"  # keep it as alike as possible
                    return Binary(resultstr, simplify=False)
                else:
                    return resultbin

        # From a string
        # REs insist on real strings, so we can too.
        if isinstance(value, str):
            value = value.strip().replace("_", "")
            if len(value) >= 3:
                if value[0:3] == ("-" + _PREFIX):
                    value = "-" + value[3:]
                elif value[0:2] == _PREFIX:
                    value = value[2:]
            m = _parser(value)
            if m is None:
                raise ValueError(f"Invalid literal for Binary: {value}.")

            if m.group("sign") == "-":
                sign = "-"
                self._sign = 1
            else:
                sign = ""
                self._sign = 0
            intpart = m.group("int")
            if intpart is not None:
                # finite number
                if not simplify:
                    self._value = value  # leave as is
                else:
                    fracpart = m.group("frac") or ""
                    fracpart = fracpart.rstrip("0")
                    exp = int(m.group("exp") or "0")
                    if exp != 0:
                        # # version A: this normalizes to remove decimal point
                        # intpart = str(int(intpart + fracpart))
                        # exppart = str(exp - len(fracpart))
                        # self._value = sign + intpart + _EXP + exppart
                        # version B: this leaves string as much as is
                        if fracpart == "":
                            self._value = sign + intpart + _EXP + str(exp)
                        else:
                            self._value = (
                                sign + intpart + "." + fracpart + _EXP + str(exp)
                            )
                    else:
                        if fracpart == "":
                            self._value = sign + intpart
                        else:
                            self._value = sign + intpart + "." + fracpart
            else:
                self._is_special = True
                diag = m.group("diag")
                if diag is not None:
                    # NaN
                    if m.group("signal"):
                        self._value = _NAN  # "NaN", N, ignore signal
                    else:
                        self._value = _NAN  # "NaN", n, ignore signal
                else:
                    # infinity
                    self._value = sign + "Infinity"  # F
            if not self._is_special:
                self._fraction = Binary.to_fraction(self._value)
            return self

        # From a tuple/list conversion (possibly from as_tuple())
        if isinstance(value, (list, tuple)):
            if len(value) != 3:
                raise ValueError(
                    "Invalid tuple size in creation of Decimal "
                    "from list or tuple.  The list or tuple "
                    "should have exactly three elements."
                )
            # process sign.  The isinstance test rejects floats
            if not (isinstance(value[0], int) and value[0] in (0, 1)):
                raise ValueError(
                    "Invalid sign.  The first value in the tuple "
                    "should be an integer; either 0 for a "
                    "positive number or 1 for a negative number."
                )
            if value[0]:
                self._sign = 1
                sign = "-"
            else:
                self._sign = 0
                sign = ""
            if value[2] == "F":
                # infinity: value[1] is ignored
                self._value = "Infinity"
                self._is_special = True
            else:
                # process and validate the digits in value[1]
                digits = []
                for digit in value[1]:
                    if isinstance(digit, int) and 0 <= digit <= 1:
                        # skip leading zeros
                        if digits or digit != 0:
                            digits.append(digit)
                    else:
                        raise ValueError(
                            "The second value in the tuple must "
                            "be composed of integers in the range "
                            "0 through 1."
                        )
                if value[2] in ("n", "N"):
                    # NaN: digits form the diagnostic
                    self._value = _NAN  # "NaN"
                    self._is_special = True
                elif isinstance(value[2], int):
                    # finite number: digits give the coefficient
                    integer = "".join(map(str, digits or [0]))
                    self._value = sign + integer + _EXP + str(value[2])
                else:
                    raise ValueError(
                        "The third value in the tuple must "
                        "be an integer, or one of the "
                        "strings 'F', 'n', 'N'."
                    )
            if not self._is_special:
                self._fraction = Binary.to_fraction(self._value)
            return self

        # From another Binary
        if isinstance(value, Binary):
            self._sign = value._sign
            self._value = value._value
            self._fraction = value._fraction
            self._is_lossless = value._is_lossless
            self._is_special = value._is_special
            self._warn_on_float = value._warn_on_float
            return self

        if isinstance(value, Fraction):
            self._fraction = value
            self._value = Binary.fraction_to_string(value)
            self._sign = 1 if value < 0 else 0
            return self

        # From an integer
        if isinstance(value, int):
            self._fraction = Fraction(value)
            # self._value = Binary.fraction_to_string(self._value)
            self._value = bin(value).replace(_PREFIX, "")
            self._sign = 1 if value < 0 else 0
            return self

        # from a float
        if isinstance(value, float):
            if math.isnan(value):
                return Binary(_NAN)
            if value == float("inf"):
                return Binary(_INF)
            if value == float("-inf"):
                return Binary(_NINF)
            if value != int(value):  # not an integer
                if not _BINARY_WARNED_ABOUT_FLOAT:
                    _BINARY_WARNED_ABOUT_FLOAT = True
                    if self._warn_on_float:
                        print(
                            "Warning: possible loss of precision "
                            "due to mixing floats and Binary. "
                            "Consider using Fraction instead of float."
                        )
            if value != int(value):
                self._is_lossless = False
            self._fraction = Fraction(value)
            self._value = Binary.fraction_to_string(value)
            self._sign = 1 if value < 0 else 0
            return self

        # any other types
        raise TypeError(f"Cannot convert {value} to Binary")

    def to_float(value: str) -> Union[float, int]:
        """Convert from Binary string to float or integer.

        This is a utility function that converts
        a Binary string to a float or integer.

        This might lead to loss of precision due to possible float conversion.
        If you need maximum precision consider working with `Fractions.`

        Parameters:
        value (str): binary string representation of number

        Returns:
        Union[float, int]: number as float or integer
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # Alternative implementation:
        # could also use inverse of method float.hex()
        if value.lower() == "inf" or value.lower() == "infinity":
            return float("inf")
        elif value.lower() == "-inf" or value.lower() == "-infinity":
            return float("-inf")
        elif value.lower() == "nan" or value.lower() == "-nan":
            return float("nan")
        value = Binary.to_no_exponent(value)
        li = value.split(".")
        intpart = li[0]
        result = int(intpart, 2)
        if result < 0:
            sign = -1
        else:
            sign = 1
        if len(li) == 1:
            fracpart = ""
            return result  # an integer
        else:
            fracpart = li[1]
        le = len(fracpart)
        for i in range(le):
            if fracpart[i] == "1":
                result += (2 ** -(i + 1)) * sign
        return result  # float

    def from_float(value: float, rel_tol: float = _BINARY_RELATIVE_TOLERANCE) -> str:
        """Convert from float to Binary string of type string.

        This is a utility function. It converts from
        float to Binary.

        This might lead to loss of precision due to possible float conversion.
        If you need maximum precision consider working with `Fractions.`

        Parameters:
        value (float): value of number
        rel_tol (float): relative tolerance to know when to stop converting.
            A smaller rel_tol leads to more precision.

        Returns:
        str: string representation of Binary string
        """
        # alternative implementation: could also use method float.hex()
        if not isinstance(value, float):
            raise TypeError(f"Argument {value} must be of type float.")
        if value == float("inf"):
            return "inf"  # lowercase like in float class
        elif value == float("-inf"):
            return "-inf"  # lowercase like in float class
        elif math.isnan(value):  # NOT CORRECT: value == float("-nan"):
            return "nan"  # lowercase like in float class
        if value >= 0:
            sign = ""
        else:
            sign = "-"
        value = abs(value)
        integer = int(value)
        intpart = bin(integer).replace(_PREFIX, "")

        fracpart = ""
        rest = 0.0
        i = 1
        fraction = value - integer
        while not (math.isclose(rest, fraction, rel_tol=rel_tol)):
            b = 2 ** -i
            if b + rest <= fraction:
                fracpart += "1"
                rest += b
            else:
                fracpart += "0"
            i += 1
        result = sign + _PREFIX + intpart + "." + fracpart
        return Binary.simplify(result, add_prefix=True)

    def to_no_exponent(
        self_value: Union[Binary, str],
        length: int = -1,
        simplify: bool = True,
        add_prefix: bool = False,
    ) -> Union[Binary, str]:
        """Normalizes string representation. Removes exponent part.

        This is both a method as well as a utility function.

        Do *NOT* use it on Twos-complement strings!

        It removes the exponent, and returns a fully "decimal" binary string.

        Any possible simplification will be done before any possible length adjustment.

        Examples:
        * converts '11.01e-2' to '0.1101'

        Parameters:
        self_value (Binary, str): a Binary instance or
            a binary string representation of number
        length (int): desired length of resulting string. If -1, result is
            not prefixed. If length is too short to fit value, an
            exception is raised. A larger length will prefix the decimal digits
            with additional sign bits to produce a resulting string of specified
            length.
            Example of length 4 is '01.1'.
        simplify (bool): If True try to simplify string representation.
            If False, try to leave the string representation as much as is.
        add_prefix (bool):
            if self_value is a string:
                if True add 0b prefix to returned output,
                if False then do not add prefix to returned output
            if self_value is a Binary instance:
                always forces to True, will always show prefix 0b

        Returns:
        Union[Binary, str]: binary string representation of number
            If self_value was of class Binary, it returns a Binary instance.
            If self_value was of class str, it returns a str instance.

        """
        if not (isinstance(self_value, str) or isinstance(self_value, Binary)):
            raise TypeError(f"Argument {self_value} must be of type Binary or str.")
        if isinstance(self_value, Binary):
            return Binary(
                Binary.to_no_exponent(
                    self_value._value, length=length, simplify=simplify
                )
            )
        if self_value == "":
            raise ValueError(f"Argument {self_value} must not be empty string.")
        value: str = self_value  # it is a string
        # print(f"before normalize {value}")
        if _NAN.lower() in value.lower() or _INF.lower() in value.lower():
            return value
        value = value.replace(_PREFIX, "")  # just in case: remove 0b prefix
        if _EXP not in value:
            result = value
        else:
            li = value.split(_EXP)
            intfracpart = li[0]
            exp = int(li[1])

            li = intfracpart.split(".")
            intpart = li[0]
            intpart = "0" if intpart == "" else intpart
            if len(li) == 1:
                fracpart = ""
            else:
                fracpart = li[1]
            lenintpart = len(intpart)
            lenfracpart = len(fracpart)

            if exp >= 0:
                if lenfracpart <= exp:
                    fracpart += "0" * (exp - lenfracpart)
                    result = intpart + fracpart
                else:
                    intpart += fracpart[:exp]
                    fracpart = fracpart[exp:]
                    result = intpart + "." + fracpart
            else:  # exp < 0
                if lenintpart <= abs(exp):
                    if intpart[0] == "-":
                        intpart = "0" * (abs(exp) - lenintpart + 1) + intpart[1:]
                        result = "-0." + intpart + fracpart
                    else:
                        intpart = "0" * (abs(exp) - lenintpart) + intpart
                        result = "0." + intpart + fracpart
                else:
                    fracpart = intpart[exp:] + fracpart
                    if intpart[:exp] == "":
                        intpart = "0"
                    elif intpart[:exp] == "-":
                        intpart = "-0"
                    else:
                        intpart = intpart[:exp]
                    result = intpart + "." + fracpart
        if simplify:
            result = Binary.simplify(result, add_prefix)
        if length != -1:
            le = len(result)
            if le > length:
                raise OverflowError
            result = "0" * (length - le) + result
        # print(f"after normalize {value} {result}")
        return result  # str

    def to_no_mantissa(self: Binary) -> Binary:
        """Convert to exponential representation without fraction,
        i.e. without mantissa.

        A method that changes the string representation of a number
        so that the resulting string has no decimal point.
        The value does not change. The precision does not change.

        Examples:
        * converts '1.1' to '11e-1'
        * converts '-0.01e-2' to '-1e-4'

        Parameters:
        none

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self._is_special:
            raise OverflowError(
                f"Argument 'self' ({self}): cannot convert NaN and infinities."
            )
        value = self._value
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.simplify(value)
        else:
            li = value.split(_EXP)
            intfracpart = Binary.simplify(li[0])
            exp = int(li[1])

        li = intfracpart.split(".")
        intpart = li[0]
        if len(li) == 1:
            fracpart = ""
        else:
            fracpart = li[1]
        # lenintpart = len(intpart)
        lenfracpart = len(fracpart)
        exp -= lenfracpart
        intpart += fracpart

        if self._sign:
            intpart = "-" + intpart[1:].lstrip("0") if len(intpart) > 1 else intpart
        else:
            intpart = intpart.lstrip("0") if len(intpart) > 1 else intpart
        result = intpart + _EXP + str(exp)
        # do not remove possible e0 by simplifying it
        return Binary(result, simplify=False)

    def to_exponent(self: Binary, exp: int = 0) -> Binary:
        """Convert to exponential representation with specified exponent.

        This is a method that changes string representation of number.
        It does not change the value. It does not change the precision.

        If `exp` is not set, it defaults to 0, producing a respresentation
        without an exponent, same as `to_no_exponent()`.

        Examples:
        * converts '1.1' with exp=0 ==> '1.1'
        * converts '1.1' with exp=3 ==> '0.0011e3'
        * converts '1.1' with exp=-3 ==> '1100e-3'
        * converts '-0.01e-2' with exp=2 ==> '-0.000001e2'

        Parameters:
        exp (int): the desired exponent, 0 is the default

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self._is_special:
            raise OverflowError(
                f"Argument 'self' ({self}): cannot convert NaN and infinities."
            )
        sign, intpart, fracpart, _ = self.to_no_exponent().components()
        result = "-" if sign else ""

        if exp >= 0:
            new_intpart = intpart[: len(intpart) - exp]
            new_fracpart = (
                "0" * (-len(intpart) + exp) + intpart[len(intpart) - exp :] + fracpart
            )
        else:
            new_intpart = (
                intpart + fracpart[: abs(exp)] + (-len(fracpart) + abs(exp)) * "0"
            )
            new_fracpart = fracpart[abs(exp) :]
        result += new_intpart + "." + new_fracpart + _EXP + str(exp)

        return Binary(Binary.simplify(result))

    def to_sci_exponent(self: Binary) -> Binary:
        """Convert to exponential representation in scientific notation.

        This is a method that changes string representation of number.
        It does not change the value. It does not change the precision.

        Scientific notation is an exponent representation with a single
        binary digit before decimal point.

        The decimal part is always 1 or -1 except for the number 0.

        Examples:
        * converts '1.1' ==> '1.1e0'
        * converts '-0.01e-2' ==> '-1e-4'

        Parameters:
        none

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self._is_special:
            raise OverflowError(
                f"Argument 'self' ({self}): cannot convert NaN and infinities."
            )
        value = self._value
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.simplify(value)
        else:
            li = value.split(_EXP)
            intfracpart = Binary.simplify(li[0])
            exp = int(li[1])

        li = intfracpart.split(".")
        intpart = li[0]
        if len(li) == 1:
            fracpart = ""
        else:
            fracpart = li[1]
        if self._sign:
            intpart = intpart[1:]
            sign = "-"
        else:
            sign = ""
        lenintpart = len(intpart)

        intfracpart = intfracpart.replace(".", "").replace("-", "")
        middle = 1
        start = 0
        exp += lenintpart - 1
        while True:
            if middle > len(intfracpart):
                break
            if intfracpart[start : start + 1] != "0":
                fracpart = intfracpart[middle:]
                intpart = intfracpart[start:middle]
                break
            start += 1
            middle += 1
            exp -= 1

        if fracpart == "" or fracpart == "0":
            result = sign + intpart + _EXP + str(exp)
        else:
            result = sign + intpart + "." + fracpart + _EXP + str(exp)
        # do not remove possible e0 by simplifying it
        return Binary(result, simplify=False)

    def to_eng_exponent(self: Binary) -> Binary:
        """Convert to exponential representation in engineering notation.

        - See https://www.purplemath.com/modules/exponent4.htm.
        - See https://www.thinkcalculator.com/numbers/decimal-to-engineering.php
        - See https://en.wikipedia.org/wiki/Engineering_notation.
        - See https://en.wikipedia.org/wiki/Engineering_notation#Binary_engineering_notation

        Engineering notation is an exponent representation with the exponent
        modulo 10 being 0, and where there are 1 through 9 digit before the
        decimal point.
        The integer part must not be 0 unless the number is 0.
        The integer part is from 1 to 1023, or written in binary fraction
        from 0b1 to 0b111111111.

        Method that changes string representation of number. It does not change
        value. It does not change precision.

        Examples:
        * converts '1.1' ==> '1.1'
        * converts '1.1111' ==> '1.1111'
        * converts '100.1111' ==> '100.1111'
        * converts '1.1111' ==> '1.1111'
        * converts '10.1111' ==> '10.1111'
        * converts '100.1111' ==> '100.1111'
        * converts '1000.1111' ==> '1000.1111'
        * converts 1023 ==> '1111111111' => '1111111111'
        * converts 1024 ==> '10000000000' => '1e10'
        * converts 1025 ==> '10000000001' => '1.0000000001e10'
        * converts 3072 ==> '110000000000' ==> 1.1e10
        * converts 1024 ** 2 ==> '1000000000000000000000000000000' => '1e20'
        * converts '0.1' => '100000000e-10'
        * converts '0.11' => '110000000e-10'
        * converts '0.01' => '10000000e-10'
        * converts '0.0000000001' => '1e-10'
        * converts '0.000000001' => '10e-10'
        * converts '0.00000000111' => '11.1e-10'
        * converts '.11111e1' ==> '1.1111'
        * converts '.011111e2' ==> '1.1111'
        * converts '.0011111e3' ==> '1.1111'
        * converts '-0.01e-2' ==> '-1e-3' => '-1000000e-10'
        * converts '-0.0001e-4' == -0.00000001 ==> '-100e-10',
        * converts '-0.0001111e-4' == -0.00000001111 ==> '-111.1e-10',

        Parameters:
        none

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self._is_special:
            raise OverflowError(
                f"Argument 'self' ({self}): cannot convert NaN and infinities."
            )

        if self._value == Binary.simplify("0"):
            return Binary("0")
        if _EXP in self._value:
            value = self.to_no_exponent()._value
        else:
            value = self._value

        sign, intpart, fracpart, exp = Binary.get_components(value)

        assert exp == 0

        result = "-" if sign else ""
        i = math.floor((len(intpart) - 1) / 10) * 10
        new_intpart = intpart[: len(intpart) - i]
        new_intpart = "0" if new_intpart == "" else new_intpart
        while new_intpart == "0":
            i -= 10
            new_intpart = intpart[: len(intpart) + i]

        if i > 0:
            new_fracpart = intpart[len(intpart) - i :] + fracpart
        else:
            new_intpart += fracpart[: abs(i)] + "0" * (abs(i) - len(fracpart[: abs(i)]))
            new_fracpart = fracpart[abs(i) :]

        result += new_intpart + "." + new_fracpart
        result = result.rstrip("0")
        result = result.rstrip(".")
        result += _EXP + str(i)
        return Binary(Binary.simplify(result))

    def to_fraction(self_value: Union[str, Binary]) -> Fraction:
        """Convert string representation of Binary to Fraction.

        This is a utility function. If operating on `Binary` use
        method `fraction()` instead.

        Parameters:
        self_value (str, Binary): binary number as string

        Returns:
        Fraction: self_value as fraction
        """
        if not isinstance(self_value, str) and not isinstance(self_value, Binary):
            raise TypeError(f"Argument {self_value} must be of type str or Binary.")
        if isinstance(self_value, Binary):
            # this is just an alternative way to get the fraction part of a Binary
            return self_value._fraction
        sign, intpart, fracpart, exp = Binary.get_components(self_value)
        exp -= len(fracpart)
        if exp > 0:
            result = Fraction((-1) ** sign * int(intpart + fracpart, 2) * (2 ** exp), 1)
        else:
            result = Fraction((-1) ** sign * int(intpart + fracpart, 2), 2 ** -exp)
        return result

    def to_fraction_alternative_implementation(value: str) -> Fraction:
        """Convert string representation of Binary to Fraction.

        This is a utility function.

        This is an alternative implementation with possibly less precision.
        Use function `to_fraction()` or method `fraction()` instead.

        Parameters:
        value (str): binary number as string

        Returns:
        Fraction: value as fraction
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        if _EXP in value:
            value = Binary.to_no_exponent(value)
        sign, intpart, fracpart, exp = Binary.get_components(value)
        result = Fraction(int(intpart, 2))
        le = len(fracpart)
        for i in range(le):
            c = fracpart[i]
            if c == "1":
                result += Fraction(1, 2 ** (i + 1))
        return result if sign == 0 else -result

    def to_twoscomplement(self: Binary, length: int = -1) -> TwosComplement:
        """Computes the representation as a string in twos-complement.

        This is a method returning a string of class `TwosComplement`.

        See `TwosComplement` class for more details on twos-complement format.

        Examples:
        * converts '-11.1e-2' to '101.1e-2' (-3/4)
        * converts '-11', 3 to '101' (3)
        * converts '-0.1' to '11.1' (-0.5)
        * converts '-1' to '1' (-1)
        * converts '-10' to '10' (-2)
        * converts '-11' to '101' (-3)
        * converts '-100' to '100' (-4)
        * converts '-1.5' to '10.1'
        * converts '-2.5' to '101.1'
        * converts '-2.5e89' to '101.1e89'

        Parameters:
        length (int): this increases the length of the returned string
            to a lenght of "length" by prefilling it with leading
            0s for positive numbers, and 1s for negative numbers.
            length == -1 means that the string will be returned as short
            as possible without prefilling. If the desired "length"
            is shorter than needed to represent the number, the exception
            OverflowError will be raised. The length is counted in a
            non-exponential representation with the decimal point counting
            as 1. So, for example, '11.01' has a length of 5. The same
            value in length 8 would be '11111.01'. Or, the decimal 2 in
            length 8 would be '00000010'.

        Returns:
        TwosComplement: binary string representation in twos-complement
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(length, int):
            raise TypeError(f"Argument {length} must be of type int.")
        if length <= 0 and length != -1:
            raise ValueError(f"Argument {length} must be bigger than 0 or -1")
        if self._is_special:
            raise ArithmeticError(
                f"ArithmeticError: argument {self} is NaN or infinity."
            )
        return TwosComplement(self._fraction, length=length)

    def from_twoscomplement(value: TwosComplement, simplify: bool = True) -> str:
        """The opposite of `to_twoscomplement()` function.

        This is a utility function that converts from twos-complement format
        to binary fraction format.

        The user, programmer should use the constructor instead, e.g.
        `Binary(TwosComplement(-123))`, to directly convert an instance of
        class `TwosComplement` into an instance of class `Binary`.

        See `TwosComplement` class for more details on twos-complement format.

        Examples:
        * converts '1101' to '-11' (-3)
        * converts '1101.1e-2' to '-11.1e-2'  (-3.5/4)

        Parameters:
        value (TwosComplement): string in twos-complement format
        simplify (bool): If simplify is False, it leaves fractional binary strings
            as much unchanged as possible.
            If simplify is True it simplifies returned fractional
            binary string representation.

        Returns:
        str: string in binary fraction format
        """
        if not isinstance(value, TwosComplement):
            raise TypeError(f"Argument {value} must be of type TwosComplement.")
        if _NAN.lower() in value.lower() or _INF.lower() in value.lower():
            raise ArithmeticError(
                f"ArithmeticError: argument {self} is NaN or infinity."
            )
        if not TwosComplement.istwoscomplement(value):
            raise ValueError(f"Argument {value} not a valid twos-complement literal.")
        result = value
        if value[0] == "0":
            # positive twoscomplement is like binary fraction but with (possibly) leading 0
            if simplify:
                # result = value[1:] if value != "0" else value
                result = Binary.simplify(result)
            return result
        return Binary(value, simplify=simplify)._value

    def __float__(self: Binary) -> Union[float, int]:
        """Convert from Binary to float.

        This is a method that convert Binary to float (or if possible to
        integer).

        Returns:
        float or integer: number as float or integer
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isinfinity():
            result = float("Inf")
        elif self.isnan():
            result = float("NaN")
        else:
            result = float(self._fraction)
        # alternative implementation of float
        # result = Binary.to_float(self._value)
        return result  # float or integer

    def __int__(self: Binary) -> int:
        """Convert from Binary to int.

        This method converts a Binary to an integer.

        Returns:
        int: number as integer
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isinfinity():
            raise ValueError(
                f"Argument {self} is infinity. Infinity cannot be converted to integer."
            )
        else:
            result = int(self._fraction)
        return result  # int

    def __str__(self: Binary) -> str:
        """Returns string of the binary fraction.

        Method that implements the string conversion `str()`.
        Return format includes the prefix of '0b'.
        As alternative one can use method `string()` which returns
        the same but without prefix '0b'.

        Examples:
        * 0b1
        * 0b0
        * 0b101.101e23
        * -0b101.101e-23

        Parameters:
        None

        Returns:
        str: string representation with prefix '0b'
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isnan():
            return _NAN
        if self.ispositiveinfinity():
            return _INF
        if self.isnegativeinfinity():
            return _NINF
        if self._sign:
            return "-" + _PREFIX + self._value[1:]
        else:
            return _PREFIX + self._value

    def compare_representation(self: Binary, other: Union[str, Binary]) -> bool:
        """Compare representation of self to representation of other string.

        Does *NOT* compare values! '1.1' does *NOT* equal to '11e-1' in
        `compare_representation()` even though the values are equal.

        Only string '11e-1' equals '11e-1' !
        Returns integer.

        Parameters:
        other (str, Binary): object to compare to

        Returns:
        bool: returns True if both strings match, False otherwise
        """
        if not isinstance(self, Binary) or not (
            isinstance(other, Binary) or isinstance(other, str)
        ):
            raise TypeError(f"Argument {self} must be of type Binary.")
        # compare representation to another Binary
        if isinstance(other, Binary):
            return str(self._value) == str(other._value)
        if isinstance(other, str):
            return str(self._value) == other
        else:
            return str(self._value) == str(other)

    def __repr__(self: Binary) -> str:
        """Represents self. Shows details of the given object.

        Parameters:
        None

        Returns:
        str: returns details of the object
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return (
            f"{self.__class__.__name__}"
            + f"({self._value}, {self._sign}, {self._is_special})"
        )

    def no_prefix(self_value: Union[str, Binary]) -> str:
        """Remove prefix '0b' from string representation.

        A method as well as a utility function.
        Return format is without prefix '0b'.

        Examples:
        * 0
        * 1
        * 10.1e45
        * -101.101e-23.

        Parameters:
        value (str, Binary): string from where to remove prefix

        Returns:
        str: string without prefix '0b'
        """
        if not isinstance(self_value, str) and not isinstance(self_value, Binary):
            raise TypeError(f"Argument {self_value} must be of type str or Binary.")
        if isinstance(self_value, str):
            return self_value.replace(_PREFIX, "")
        else:
            return str(self_value._value)

    def np(self_value: Union[str, Binary]) -> str:  # no prefix
        """Remove prefix '0b' from string representation.

        Same as `no_prefix()`.

        Parameters:
        value (str, Binary): string from where to remove prefix

        Returns:
        str: string without prefix '0b'
        """
        return Binary.no_prefix(self_value)

    def version() -> str:
        """Gives version number.

        This is a utility function giving version of this program.

        Examples:
        * "20210622-103815"

        Returns:
        str: version number as date in format "YYMMDD-HHMMSS".
        """
        return _BINARY_VERSION

    def simplify(value: str, add_prefix: bool = False) -> str:
        """Simplifies string representation.

        This is a utility function.

        Do *NOT* use it on Twos-complement strings!

        Examples:
        * converts '11.0' to '11'
        * converts '0011.0e-0' to '11'

        Parameters:
        value (str): binary string representation of number
        add_prefix (bool): if True add '0b' prefix to returned output;
            if False then do not add prefix to returned output.

        Returns:
        str: simplified binary string representation of number
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        if not isinstance(add_prefix, bool):
            raise TypeError(f"Argument {value} must be of type bool.")
        if _NAN.lower() in value.lower() or _INF.lower() in value.lower():
            return value
        value = value.replace(_PREFIX, "")  # just in case: remove 0b prefix
        sign, intpart, fracpart, exp = Binary.get_components(value)
        fracpart = fracpart.rstrip("0")
        intpart = intpart.lstrip("0")
        pre = _PREFIX if add_prefix else ""
        if intpart == "" and fracpart == "":
            # it does not matter what sign is
            # it does not matter what exp is, for any exp, result is 0
            return pre + "0"
        signstr = "-" if sign else ""
        intpart = "0" if intpart == "" else intpart
        if exp == 0:
            if fracpart == "":
                return signstr + pre + intpart
            else:
                return signstr + pre + intpart + "." + fracpart
        else:
            if fracpart == "":
                return signstr + pre + intpart + _EXP + str(exp)
            else:
                return signstr + pre + intpart + "." + fracpart + _EXP + str(exp)

    def __round__(self: Binary, ndigits: int = 0) -> Binary:
        """Normalize and round number to `ndigits` digits after decimal point.

        This is a method. It implements the function `round()`.
        Same as method `round()`.
        See utility function `round_to()` for details and examples.

        Parameters:
        ndigits (int): number of digits after decimal point, precision

        Returns:
        Binary: binary string representation of number
        Other classes like Fractions have the simplicity of returning class int.
        The return class here must be Binary and it cannot be int because round()
        needs to be able to support ndigits (precision).
        """
        return self.round(ndigits)

    def round(self: Binary, ndigits: int = 0) -> Binary:
        """Normalize and round number to `ndigits` digits after decimal point.

        This is a method. Same as function `__round__()`.
        See utility function `round_to()` for details and examples.

        Parameters:
        ndigits (int): number of digits after decimal point, precision

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(ndigits, int):
            raise TypeError(f"Argument {self} must be of type int.")
        value = self._value
        result = Binary.round_to(value, ndigits)
        return Binary(result)

    def round_to(value: str, ndigits: int = 0) -> str:
        """Normalize and round number to `ndigits` digits after decimal point.

        This is a utility function.

        Examples:
        * converts '11.01e-2' to '0.11' with ndigits==2.
        * converts '0.1' to '0' with ndigits==0.
        * converts '0.10000001' to '1' with ndigits==0.

        Parameters:
        value (str): binary string representation of number
        ndigits (int): number of digits after decimal point, precision

        Returns:
        str: binary string representation of number
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        if not isinstance(ndigits, int):
            raise TypeError(f"Argument {ndigits} must be of type int.")
        if ndigits < 0:
            raise ValueError(
                f"Argument 'ndigits' ({ndigits}) must be a positive integer."
            )
        if _NAN.lower() in value.lower():
            raise ValueError(
                f"Argument 'value' ({value}): cannot convert NaN to integer."
            )
        if _INF.lower() in value.lower():
            raise OverflowError(
                f"Argument 'value' ({value}): cannot convert infinities to integer."
            )
        value = Binary.to_no_exponent(value)
        value = value.replace(_PREFIX, "")
        li = value.split(".")
        intpart = li[0]
        if len(li) == 1:
            fracpart = ""
        else:
            fracpart = li[1]

        if len(fracpart) <= ndigits:
            return value
        nplusonedigit = fracpart[ndigits]
        nplusonedigits = fracpart[ndigits:]
        if (len(nplusonedigits.rstrip("0")) <= 1) or (nplusonedigit == "0"):
            # '' or '1'
            result = intpart + "." + fracpart[0:ndigits]
            # round down from 0.10xxx1 to 0.11000 ==> 0.1
        else:
            # round up from 0.1xxxx1 to 0.111111 ==> 1.0
            digits = intpart + fracpart[0:ndigits]
            if digits[0] == "-":
                signstr = "-"
                digits = digits[1:]  # remove - sign
            else:
                signstr = ""
            digits = bin(int(digits, 2) + 1)[2:]  # rounded up
            # print(f'digits is {digits}')
            le = len(digits)
            result = signstr + digits[: le - ndigits] + "." + digits[le - ndigits :]
        result = Binary.simplify(result)
        return result

    def fill(self: Binary, ndigits: int = 0, strict: bool = False):
        """Normalize and fill number to `ndigits` digits after decimal point.

        This is a method. See also function `fill_to()` for more details.

        Parameters:
        ndigits (int): desired number of digits after decimal point, precision
        strict (bool): If True, truncate result by rounding if input is
            too long to fit into ndigits after decimal point. This would
            remove precision. If True, result will have at strictly
            (i.e. exactly) `ndigits` digits after decimal point.
            If False, never truncate. If False, result can have more than
            `ndigits`
            digits after decimal point.

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(ndigits, int):
            raise TypeError(f"Argument {self} must be of type int.")
        if not isinstance(strict, bool):
            raise TypeError(f"Argument {self} must be of type bool.")
        value = self._value
        return Binary(Binary.fill_to(value, ndigits, strict))

    def fill_to(value: str, ndigits: int = 0, strict: bool = False) -> str:
        """Normalize and fill number to n digits after decimal point.

        This is a utility function.

        Normalizes the input, i.e. it converts it into a representation
        without an exponent. Then it appends '0's to the right, after the
        decimal point, to assure at least `ndigits` digits after the
        decimal point.

        If strict is True and if value does not fit into ndigit digits
        after the decimal point,
        then shorten fractional part to strictly (exactly) ndigits.
        In this case precision is lost.

        If strict is False, never shorten, never truncate the result.
        In this case, the return value could have more than `ndigits`
        digits after the decimal point.

        Parameters:
        ndigits (int): desired number of digits after decimal point, precision
        strict (bool): If True, truncate result by rounding if input is
            too long to fit into ndigits after decimal point. This would
            remove precision. If True, result will have at strictly
            (i.e. exactly) `ndigits` digits after decimal point.
            If False, never truncate. If False, result can have more than
            `ndigits`
            digits after decimal point.

        Returns:
        str: binary string representation of number
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        if _NAN.lower() in value.lower():
            raise ValueError(f"Argument 'value' ({value}): cannot fill NaN.")
        if _INF.lower() in value.lower():
            raise OverflowError(f"Argument 'value' ({value}): cannot fill infinities.")
        if ndigits < 0:
            raise ValueError(
                f"Argument 'ndigits' ({ndigits}) must be a positive integer."
            )
        value = Binary.to_no_exponent(value)
        li = value.split(".")
        if len(li) == 1:
            fracpart = ""
        else:
            fracpart = li[1]
        if len(fracpart) == ndigits:
            return value
        elif len(fracpart) < ndigits:
            if fracpart == "":
                value += "."
            return value + "0" * (ndigits - len(fracpart))
        elif not strict:  # len(fracpart) > ndigits:
            return value
        else:  # strict
            result = Binary.round_to(value, ndigits)
            # rounding can shorten it drastically, 0.1111 => 1
            return Binary.fill_to(result, ndigits, strict)

    def get_components(value: str) -> tuple:
        """Returns sign, integer part (without sign), fractional part, and
        exponent.

        A `sign` of integer 1 represents a negative (-) value. A `sign` of integer 0
        represents a positive (+) value.

        Examples:
        * converts 11 ==> (0, '11', '', 0)
        * converts 11.01e3 ==> (0, '11', '01', 3)
        * converts -11.01e2 ==> (1, '11', '01', 2)

        Parameters:
        value (str): respresentation of a binary

        Returns:
        tuple: tuple of 4 elements: sign (int), integer part (without sign) (str),
            fractional part (str), exponent (int)
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        if _NAN.lower() in value.lower() or _INF.lower() in value.lower():
            raise ValueError(f"Argument {value} must not be Inf, -Inf or NaN.")
        value = value.replace(_PREFIX, "")  # just in case: remove 0b prefix
        sign = 1 if value[0] == "-" else 0
        if sign:
            value = value[1:]  # remove sign from intpart
        if _EXP not in value:
            exp = 0
            intfracpart = value
        else:
            li = value.split(_EXP)
            intfracpart = li[0]
            exp = int(li[1])

        li = intfracpart.split(".")
        intpart = li[0]
        if len(li) == 1:
            fracpart = ""
        else:
            fracpart = li[1]

        # simplify intpart uand fracpart
        fracpart = fracpart.rstrip("0")
        intpart = intpart.lstrip("+")
        intpart = intpart.lstrip("0")
        intpart = "0" if intpart == "" else intpart
        sign = 0 if intpart == "0" and fracpart == "" else sign
        return (sign, intpart, fracpart, exp)

    def components(self: Binary) -> tuple:
        """Returns sign, integer part (without sign), fractional part, and
        exponent.

        A `sign` of integer 1 represents a negative (-) value. A `sign` of integer 0
        represents a positive (+) value.

        Examples:
        * converts 11 ==> (0, '11', '', 0)
        * converts 11.01e3 ==> (0, '11', '01', 3)
        * converts -11.01e2 ==> (1, '11', '01', 2)

        Parameters:
        value (str): respresentation of a binary

        Returns:
        tuple: tuple of 4 elements: sign (int), integer part (without sign) (str),
            fractional part (str), exponent (int)
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return Binary.get_components(self._value)

    def isinfinity(self: Binary) -> bool:
        """Determines if object is positive or negative Infinity.

        Parameters:
        none

        Returns:
        bool: is or is not any kind of infinity or negative infinity
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _INF in self._value

    def isnegativeinfinity(self: Binary) -> bool:
        """Determines if object is Negative Infinity.

        Parameters:
        none

        Returns:
        bool: is or is not negative infinity
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _NINF in self._value

    def ispositiveinfinity(self: Binary) -> bool:
        """Determines if object is Positive Infinity.

        Parameters:
        none

        Returns:
        bool: is or is not positive infinity
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _INF in self._value and not _NINF in self._value

    def isnan(self: Binary) -> bool:
        """Determines if object is not-a-number (NaN).

        Parameters:
        none

        Returns:
        bool: is or is not a NaN
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _NAN in self._value  # "NaN"

    def isint(self: Binary) -> bool:
        """Determines if binary fraction is an integer.

        This is a utility function.

        Returns:
        bool: True if int, False otherwise (i.e. has a non-zero fraction).
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self._is_special:
            return False
        return self._fraction == int(self._fraction)

    def _adjusted(self: Binary) -> int:
        """Return the adjusted exponent of self.

        Parameters:
        none

        Returns:
        int: adjusted exponent
        """
        if self._is_special:
            return 0
        se = Binary.to_no_mantissa(self)
        sign, intpart, fracpart, exp = Binary.components(se)
        if fracpart != "":
            raise ValueError(
                f"Invalid literal: {se._value}. Internal error. "
                "Fraction part should be empty."
            )
        return exp + len(intpart) - 1

    def fraction(self: Binary) -> Fraction:
        """Extracts Fractional representation from Binary instance.

        A method to get the Binary as a `Fraction`.

        Parameters:
        None

        Returns:
        Fraction: binary number in Fraction representation
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return self._fraction

    def string(self: Binary) -> str:
        """Extracts string representation from Binary instance.

        A method to get the Binary as a string.
        It does not have a '0b' prefix.

        See also function `__str__()` which implements the `str()` conversion function
        which returns the string representation, but with a '0b' prefix.

        Parameters:
        None

        Returns:
        str: binary number in string representation without prefix '0b'
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return self._value

    def fraction_to_string(
        number: Union[int, float, Fraction],
        ndigits: int = _BINARY_PRECISION,
        simplify: bool = True,
    ) -> str:
        """Converts number representation (int, float, or Fraction) to string.

        This is a utility function.

        Parameters:
        number (int,float,Fraction): binary number in number representation
        ndigits (int): desired digits after decimal point.
        simplify (bool): If True simplify output by performing cleanup and
            removing unnecessary digits.
            If False, then produce exact as-is twos-complement components
            without any cleanup or simplifications.

        Returns:
        str: binary number in string representation
        """
        number = Fraction(number) if not isinstance(number, Fraction) else number
        sign = "-" if number < 0 else ""
        number = abs(number)
        int_number = math.floor(number)
        if int_number == 0:
            result = [sign, "0"]
        else:
            result = [sign] + bin(int_number)[2:].split()
        rest = Fraction(0)
        i = 1
        fraction_number = number - int_number
        if fraction_number > 0:
            result.append(".")
            while i < ndigits + 1:
                b = Fraction(1, 2 ** i)
                if b + rest < fraction_number:
                    result.append("1")
                    rest += b
                elif b + rest > fraction_number:
                    result.append("0")
                elif b + rest == fraction_number:
                    result.append("1")
                    break
                i += 1
        return Binary.simplify("".join(result)) if simplify else "".join(result)

    def isclose(
        self: Binary, other: Any, rel_tol: float = _BINARY_RELATIVE_TOLERANCE
    ) -> bool:
        """Compare two objects to see if they are mathematically close.

        This is a utility function. Useful for floats that have been converted
        to binary fractions. A substitute for the `==` operand for binary fractions
        created from floats with precision errors.

        Parameters:
        other (Any, int, float, Fraction, Binary): value of number
        rel_tol (float): relative tolerance as epsilon-value
            to decide if two numbers are close relative to each other

        Returns:
        bool: True if two numbers are close, False otherwise
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self._is_special or other._is_special:
            return False
        return math.isclose(self._fraction, other._fraction, rel_tol=rel_tol)

    def _cmp(self: Binary, other: Any) -> int:
        """Compare two objects.

        Compare the two non-NaN decimal instances self and other.
        Returns -1 if self < other, 0 if self == other and 1
        if self > other.  This routine is for internal use only.
        Returns integer.

        Note: The Decimal standard doesn't cover rich comparisons for
        Decimals.  In particular, the specification is silent on the
        subject of what should happen for a comparison involving a NaN.
        In Decimal they take the following approach:

        ```
          == comparisons involving a quiet NaN always return False
          != comparisons involving a quiet NaN always return True
          == or != comparisons involving a signaling NaN signal
             InvalidOperation, and return False or True as above if the
             InvalidOperation is not trapped.
          <, >, <= and >= comparisons involving a (quiet or signaling)
             NaN signal InvalidOperation, and return False if the
             InvalidOperation is not trapped.
        ```

        That Decimal behavior is designed to conform as closely as possible to
        that specified by IEEE 754.

        Here in Binary we take a similar approach and try to follow Decimal.

        Parameters:
        other (Any, str, Binary, int, float, Fraction): object to compare to

        Returns:
        int: returns -1 if s<o, 0 if equal, 1 if s>o
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self._is_special or other._is_special:
            if self.isnan() or other.isnan():
                # Compare(NaN, NaN) => exception
                # Equal(NaN, NaN) => False
                # Compare(NaN, 1) => False
                # Compare(NaN, Inf) => False
                raise ArithmeticError(f"Arithmetic Error: Cannot compare two NaNs.")
            if self.isnegativeinfinity() and other.ispositiveinfinity():
                return -1
            elif self.ispositiveinfinity() and other.isnegativeinfinity():
                return 1
            elif self.isnegativeinfinity() and other.isnegativeinfinity():
                return 0
            elif self.ispositiveinfinity() and other.ispositiveinfinity():
                return 0
            elif self.isnegativeinfinity():
                return -1
            elif self.ispositiveinfinity():
                return 1
            elif other.isnegativeinfinity():
                return -1
            else:  # other.ispostiveinfinity():
                return 1

        if self._fraction == other._fraction:
            result = 0
        elif self._fraction < other._fraction:
            result = -1
        else:
            result = 1
        return result

    def compare(self: Binary, other: Any) -> Binary:
        """Compares `self` to `other`. Returns a Binary value.

        ```
        s or o is a NaN ==> Binary('NaN')
        s < o           ==> Binary('-1')
        s == o          ==> Binary('0')
        s > o           ==> Binary('1')
        ```

        Parameters:
        other (str, Binary): object to compare to

        Returns:
        Binary: returns Binary -1 if s<o, Binary 0 if equal,
            Binary 1 if s>o
        """
        return Binary(self._cmp(other))

    def __eq__(self: Binary, other: Any) -> bool:
        """Implements equal, implements operand `==`.

        Method that implements `==` operand.

        See `_cmp()` for details.

        Parameters:
        self (Binary): binary fraction number
        other (Any): number

        Returns:
        bool: result
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return False  # see comments in _cmp()
        return self._cmp(other) == 0

    def __lt__(self: Binary, other: Any) -> bool:
        """Less than operation.

        Method that implements `<` operand.

        Parameters:
        self (Binary): binary fraction number
        other (Any): number

        Returns:
        bool: result
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return False  # see comments in _cmp()
        return self._cmp(other) == -1

    def __gt__(self: Binary, other: Any) -> bool:
        """Greater than operation.

        Method that implements `>` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        bool: result
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return False  # see comments in _cmp()
        return self._cmp(other) == 1

    def __le__(self: Binary, other: Any) -> bool:
        """Less or equal operation.

        Method that implements `<=` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        bool: result
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return False  # see comments in _cmp()
        compare = self._cmp(other)
        return not compare == 1 or compare == 0

    def __ge__(self: Binary, other: Any) -> bool:
        """Greater or equal operation.

        Method that implements `>=` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        bool: result
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return False  # see comments in _cmp()
        compare = self._cmp(other)
        return not compare == -1 or compare == 0

    def __add__(self: Binary, other: Any) -> Binary:
        """Add operation.

        Method that implements the `+` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: addition of the two numbers
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.ispositiveinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity() and other.isnegativeinfinity():
            return Binary(_NINF)
        if self.isnegativeinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity() or other.ispositiveinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity() or other.isnegativeinfinity():
            return Binary(_NINF)
        return Binary(self._fraction + other._fraction)

    def __sub__(self: Binary, other: Any) -> Binary:
        """Subtraction operation.

        Method that implements the `-` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: substraction of the two numbers
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.ispositiveinfinity():
            return Binary(_NINF)
        if self.ispositiveinfinity() and other.isnegativeinfinity():
            return Binary(_INF)
        if self.ispositiveinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity():
            return Binary(_NINF)
        if other.isnegativeinfinity():
            return Binary(_INF)
        if other.ispositiveinfinity():
            return Binary(_NINF)
        return Binary(self._fraction - other._fraction)

    def __mul__(self: Binary, other: Any) -> Binary:
        """Multiply operation.

        Method that implements the `*` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: multiplication, i.e. product, of the two numbers
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.ispositiveinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity() and other.isnegativeinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity() and other.ispositiveinfinity():
            return Binary(_NINF)
        if self.ispositiveinfinity() and other.isnegativeinfinity():
            return Binary(_NINF)
        if self.ispositiveinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity():
            return Binary(_NINF)
        if other.isnegativeinfinity():
            return Binary(_NINF)
        if other.ispositiveinfinity():
            return Binary(_INF)
        return Binary(self._fraction * other._fraction)

    def __truediv__(self: Binary, other: Any) -> Binary:
        """True division operation.

        Method that implements the `/` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: true division of the two numbers
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity():
            return Binary(_NINF)
        if other.isnegativeinfinity():
            return Binary(0)
        if other.ispositiveinfinity():
            return Binary(-0)
        if other._fraction == 0:
            raise ZeroDivisionError(f"ZeroDivisionError: Binary division by zero.")
        return Binary(self._fraction / other._fraction)

    def __floordiv__(self: Binary, other: Any) -> Binary:
        """Floor division operation.

        Method that implements the `//` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: floor division of the two numbers
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity():
            return Binary(_NAN)
        if other.isnegativeinfinity():
            return Binary(0) if self._sign else Binary(-1)
        if other.ispositiveinfinity():
            return Binary(-1) if self._sign else Binary(0)
        if other._fraction == 0:
            raise ZeroDivisionError(f"ZeroDivisionError: Binary division by zero.")
        return Binary(self._fraction // other._fraction)

    def __mod__(self: Binary, other: Any) -> Binary:
        """Modulo operation.

        Method that implements modulo, i.e. returns the integer remainder.
        Method that implements the `%` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: modulo of the two numbers
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity() and other.ispositiveinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.isnegativeinfinity():
            return Binary(_NAN)
        if self.ispositiveinfinity():
            return Binary(_NAN)
        if self.isnegativeinfinity():
            return Binary(_NAN)
        if other.isnegativeinfinity():
            return self if self._sign else Binary(_NINF)
        if other.ispositiveinfinity():
            return Binary(_INF) if self._sign else self
        if other._fraction == 0:
            raise ZeroDivisionError(f"ZeroDivisionError: Binary modulo.")
        return Binary(self._fraction % other._fraction)

    def __pow__(self: Binary, other: Any) -> Binary:
        """Power of operation.

        Method that implements the `**` operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: power of the two numbers
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return Binary(_NAN)
        if self.ispositiveinfinity() and other.ispositiveinfinity():
            return Binary(_INF)
        if self.isnegativeinfinity() and other.isnegativeinfinity():
            return Binary(0)
        if self.isnegativeinfinity() and other.ispositiveinfinity():
            return Binary(_INF)
        if self.ispositiveinfinity() and other.isnegativeinfinity():
            return Binary(0)
        if self.ispositiveinfinity():
            return Binary(0) if other._sign else Binary(_INF)
        if self.isnegativeinfinity():
            return Binary(-0) if other._sign else Binary(_NINF)
        if other.isnegativeinfinity():
            return Binary(0)
        if other.ispositiveinfinity():
            return Binary(_INF)
        if other._fraction == 0:
            return Binary(1)
        po = self._fraction ** other._fraction
        # (-3.4)**(-3.4)  ==>  (-0.00481896804140973+0.014831258607220378j)
        # type((-3.4)**(-3.4))  ==>  <class 'complex'>
        if isinstance(po, complex):
            raise ArithmeticError(
                f"Argument {self} to the power of {other} is a "
                "complex number which cannot be represented as a Binary."
            )
        return Binary(po)

    def __abs__(self: Binary) -> Binary:
        """Computes absolute value.

        Method that implements absolute value, i.e. the positive value.

        Parameters:
        self (Binary): binary number

        Returns:
        Binary: Absolute of the number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isnan():
            return Binary(_NAN)
        if self.isinfinity():
            return Binary(_INF)
        return Binary(abs(self._fraction))

    def __ceil__(self: Binary) -> int:
        """Performs math ceiling operation returning an int.

        Method that implements `ceil`. This method is invoked by calling
        `math.ceil()`. Note, that `math.ceil()` will return an int (and NOT
        a Binary). See method `ceil()` for a function that returns a `Binary` instance.

        Examples:
        * input '1.11' will return 1.

        Parameters:
        self (Binary): binary number.

        Returns:
        int: ceiling of the number expressed as an int.

        Other classes like Fractions return class int to be consistent
        with math.ceil().
        Following their lead, Binary does the same and returns class int
        instead of class Binary. Use method Binary.ceil() to get result
        in Binary.
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isnan():
            raise ValueError(f"ValueError: cannot convert Binary NaN to integer.")
        if self.isinfinity():
            raise OverflowError(
                f"OverflowError: cannot convert Binary infinity to integer."
            )
        return math.ceil(self._fraction)

    def ceil(self: Binary) -> Binary:
        """Perform math ceiling operation returning a Binary.

        Method that implements `ceil`. This method returns a Binary.
        See method '__ceil__()' for getting an `int` return.

        Examples:
        * input '1.11' will return '0b1' as Binary.

        Parameters:
        self (Binary): binary number.

        Returns:
        Binary: ceiling of the number as Binary.
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isnan():
            raise ValueError(f"ValueError: cannot convert Binary NaN to integer.")
        if self.isinfinity():
            raise OverflowError(
                f"OverflowError: cannot convert Binary infinity to integer."
            )
        return Binary(math.ceil(self._fraction))

    def __floor__(self: Binary) -> int:
        """Perform math floor operation returning an int.

        Method that implements `floor`. This method is invoked by calling
        `math.floor()`. Note, that `math.floor()` will return an int (and NOT
        a Binary). See method `floor()` for a function that returns a `Binary` instance.

        Examples:
        * input '1.11' will return int 1.

        Parameters:
        self (Binary): binary number.

        Returns:
        int: floor of the number expressed as an int.

        Other classes like Fractions return class int to be consistent
        with math.floor().
        Following their lead, Binary does the same and returns class int
        instead of class Binary. Use method Binary.floor() to get result
        in Binary.
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isnan():
            raise ValueError(f"ValueError: cannot convert Binary NaN to integer.")
        if self.isinfinity():
            raise OverflowError(
                f"OverflowError: cannot convert Binary infinity to integer."
            )
        return math.floor(self._fraction)

    def floor(self: Binary) -> Binary:
        """Perform math floor operation returning a Binary.

        Method that implements `floor`. This method returns a Binary.
        See method '__floor__()' for getting an int return.

        Examples:
        * input '1.11' will return '0b1' as Binary.

        Parameters:
        self (Binary): binary number.

        Returns:
        Binary: floor of the number as Binary.
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isnan():
            raise ValueError(f"ValueError: cannot convert Binary NaN to integer.")
        if self.isinfinity():
            raise OverflowError(
                f"OverflowError: cannot convert Binary infinity to integer."
            )
        return Binary(math.floor(self._fraction))

    def __rshift__(self: Binary, ndigits: int) -> Binary:
        """Shifts number `ndigits` digits (bits) to the right.

        Method that implementes `>>` operand.

        As example, shifting right by 1, divides the number by 2.
        The string representation will be changed as little as possible.
        If the string representation is in exponential form it will remain in
        exponential form. If the string representation is in non-exponential form,
        it will remain in non-exponential form, i.e. only the decimal point will be
        moved to the left.

        Parameters:
        self (Binary): number to be shifted
        ndigits (int): number of digits to be shifted right

        Returns:
        Binary: right shifted number
        """
        if not isinstance(self, Binary) or not isinstance(ndigits, int):
            raise TypeError(
                f"Arguments {self} {ndigits} must be of type Binary and int."
            )
        if ndigits < 0:
            raise ValueError(f"ValueError: negative shift count")
        if self.isnan():
            return Binary(_NAN)
        if self.isnegativeinfinity():
            return Binary(_NINF)
        if self.ispositiveinfinity():
            return Binary(_INF)
        if ndigits == 0:
            return self
        if _EXP in self._value:
            sign, intpart, fracpart, exp = Binary.get_components(self._value)
            shifted = (
                sign * "-"
                + intpart
                + "."
                + (fracpart if len(fracpart) > 0 else "0")
                + _EXP
                + str(exp - ndigits)
            )
        else:
            sign, intpart, fracpart, exp = Binary.get_components(self._value)
            if ndigits >= len(intpart):
                intpart = (ndigits - len(intpart) + 1) * "0" + intpart

            shifted_intpart = sign * "-" + intpart[: len(intpart) - ndigits] + "."
            shifted_fracpart = intpart[len(intpart) - ndigits :] + fracpart
            shifted = Binary.simplify(shifted_intpart + shifted_fracpart)
        return Binary(shifted)

    def __lshift__(self: Binary, ndigits: int) -> Binary:
        """Shifts number `ndigits` digits (bits) to the left.

        Method that implementes `<<` operand.

        As example, shifting left by 1, multiplies the number by 2.
        The string representation will be changed as little as possible.
        If the string representation is in exponential form it will remain in
        exponential form. If the string representation is in non-exponential form,
        it will remain in non-exponential form, i.e. only the decimal point will be
        moved to the right.

        Parameters:
        self (Binary): number to be shifted
        ndigits (int): number of digits to be shifted left

        Returns:
        Binary: left shifted number
        """
        if not isinstance(self, Binary) or not isinstance(ndigits, int):
            raise TypeError(
                f"Arguments {self} {ndigits} must be of type Binary and int."
            )
        if ndigits < 0:
            raise ValueError(f"ValueError: negative shift count")
        if self.isnan():
            return Binary(_NAN)
        if self.isnegativeinfinity():
            return Binary(_NINF)
        if self.ispositiveinfinity():
            return Binary(_INF)
        if ndigits == 0:
            return self
        if _EXP in self._value:
            sign, intpart, fracpart, exp = Binary.get_components(self._value)
            shifted = (
                sign * "-"
                + intpart
                + "."
                + (fracpart if len(fracpart) > 0 else "0")
                + _EXP
                + str(exp + ndigits)
            )
        else:
            sign, intpart, fracpart, exp = Binary.get_components(self._value)
            if ndigits >= len(fracpart):
                fracpart += (ndigits - len(fracpart) + 1) * "0"
            shifted_intpart = (
                sign * "-" + (intpart + fracpart[:ndigits]).lstrip("0") + "."
            )
            shifted_intpart = "0." if len(shifted_intpart) <= 1 else shifted_intpart
            shifted_fracpart = fracpart[ndigits:]
            shifted = Binary.simplify(shifted_intpart + shifted_fracpart)
        return Binary(shifted)

    def __bool__(self: Binary) -> bool:
        """Boolean transformation. Used for `bool()` and `not` operand.

        Method that implements transformation to boolean `bool`. This
        boolean transformation is then used by operations like `not`.

        Number 0 returns `False`. All other numbers return `True`.

        Parameters:
        self (Binary): binary number

        Returns:
        bool: boolean transformation of the number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isnan() or self.isinfinity():
            return True
        return bool(self._fraction)

    def __not__(self: Binary) -> bool:
        """Return the 'boolean not' of self.

        Method that implements the `not` operand.
        Do not confuse it with the 'bitwise not' operand `~`.

        If self is 0, then method returns True.
        For all other values it returns False.

        Examples:
        * operation not Binary(0) returns True.
        * operation not Binary(3.5) returns False.

        Parameters:
        self (Binary): number

        Returns:
        Binary: 'boolean not' of number
        """
        return not self._fraction

    def __and__(self: Binary, other: Any) -> Binary:
        """Return the bitwise 'and' of self and other.

        Method that implements the `&` operand.

        Any negative number will be converted into twos-complement
        representation, than bitwise-and will be done, then the resulting
        number will be converted back from twos-complement to
        binary string format.

        Examples:
        * operation '11.1' & '10.1' will return '10.1'
        * operation '-0.1' & '+1' will return '-1'
            because twos-complement of '-0.1' is 1.1.
            Further, 1.1 & 01.0 results in twos-complement 1.0,
            and 1.0 in twos-complement is '-1' in binary fraction. Leading to the
            final result '-1' (or '-0b1').

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: bitwise 'and' of the two numbers in binary fraction format
        """

        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self._is_special or other._is_special:
            raise ArithmeticError(
                f"ArithmeticError: one of the arguments {self}, {other} "
                "is NaN or infinity."
            )
        return Binary._and_or_xor(self, other, "and")

    def __or__(self: Binary, other: Any) -> Binary:
        """Return the bitwise 'or' of self and other.

        Method that implements the `|` operand.

        Any negative number will be converted into twos-complement
        representation, than bitwise-or will be done, then the resulting
        number will be converted back from twos-complement to
        binary string format.

        Examples:
        * operation '11.1' | '10.1' will return '11.1'
        * operation '-0.1' | '+1' will return '-0.1'
        because twos-complement of
        '-0.1' is 1.1; and 1.1 | 01.0 results in twos-complement 1.1;
        and 1.1 in twos-complement is '-0.1' in binary fraction. Hence, the
        final result of '-0.1'.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: bitwise 'or' of the two numbers in binary fraction format
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self._is_special or other._is_special:
            raise ArithmeticError(
                f"ArithmeticError: one of the arguments {self}, {other} "
                "is NaN or infinity."
            )
        return Binary._and_or_xor(self, other, "or")

    def __xor__(self: Binary, other: Any) -> Binary:
        """Return the bitwise 'xor' of self and other.

        Method that implements the `^` operand.

        Any negative number will be converted into twos-complement
        representation, than bitwise-xor will be done, then the resulting
        number will be converted back from twos-complement to
        binary string format.

        Examples:
        * operation '11.1' ^ '10.1' will return '1'.
        * operation '-0.1' ^ '+1' will return '-1.1' because twos-complement of
        '-0.1' is 1.1; and 1.1 ^ 01.0 results in twos-complement 10.1;
        and 10.1 in twos-complement is '-1.1' in binary fraction. Hence, the final
        result of '-1.1'.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: bitwise 'xor' (bitwise exclusive or) of the
            two numbers in binary fraction format
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self._is_special or other._is_special:
            raise ArithmeticError(
                f"ArithmeticError: one of the arguments {self}, {other} "
                "is NaN or infinity."
            )
        return Binary._and_or_xor(self, other, "xor")

    def _and_or_xor(this: Binary, other: Binary, which: str) -> Binary:
        """Performs bitwise 'and', 'or', or 'xor' on two binary fractions.

        This is a function, not a method.

        Parameters:
        this (Binary): number, binary fraction
        other (Binary): number, binary fraction
        which (str): 'and' or 'or' or 'xor'

        Returns:
        Binary: 'and'ed, 'or'ed or 'xor'ed binary fraction
        """
        if not isinstance(this, Binary) or not isinstance(other, Binary):
            raise TypeError(
                f"Arguments {this} {other} must be of type Binary and Binary."
            )
        if not isinstance(which, str):
            raise TypeError(f"Arguments {which} must be of type str.")
        if this._is_special or other._is_special:
            raise ArithmeticError(
                f"ArithmeticError: one of the arguments {this}, {other} "
                "is NaN or infinity."
            )
        which = which.lower()
        if which != "and" and which != "or" and which != "xor":
            raise ValueError(
                f"ValueError: which ({which}) should be 'and', 'or', or 'xor'."
            )

        def __and(ab):
            a, b = ab
            return "1" if a == "1" and b == "1" else "." if a == "." else "0"

        def __or(ab):
            a, b = ab
            return "1" if a == "1" or b == "1" else "." if a == "." else "0"

        def __xor(ab):
            a, b = ab
            return "1" if a != b else "." if a == "." else "0"

        sign1, _, _, _ = this.components()
        sign2, _, _, _ = other.components()

        if sign1:
            this = TwosComplement(this._fraction)
        if sign2:
            other = TwosComplement(other._fraction)
        _, intpart1, fracpart1, _ = this.components()
        _, intpart2, fracpart2, _ = other.components()

        v1, v2 = intpart1, intpart2
        l1, l2 = len(v1), len(v2)
        if sign1 and not sign2:
            if l1 <= l2:
                v1 = (l2 - l1 + 1) * "1" + v1

        if not sign1 and sign2:
            if l2 <= l1:
                v2 = (l1 - l2 + 1) * "1" + v2
        l1, l2 = len(v1), len(v2)

        if l1 > l2:
            v2 = (l1 - l2) * str(sign2) + v2
        else:
            v1 = (l2 - l1) * str(sign1) + v1

        value1 = v1
        value2 = v2
        v1, v2 = fracpart1, fracpart2
        l1, l2 = len(v1), len(v2)
        if l1 > l2:
            v2 = v2 + (l1 - l2) * "0"
        else:
            v1 = v1 + (l2 - l1) * "0"
        value1 += "." + v1
        value2 += "." + v2
        value1 = value1.rstrip(".")
        value2 = value2.rstrip(".")

        func = (
            __and
            if which == "and"
            else __or
            if which == "or"
            else __xor
            if which == "xor"
            else __and
        )

        def negative(number):
            return Binary(TwosComplement(number))._value
            result = "-"
            if number[0] == "1":
                result += "1" + number.lstrip("1")
            else:
                result += number
            return result

        result = "".join(map(func, zip(value1, value2)))
        if which == "and":
            if sign1 and sign2:
                result = negative(result)
        elif which == "or":
            if sign1 or sign2:
                result = negative(result)
        elif which == "xor":
            if sign1 != sign2:
                result = negative(result)

        return Binary(Binary.simplify(result))

    def __invert__(self: Binary) -> Binary:
        """Returns the 'bitwise not' of self.

        Method that implements the 'bitwise not' operand `~`.
        This is also called the 'invert' operand, or the 'bitwise not' operand.
        Do not confuse it with the 'boolean not' operand implemented
        via the `not` operand and the `__not__()` method.

        It is only defined for integers. If self is not an integer it
        will raise an exception. For integers, `~` is defined as
        `~n = -(n+1)`.

        To perform `~` on a non-integer Binary instance, convert it to
        two's complement string of class `TwosComplement`, adjust that string
        to the desired representation with the desired mantissa and exponent,
        and then perform `TwosComplement.invert()` on that string.
        In short, for non-integer binary fractions, do this:
        `TwosComplement.invert(Binary.to_twoscomplement(value))`.
        Forcing the user to do this, will lead to more awareness of how to represent
        the number before inverting it. If arbitrary Binary or float values were
        allowed to be inverted directly it would lead to unexpected results.
        To avoid confusion this additional 'manual' step was introduced.

        For more information, see also the `TwosComplement.invert()` function.

        Examples:
        * operation ~9 will return -10.
        * operation ~-10 will return 9.

        Parameters:
        self (Binary): number

        Returns:
        Binary: 'bitwise not' (`~`) of integer number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Arguments {self} must be of type Binary.")
        if self._is_special:
            raise ArithmeticError(
                f"ArithmeticError: argument {self} is NaN or infinity."
            )
        # for integers it is defined as -(x+1). So ~9 is -10.
        if Binary.isint(self):
            # for integers ~ is defined as: ~n = - (n+1) formula
            return Binary(-(self._fraction + 1))
        else:
            # For floating point numbers ~ is not defined. What would ~0.5 be?
            # It could be implemented but only if the number of fractional bits is
            # known and managed.
            # ~ of floats would be very difficult to understand and get right as a
            # user. To avoid user error and to avoid introducing ndigits for
            # number of fractional bits it is better to force the user to convert
            # to a twos-complement string and invert (~) this twos-complement formatted
            # string. This avoids the computation of a number representation (float) of
            # an inverted (~) float.

            raise ValueError(
                f"Invalid literal for Binary: {self._value}. "
                "~ operand only allowed on integers and integer fractions. "
                "To perform ~ on Binary, convert it to two's complement string"
                "and then perform invert() on that string. In short, do this: "
                "TwosComplement.invert(Binary.to_twoscomplement(value))."
            )


##########################################################################
# CLASS TESTTWOSCOMPLEMENT
##########################################################################


class TestTwosComplement(unittest.TestCase):
    """Unit testing of class TwosComplement."""

    def selftest(self) -> bool:
        """Perform self test by running various test cases.

        `TwosComplement` uses module `unittest` for unit testing.
        See https://docs.python.org/3/library/unittest.html for details.

        Parameters:
        none

        Returns:
        bool: True if all tests pass, False if any single test fails
        """
        # default would be: unittest.main()
        # This would run all testcase, print resultsm and terminates program.
        # But this would not allow further inspection or tuning.
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTwosComplement)
        test_result = unittest.TextTestRunner().run(suite)
        err = len(test_result.errors)
        fail = len(test_result.failures)
        skip = len(test_result.skipped)
        run = test_result.testsRun
        ttl = suite.countTestCases()
        success = test_result.wasSuccessful()
        print("")
        print(f"Test results for class TwosComplement are: ")
        print(f"    Total number of individual tests = {_BINARY_TOTAL_TESTS}")
        print(f"    Total number of unit tests       = {ttl}")
        print(f"    Unit tests executed              = {run}")
        print(f"    Unit tests skipped               = {skip}")
        print(f"    Unit tests failed                = {fail}")
        print(f"    Unit tests with error            = {err}")
        if success:
            result = f"Self-Test: 😃 All {run} out of {ttl} unit tests passed ✅"
            ret = True
        else:
            plural = "" if run - err - fail == 1 else "s"
            result = f"Self-Test: {run-err-fail} unit test{plural} passed ✅\n"
            plural = "" if err + fail == 1 else "s"
            result += f"Self-Test: {err+fail} unit test{plural} failed  ❌"
            ret = False
        print(f"{result}")
        return ret

    def test___new__(self):
        """Testing the constructor."""
        self.assertIsInstance(TwosComplement(1), TwosComplement)
        self.assertIsInstance(TwosComplement(1.6), TwosComplement)
        self.assertIsInstance(TwosComplement("1.1"), TwosComplement)
        self.assertIsInstance(TwosComplement("1.1e+2"), TwosComplement)
        self.assertTrue("TwosComplement" in str(type(TwosComplement(5))))
        self.assertEqual(TwosComplement(1) + TwosComplement(1), "0101")
        self.assertEqual(len(TwosComplement("1.1")), 3)
        self.assertEqual(str(TwosComplement(+3.5)), "011.1")
        self.assertEqual(TwosComplement(1975), "011110110111")
        self.assertEqual(TwosComplement(1975, 13), "0011110110111")
        self.assertEqual(TwosComplement(-1975), "100001001001")
        self.assertEqual(TwosComplement(-1975, 20), "11111111100001001001")
        self.assertEqual(TwosComplement(+0.375), "0.011")
        self.assertEqual(TwosComplement(-0.375), "1.101")
        with self.assertRaises(ValueError):
            TwosComplement("102")  # should fail
        with self.assertRaises(TypeError):
            TwosComplement(complex(1, 1))  # should fail
        with self.assertRaises(OverflowError):
            TwosComplement(1975, 11)
        with self.assertRaises(OverflowError):
            TwosComplement(-1975, 11)
        with self.assertRaises(ArithmeticError):
            TwosComplement(float("inf"))
        with self.assertRaises(ArithmeticError):
            TwosComplement(float("nan"))
        with self.assertRaises(ValueError):
            TwosComplement("nan")

    def test__int2twoscomp(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement._int2twoscomp(1), str)
        self.assertEqual(TwosComplement._int2twoscomp(8), "01000")
        self.assertEqual(TwosComplement._int2twoscomp(-2), "10")
        self.assertEqual(TwosComplement._int2twoscomp(-0), "0")
        self.assertEqual(TwosComplement._int2twoscomp(-1), "1")
        self.assertEqual(TwosComplement._int2twoscomp(+1), "01")

    def test__frac2twoscomp(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement._frac2twoscomp(1), str)
        self.assertEqual(TwosComplement._frac2twoscomp(0.5), "0.1")
        self.assertEqual(TwosComplement._frac2twoscomp(-0.5), "1.1")
        self.assertEqual(TwosComplement._frac2twoscomp(1.5), "0.1")
        self.assertEqual(TwosComplement._frac2twoscomp(-1.5), "1.1")

    def test__float2twoscomp(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement._float2twoscomp(1.0), str)
        self.assertEqual(TwosComplement._float2twoscomp(0.5), "0.1")
        self.assertEqual(TwosComplement._float2twoscomp(-0.5), "1.1")
        self.assertEqual(TwosComplement._float2twoscomp(1.5), "01.1")
        self.assertEqual(TwosComplement._float2twoscomp(-1.5), "10.1")

    def test__fraction2twoscomp(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement._fraction2twoscomp(Fraction(1, 1)), str)
        self.assertEqual(TwosComplement._fraction2twoscomp(Fraction(1, 2)), "0.1")
        self.assertEqual(TwosComplement._fraction2twoscomp(Fraction(-1, 2)), "1.1")
        self.assertEqual(TwosComplement._fraction2twoscomp(Fraction(3, 2)), "01.1")
        self.assertEqual(TwosComplement._fraction2twoscomp(Fraction(-3, 2)), "10.1")

    def test__str2twoscomp(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement._str2twoscomp("1.0"), str)
        self.assertEqual(TwosComplement._str2twoscomp("0.1"), "0.1")
        self.assertEqual(TwosComplement._str2twoscomp("1.1"), "1.1")
        self.assertEqual(TwosComplement._str2twoscomp("01.1"), "01.1")
        self.assertEqual(TwosComplement._str2twoscomp("10.1"), "10.1")

    def test_istwoscomplement(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement.istwoscomplement("1.0"), bool)
        self.assertEqual(TwosComplement.istwoscomplement("0.1"), True)
        self.assertEqual(TwosComplement.istwoscomplement("0"), True)
        self.assertEqual(TwosComplement.istwoscomplement("1"), True)
        self.assertEqual(TwosComplement.istwoscomplement("0.1"), True)
        self.assertEqual(TwosComplement.istwoscomplement("1.1e+123"), True)
        self.assertEqual(TwosComplement.istwoscomplement("0b0.1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("-0b0.1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("-1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("+1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("0x1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("1"), True)
        self.assertEqual(TwosComplement.istwoscomplement("0b1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("0b01"), False)
        self.assertEqual(TwosComplement.istwoscomplement("0"), True)
        self.assertEqual(TwosComplement.istwoscomplement("1.1"), True)
        self.assertEqual(TwosComplement.istwoscomplement("0.1"), True)
        self.assertEqual(TwosComplement.istwoscomplement("1.1e9"), True)
        self.assertEqual(TwosComplement.istwoscomplement("0.1e8"), True)
        self.assertEqual(TwosComplement.istwoscomplement("1110.1e-19"), True)
        self.assertEqual(TwosComplement.istwoscomplement("00001.1e-18"), True)
        self.assertEqual(TwosComplement.istwoscomplement("1.1e9"), True)
        self.assertEqual(TwosComplement.istwoscomplement("00.001.1e-18"), False)
        self.assertEqual(TwosComplement.istwoscomplement("00e001.1e-18"), False)
        self.assertEqual(TwosComplement.istwoscomplement("8"), False)
        self.assertEqual(TwosComplement.istwoscomplement("Hello"), False)
        self.assertEqual(TwosComplement.istwoscomplement(""), False)
        self.assertEqual(TwosComplement.istwoscomplement("-0b1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("-0b01"), False)
        self.assertEqual(TwosComplement.istwoscomplement("-0"), False)
        self.assertEqual(TwosComplement.istwoscomplement("0b1"), False)
        self.assertEqual(TwosComplement.istwoscomplement("0b01"), False)
        self.assertEqual(TwosComplement.istwoscomplement("inf"), False)
        with self.assertRaises(TypeError):
            TwosComplement.istwoscomplement(1975)  # should fail
        with self.assertRaises(TypeError):
            TwosComplement.istwoscomplement(1.1)  # should fail

    def test_components(self):
        """Test function/method."""
        self.assertEqual(TwosComplement.components("0"), (0, "0", "", 0))
        self.assertEqual(TwosComplement.components("1"), (1, "1", "", 0))
        self.assertEqual(TwosComplement.components("01"), (0, "01", "", 0))
        self.assertEqual(TwosComplement.components("10"), (1, "10", "", 0))
        self.assertEqual(TwosComplement.components("01."), (0, "01", "", 0))
        self.assertEqual(TwosComplement.components("10."), (1, "10", "", 0))
        self.assertEqual(TwosComplement.components("01.0"), (0, "01", "", 0))
        self.assertEqual(TwosComplement.components("10.0"), (1, "10", "", 0))
        self.assertEqual(TwosComplement.components("00001.0"), (0, "01", "", 0))
        self.assertEqual(TwosComplement.components("11110.0"), (1, "10", "", 0))
        self.assertEqual(TwosComplement.components("0.01e-2"), (0, "0", "01", -2))
        self.assertEqual(TwosComplement.components("1.00e-2"), (1, "1", "", -2))
        self.assertEqual(TwosComplement.components("1.01e+2"), (1, "1", "01", 2))
        self.assertEqual(TwosComplement.components("0.01e2"), (0, "0", "01", 2))
        self.assertEqual(TwosComplement.components("101010.e+2"), (1, "101010", "", 2))
        with self.assertRaises(ValueError):
            TwosComplement.components("inf")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.components("-1")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.components("+1")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.components("0b1")  # should fail
        with self.assertRaises(TypeError):
            TwosComplement.components(0.0)  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.components(".01e-2")
        with self.assertRaises(ValueError):
            TwosComplement.components("+0101010e2")

    def test_simplify(self):
        """Test function/method."""
        self.assertEqual(TwosComplement.simplify("0"), "0")
        self.assertEqual(TwosComplement.simplify("1"), "1")
        self.assertEqual(TwosComplement.simplify("01"), "01")
        self.assertEqual(TwosComplement.simplify("10"), "10")
        self.assertEqual(TwosComplement.simplify("001"), "01")
        self.assertEqual(TwosComplement.simplify("110"), "10")
        self.assertEqual(TwosComplement.simplify("01."), "01")
        self.assertEqual(TwosComplement.simplify("10."), "10")
        self.assertEqual(TwosComplement.simplify("01.0"), "01")
        self.assertEqual(TwosComplement.simplify("10.0"), "10")
        self.assertEqual(TwosComplement.simplify("001.00"), "01")
        self.assertEqual(TwosComplement.simplify("110.00"), "10")
        self.assertEqual(TwosComplement.simplify("001.00e0"), "01")
        self.assertEqual(TwosComplement.simplify("110.00e-00"), "10")
        self.assertEqual(TwosComplement.simplify("001.00e+0"), "01")
        self.assertEqual(TwosComplement.simplify("110.00e+000"), "10")
        self.assertEqual(TwosComplement.simplify("001.001"), "01.001")
        self.assertEqual(TwosComplement.simplify("110.001"), "10.001")

    def test_to_fraction(self):
        """Test function/method."""
        self.assertEqual(TwosComplement.to_fraction("0"), Fraction(0, 1))
        self.assertEqual(TwosComplement.to_fraction("1"), Fraction(-1, 1))
        self.assertEqual(TwosComplement.to_fraction("100001001001"), Fraction(-1975, 1))
        self.assertEqual(TwosComplement.to_fraction("011110110111"), Fraction(+1975, 1))
        self.assertEqual(TwosComplement.to_fraction("0.1"), Fraction(1, 2))
        self.assertEqual(TwosComplement.to_fraction("1.1"), Fraction(-1, 2))
        self.assertEqual(TwosComplement.to_fraction("10.1"), Fraction(-3, 2))
        for ii in [
            -8,
            -7.5,
            -4.24,
            -2,
            -1.375,
            -1.0,
            -0.25,
            0,
            0.75,
            1,
            1.875,
            2,
            4.58757,
            7,
            8,
        ]:
            self.assertEqual(TwosComplement(Fraction(ii)).to_fraction(), Fraction(ii))

    def test_to_float(self):
        """Test function/method."""
        self.assertEqual(TwosComplement.to_float("0"), 0.0)
        self.assertEqual(TwosComplement.to_float("1"), -1.0)
        self.assertEqual(TwosComplement.to_float("100001001001"), -1975.0)
        self.assertEqual(TwosComplement.to_float("011110110111"), +1975.0)
        self.assertEqual(TwosComplement.to_float("0.1"), 0.5)
        self.assertEqual(TwosComplement.to_float("1.1"), -0.5)
        self.assertEqual(TwosComplement.to_float("10.1"), -1.5)
        for ii in [
            -8,
            -7.5,
            -4.24,
            -2,
            -1.375,
            -1.0,
            -0.25,
            0,
            0.75,
            1,
            1.875,
            2,
            4.58757,
            7,
            8,
        ]:
            self.assertEqual(TwosComplement(ii).to_float(), ii)

    def test_to_no_mantissa(self):
        """Test function/method."""
        self.assertEqual(TwosComplement.to_no_mantissa("0"), "0")
        self.assertEqual(TwosComplement.to_no_mantissa("01e12"), "01e12")
        self.assertEqual(TwosComplement.to_no_mantissa("01e-12"), "01e-12")
        self.assertEqual(TwosComplement.to_no_mantissa("101e12"), "101e12")
        self.assertEqual(TwosComplement.to_no_mantissa("101e-12"), "101e-12")
        self.assertEqual(TwosComplement.to_no_mantissa("01.e12"), "01e12")
        self.assertEqual(TwosComplement.to_no_mantissa("01.e-12"), "01e-12")
        self.assertEqual(TwosComplement.to_no_mantissa("01.1e12"), "011e11")
        self.assertEqual(TwosComplement.to_no_mantissa("01.1e-12"), "011e-13")
        self.assertEqual(TwosComplement.to_no_mantissa("01.0e12"), "01e12")
        self.assertEqual(TwosComplement.to_no_mantissa("01.0e-12"), "01e-12")
        self.assertEqual(TwosComplement.to_no_mantissa("01.11e12"), "0111e10")
        self.assertEqual(TwosComplement.to_no_mantissa("01.11e-12"), "0111e-14")
        self.assertEqual(TwosComplement.to_no_mantissa("01.01e12"), "0101e10")
        self.assertEqual(TwosComplement.to_no_mantissa("01.01e-12"), "0101e-14")
        self.assertEqual(TwosComplement.to_no_mantissa("01.01e1"), "0101e-1")
        self.assertEqual(TwosComplement.to_no_mantissa("01.01e2"), "0101")

    def test_to_no_exponent(self):
        """Test function/method."""
        self.assertEqual(TwosComplement.to_no_exponent("0"), "0")
        self.assertEqual(TwosComplement.to_no_exponent("1"), "1")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e4"), "10100")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e3"), "1010")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e2"), "101")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e1"), "10.1")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e0"), "1.01")
        self.assertEqual(
            TwosComplement.to_no_exponent("11.01e4", simplify=False), "110100"
        )
        self.assertEqual(
            TwosComplement.to_no_exponent("11.01e3", simplify=False), "11010"
        )
        self.assertEqual(
            TwosComplement.to_no_exponent("11.01e2", simplify=False), "1101"
        )
        self.assertEqual(
            TwosComplement.to_no_exponent("11.01e1", simplify=False), "110.1"
        )
        self.assertEqual(
            TwosComplement.to_no_exponent("11.01e0", simplify=False), "11.01"
        )
        self.assertEqual(TwosComplement.to_no_exponent("11.01e-1"), "1.101")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e-2"), "1.1101")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e-3"), "1.11101")
        self.assertEqual(TwosComplement.to_no_exponent("11.01e-4"), "1.111101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e4"), "0110100")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e3"), "011010")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e2"), "01101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e1"), "0110.1")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e0"), "011.01")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-1"), "01.101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-2"), "0.1101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-3"), "0.01101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-4"), "0.001101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e2"), "01101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e+2"), "01101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e4"), "0110100")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-4"), "0.001101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-2"), "0.1101")
        self.assertEqual(TwosComplement.to_no_exponent("0.1e-1"), "0.01")
        self.assertEqual(TwosComplement.to_no_exponent("1.111e0"), "1.111")
        self.assertEqual(TwosComplement.to_no_exponent("1.11e0"), "1.11")
        self.assertEqual(TwosComplement.to_no_exponent("1.1e0"), "1.1")
        self.assertEqual(TwosComplement.to_no_exponent("1.e0"), "1")
        self.assertEqual(TwosComplement.to_no_exponent("1.e1"), "10")
        self.assertEqual(TwosComplement.to_no_exponent("1.01e2"), "101")
        self.assertEqual(TwosComplement.to_no_exponent("1.01e1"), "10.1")
        self.assertEqual(TwosComplement.to_no_exponent("1.011e2"), "101.1")
        self.assertEqual(TwosComplement.to_no_exponent("1111000e-0"), "1000")
        self.assertEqual(TwosComplement.to_no_exponent("1111000e-3"), "1")
        self.assertEqual(TwosComplement.to_no_exponent("1111000000.e-3"), "1000")
        self.assertEqual(TwosComplement.to_no_exponent("1111000e+3"), "1000000")
        self.assertEqual(TwosComplement.to_no_exponent("1111e+3"), "1000")
        self.assertEqual(TwosComplement.to_no_exponent("1111.1e+3"), "100")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-02"), "0.1101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-02", -1), "0.1101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-02", 7), "00.1101")
        self.assertEqual(TwosComplement.to_no_exponent("011.01e-02", 8), "000.1101")
        self.assertEqual(TwosComplement.to_no_exponent("0.01"), "0.01")
        self.assertEqual(TwosComplement.to_no_exponent("1.111"), "1.111")
        self.assertEqual(TwosComplement.to_no_exponent("1.11"), "1.11")
        self.assertEqual(TwosComplement.to_no_exponent("1.1"), "1.1")
        self.assertEqual(TwosComplement.to_no_exponent("111"), "1")
        self.assertEqual(TwosComplement.to_no_exponent("10.000"), "10")
        self.assertEqual(TwosComplement.to_no_exponent("101.000e0"), "101")
        self.assertEqual(TwosComplement.to_no_exponent("10.10"), "10.1")
        self.assertEqual(TwosComplement.to_no_exponent("101.1e-0"), "101.1")
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("0b1")  # leading 0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("0b01")  # leading 0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("-0b1")  # leading -0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("-0b01")  # leading -0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("-1")  # leading - not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("1", 0)  # should fail
        with self.assertRaises(OverflowError):
            TwosComplement.to_no_exponent("11100", 1)  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("111", 0)  # should fail
        with self.assertRaises(OverflowError):
            TwosComplement.to_no_exponent("0111", 2)  # should fail
        with self.assertRaises(OverflowError):
            TwosComplement.to_no_exponent("011.01e-02", 5)
        with self.assertRaises(ValueError):
            TwosComplement.to_no_exponent("-0b10")  # should fail
        with self.assertRaises(TypeError):
            TwosComplement.to_no_exponent(1)  # should fail
        with self.assertRaises(TypeError):
            TwosComplement.to_no_exponent("1", "-1")  # should fail

    def test_invert(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement.invert("1"), str)
        self.assertIsInstance(
            TwosComplement.invert(TwosComplement("1")), TwosComplement
        )
        self.assertIsInstance(TwosComplement("1").invert(), TwosComplement)
        self.assertEqual(TwosComplement.invert("0001000", False), "1110111")
        self.assertEqual(TwosComplement.invert("0001000", simplify=True), "10111")
        self.assertEqual(TwosComplement.invert("1110110", simplify=True), "01001")
        self.assertEqual(TwosComplement.invert("0.1101", simplify=False), "1.0010")
        self.assertEqual(TwosComplement.invert("0.1101", simplify=True), "1.001")
        self.assertEqual(TwosComplement.invert("11.1101", simplify=True), "0.001")
        self.assertEqual(TwosComplement.invert("00.1101", simplify=True), "1.001")
        self.assertEqual(TwosComplement.invert("01"), "10")
        self.assertEqual(TwosComplement.invert("0"), "1")
        self.assertEqual(TwosComplement.invert("1"), "0")
        self.assertEqual(TwosComplement.invert("10"), "01")
        self.assertEqual(TwosComplement.invert("101"), "010")
        self.assertEqual(TwosComplement.invert("101010"), "010101")
        self.assertEqual(TwosComplement.invert("0101010"), "1010101")
        self.assertEqual(TwosComplement.invert("101.010"), "010.101")
        self.assertEqual(TwosComplement.invert("010.1010"), "101.0101")
        self.assertEqual(TwosComplement.invert("1e1"), "0.1e1")
        self.assertEqual(
            TwosComplement("1e1", simplify=False).invert().to_no_exponent(), "01"
        )
        self.assertEqual(
            TwosComplement.invert("0101010e-3", simplify=False), "1010101e-3"
        )
        self.assertEqual(TwosComplement.invert("0101010e-3"), "1010101e-3")
        self.assertEqual(TwosComplement.invert("1010101e0"), "0101010")
        self.assertEqual(TwosComplement.invert("0101010e-0"), "1010101")
        self.assertEqual(TwosComplement.invert("1010101e-34"), "0101010e-34")
        self.assertEqual(TwosComplement.invert("0101010e-34"), "1010101e-34")
        self.assertEqual(
            TwosComplement.invert("010101e34"),
            "101010.1111111111111111111111111111111111e34",
        )
        self.assertEqual(
            TwosComplement("010101e34").invert().to_no_exponent(),
            "1010101111111111111111111111111111111111",
        )
        self.assertEqual(
            TwosComplement.invert("101010e34"),
            "010101.1111111111111111111111111111111111e34",
        )
        self.assertEqual(
            TwosComplement("101010e34").invert().to_no_exponent(),
            "0101011111111111111111111111111111111111",
        )
        self.assertEqual(TwosComplement.invert("010.1010e-34"), "101.0101e-34")

        self.assertEqual(
            TwosComplement.invert("101.010e34"),
            "010.1011111111111111111111111111111111e34",
        )
        self.assertEqual(
            TwosComplement("101.010e34").invert().to_no_exponent(),
            "0101011111111111111111111111111111111",
        )
        self.assertEqual(
            TwosComplement.invert("101.010e1", simplify=False), "010.101e1"
        )
        self.assertEqual(
            TwosComplement("101.010e1", simplify=False)
            .invert(simplify=False)
            .to_no_exponent(),
            "0101.01",
        )
        self.assertEqual(
            TwosComplement("101.010e1", simplify=False).invert(simplify=False),
            "010.101e1",
        )
        self.assertEqual(
            TwosComplement.invert("101.010e1", simplify=False), "010.101e1"
        )
        self.assertEqual(
            TwosComplement("101.010e1", simplify=False)
            .invert(simplify=False)
            .to_no_exponent(),
            "0101.01",
        )
        self.assertEqual(TwosComplement.invert("101.010e0"), "010.101")
        self.assertEqual(
            TwosComplement.invert(TwosComplement.invert("0101010e-34")), "0101010e-34"
        )
        self.assertEqual(
            TwosComplement.invert(TwosComplement.invert("101010e34")),
            "101010e34",
        )
        self.assertEqual(
            TwosComplement("101010e34").invert().invert().to_no_exponent(),
            "1010100000000000000000000000000000000000",
        )
        with self.assertRaises(ValueError):
            TwosComplement.invert("1975")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.invert("1.1.")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.invert("1e")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.invert("1e2e3")  # should fail
        with self.assertRaises(TypeError):
            TwosComplement.invert(1975)  # should fail
        with self.assertRaises(ArithmeticError):
            TwosComplement.invert("Inf")
        with self.assertRaises(ArithmeticError):
            TwosComplement.invert("-inf")
        with self.assertRaises(ArithmeticError):
            TwosComplement.invert("nan")


##########################################################################
# CLASS TESTBINARY
##########################################################################


class TestBinary(unittest.TestCase):
    """Unit testing of class Binary."""

    def selftest(self) -> bool:
        """Perform self test by running various test cases.

        `Binary` uses module `unittest` for unit testing.
        See https://docs.python.org/3/library/unittest.html for details.

        Parameters:
        none

        Returns:
        bool: True if all tests pass, False if any single test fails
        """
        # default would be: unittest.main()
        # This would run all testcase, print resultsm and terminates program.
        # But this would not allow further inspection or tuning.
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBinary)
        test_result = unittest.TextTestRunner().run(suite)
        err = len(test_result.errors)
        fail = len(test_result.failures)
        skip = len(test_result.skipped)
        run = test_result.testsRun
        ttl = suite.countTestCases()
        success = test_result.wasSuccessful()
        print("")
        print(f"Test results for class Binary are: ")
        print(f"    Total number of individual tests = {_BINARY_TOTAL_TESTS}")
        print(f"    Total number of unit tests       = {ttl}")
        print(f"    Unit tests executed              = {run}")
        print(f"    Unit tests skipped               = {skip}")
        print(f"    Unit tests failed                = {fail}")
        print(f"    Unit tests with error            = {err}")
        if success:
            result = f"Self-Test: 😃 All {run} out of {ttl} unit tests passed ✅"
            ret = True
        else:
            plural = "" if run - err - fail == 1 else "s"
            result = f"Self-Test: {run-err-fail} unit test{plural} passed ✅\n"
            plural = "" if err + fail == 1 else "s"
            result += f"Self-Test: {err+fail} unit test{plural} failed  ❌"
            ret = False
        print(f"{result}")
        return ret

    def test___new__(self):
        """Testing the constructor."""
        self.assertIsInstance(Binary(1), Binary)
        self.assertIsInstance(Binary(1.5), Binary)
        self.assertIsInstance(Binary("0110"), Binary)
        self.assertIsInstance(Binary("0110.010e-23"), Binary)
        self.assertIsInstance(Binary(TwosComplement(1)), Binary)
        self.assertTrue("Binary" in str(type(Binary(5))))
        self.assertEqual(float(Binary("0")), 0.0)
        self.assertEqual(float(Binary("1.1")), 1.5)
        self.assertEqual(float(Binary("-1.11")), -1.75)
        self.assertEqual(Binary("0b1.1"), "1.1")
        self.assertEqual(Binary("-0b1.1"), "-1.1")
        self.assertEqual(Binary(-3.5), "-11.1")
        self.assertEqual(Binary(-3.5), "-0b11.1")
        self.assertEqual(str(Binary(-3.5)), "-0b11.1")
        self.assertEqual(
            Binary((1, (1, 0, 1, 0), -2)).compare_representation("-1010e-2"), True
        )
        self.assertEqual(Binary(TwosComplement(0)), 0)
        self.assertEqual(Binary(TwosComplement(1)), 1)
        self.assertEqual(Binary(TwosComplement(2)), 2)
        self.assertEqual(Binary(TwosComplement(-1)), -1)
        self.assertEqual(Binary(TwosComplement(-2)), -2)
        self.assertEqual(Binary(TwosComplement(-1975)), -1975)
        self.assertEqual(Binary(TwosComplement(1975)), 1975)
        self.assertEqual(Binary(TwosComplement("01")), 1)
        self.assertEqual(Binary(TwosComplement("1")), -1)
        self.assertEqual(Binary(TwosComplement("10")), -2)
        with self.assertRaises(ValueError):
            Binary("102")  # should fail
        with self.assertRaises(TypeError):
            Binary(complex(1, 1))  # should fail

    def test_version(self):
        """Testing the version method."""
        self.assertIsInstance(Binary.version(), str)
        self.assertEqual(len(Binary.version()), len("20210622-103815"))
        self.assertEqual(Binary.version()[8], "-")
        self.assertEqual(Binary.version()[0:2], "20")  # YY

    def test_to_float(self):
        """Test to_float() function."""
        self.assertIsInstance(Binary.to_float("1"), int)
        self.assertIsInstance(Binary.to_float("1.1"), float)
        self.assertEqual(Binary.to_float("inf"), float("inf"))
        self.assertEqual(Binary.to_float("-inf"), float("-inf"))
        self.assertEqual(math.isnan(Binary.to_float("-nan")), True)
        self.assertEqual(Binary.to_float("-0b11.1"), -3.5)
        self.assertEqual(Binary.to_float("0b0"), 0)
        self.assertEqual(Binary.to_float("0b1000.01"), 8.25)
        with self.assertRaises(ValueError):
            Binary.to_float("2")  # should fail

    def test_from_float(self):
        """Testing from_float() function."""
        self.assertIsInstance(Binary.from_float(1.0), str)
        self.assertEqual(Binary.from_float(float("inf")), "inf")
        self.assertEqual(Binary.from_float(float("-inf")), "-inf")
        self.assertEqual(Binary.from_float(float("-nan")), "nan")
        self.assertEqual(Binary.from_float(-3.5), "-0b11.1")
        self.assertEqual(Binary.from_float(-0.0), "0b0")
        self.assertEqual(Binary.from_float(8.25), "0b1000.01")
        with self.assertRaises(TypeError):
            Binary.from_float("1")  # should fail

    def test_to_no_exponent(self):
        """Test function/method."""
        self.assertIsInstance(Binary.to_no_exponent("1"), str)
        self.assertIsInstance(Binary.to_no_exponent(Binary("1")), Binary)
        self.assertIsInstance(Binary("1").to_no_exponent(), Binary)
        self.assertEqual(Binary.to_no_exponent("0"), "0")
        self.assertEqual(Binary.to_no_exponent("1"), "1")
        self.assertEqual(Binary.to_no_exponent("11.01e4"), "110100")
        self.assertEqual(Binary.to_no_exponent("11.01e3"), "11010")
        self.assertEqual(Binary.to_no_exponent("11.01e2"), "1101")
        self.assertEqual(Binary.to_no_exponent("11.01e1"), "110.1")
        self.assertEqual(Binary.to_no_exponent("11.01e0"), "11.01")
        self.assertEqual(Binary.to_no_exponent("11.01e4", simplify=False), "110100")
        self.assertEqual(Binary.to_no_exponent("11.01e3", simplify=False), "11010")
        self.assertEqual(Binary.to_no_exponent("11.01e2", simplify=False), "1101")
        self.assertEqual(Binary.to_no_exponent("11.01e1", simplify=False), "110.1")
        self.assertEqual(Binary.to_no_exponent("11.01e0", simplify=False), "11.01")
        self.assertEqual(Binary.to_no_exponent("11.01e-1"), "1.101")
        self.assertEqual(Binary.to_no_exponent("11.01e-2"), "0.1101")
        self.assertEqual(Binary.to_no_exponent("11.01e-3"), "0.01101")
        self.assertEqual(Binary.to_no_exponent("11.01e-4"), "0.001101")
        self.assertEqual(Binary.to_no_exponent("011.01e4"), "110100")
        self.assertEqual(Binary.to_no_exponent("011.01e3"), "11010")
        self.assertEqual(Binary.to_no_exponent("011.01e2"), "1101")
        self.assertEqual(Binary.to_no_exponent("011.01e1"), "110.1")
        self.assertEqual(Binary.to_no_exponent("011.01e0"), "11.01")
        self.assertEqual(Binary.to_no_exponent("011.01e-1"), "1.101")
        self.assertEqual(Binary.to_no_exponent("011.01e-2"), "0.1101")
        self.assertEqual(Binary.to_no_exponent("011.01e-3"), "0.01101")
        self.assertEqual(Binary.to_no_exponent("011.01e-4"), "0.001101")
        self.assertEqual(Binary.to_no_exponent("011.01e2"), "1101")
        self.assertEqual(Binary.to_no_exponent("011.01e+2"), "1101")
        self.assertEqual(Binary.to_no_exponent("011.01e4"), "110100")
        self.assertEqual(Binary.to_no_exponent("011.01e-4"), "0.001101")
        self.assertEqual(Binary.to_no_exponent("011.01e-2"), "0.1101")
        self.assertEqual(Binary.to_no_exponent("0.1e-1"), "0.01")
        self.assertEqual(Binary.to_no_exponent("1.111e0"), "1.111")
        self.assertEqual(Binary.to_no_exponent("1.11e0"), "1.11")
        self.assertEqual(Binary.to_no_exponent("1.1e0"), "1.1")
        self.assertEqual(Binary.to_no_exponent("1.e0"), "1")
        self.assertEqual(Binary.to_no_exponent("1.e1"), "10")
        self.assertEqual(Binary.to_no_exponent("1.01e2"), "101")
        self.assertEqual(Binary.to_no_exponent("1.01e1"), "10.1")
        self.assertEqual(Binary.to_no_exponent("1.011e2"), "101.1")
        self.assertEqual(Binary.to_no_exponent("1111000e-0"), "1111000")
        self.assertEqual(Binary.to_no_exponent("1111000e-3"), "1111")
        self.assertEqual(Binary.to_no_exponent("1111000000.e-3"), "1111000")
        self.assertEqual(Binary.to_no_exponent("1111000e+3"), "1111000000")
        self.assertEqual(Binary.to_no_exponent("1111e+3"), "1111000")
        self.assertEqual(Binary.to_no_exponent("1111.1e+3"), "1111100")
        self.assertEqual(Binary.to_no_exponent("011.01e-02"), "0.1101")
        self.assertEqual(
            Binary.to_no_exponent("011.01e-02", add_prefix=True), "0b0.1101"
        )
        self.assertEqual(Binary.to_no_exponent("011.01e-02", length=-1), "0.1101")
        self.assertEqual(Binary.to_no_exponent("011.01e-02", length=7), "00.1101")
        self.assertEqual(Binary.to_no_exponent("011.01e-02", length=8), "000.1101")
        self.assertEqual(Binary.to_no_exponent("0.01"), "0.01")
        self.assertEqual(Binary.to_no_exponent("1.111"), "1.111")
        self.assertEqual(Binary.to_no_exponent("1.11"), "1.11")
        self.assertEqual(Binary.to_no_exponent("1.1"), "1.1")
        self.assertEqual(Binary.to_no_exponent("111"), "111")
        self.assertEqual(Binary.to_no_exponent("10.000"), "10")
        self.assertEqual(Binary.to_no_exponent("101.000e0"), "101")
        self.assertEqual(Binary.to_no_exponent("10.10"), "10.1")
        self.assertEqual(Binary.to_no_exponent("101.1e-0"), "101.1")
        self.assertEqual(Binary.to_no_exponent("-0"), "0")
        self.assertEqual(Binary.to_no_exponent("11.01e-2"), "0.1101")
        self.assertEqual(Binary.to_no_exponent("-11.01e-2"), "-0.1101")
        self.assertEqual(Binary.to_no_exponent("-11.01e-3"), "-0.01101")
        self.assertEqual(Binary.to_no_exponent("-11.01e-4"), "-0.001101")
        self.assertEqual(Binary.to_no_exponent("11.01e2"), "1101")
        self.assertEqual(Binary.to_no_exponent("-11.01e+2"), "-1101")
        self.assertEqual(Binary.to_no_exponent("11.01e4"), "110100")
        self.assertEqual(Binary.to_no_exponent("-11.01e+4"), "-110100")
        self.assertEqual(Binary.to_no_exponent("11.01e4", add_prefix=True), "0b110100")
        self.assertEqual(
            Binary.to_no_exponent("-11.01e+4", add_prefix=True), "-0b110100"
        )
        self.assertEqual(Binary.to_no_exponent(Binary("Inf")), "Infinity")
        self.assertEqual(Binary.to_no_exponent(Binary("-0")), "0b0")
        self.assertEqual(Binary.to_no_exponent(Binary("-0"), add_prefix=True), "0b0")
        self.assertEqual(Binary.to_no_exponent(Binary("11.01e-2")), "0b0.1101")
        self.assertEqual(Binary.to_no_exponent(Binary("-11.01e-2")), "-0b0.1101")
        self.assertEqual(Binary.to_no_exponent(Binary("-11.01e-3")), "-0b0.01101")
        self.assertEqual(Binary.to_no_exponent(Binary("-11.01e-4")), "-0b0.001101")
        self.assertEqual(Binary.to_no_exponent(Binary("11.01e2")), "0b1101")
        self.assertEqual(Binary.to_no_exponent(Binary("-11.01e+2")), "-0b1101")
        self.assertEqual(Binary.to_no_exponent(Binary("11.01e4")), "0b110100")
        self.assertEqual(Binary.to_no_exponent(Binary("-11.01e+4")), "-0b110100")
        with self.assertRaises(ValueError):
            Binary.to_no_exponent("")  # should fail
        with self.assertRaises(TypeError):
            Binary.to_no_exponent(1)  # should fail
        with self.assertRaises(OverflowError):
            Binary.to_no_exponent("1", length=0)  # should fail
        with self.assertRaises(OverflowError):
            Binary.to_no_exponent("11100", length=4)  # should fail
        with self.assertRaises(OverflowError):
            Binary.to_no_exponent("0011", length=1)  # should fail
        with self.assertRaises(OverflowError):
            Binary.to_no_exponent("0111", length=2)  # should fail
        with self.assertRaises(OverflowError):
            Binary.to_no_exponent("011.01e-02", length=4)
        with self.assertRaises(TypeError):
            Binary.to_no_exponent("1", "-1")  # should fail

    def test___float__(self):
        """Test __float__() method."""
        self.assertEqual(float(Binary("-1")), -1.0)
        self.assertEqual(float(Binary("-1.1")), -1.5)
        self.assertEqual(float(Binary("1.001")), 1.125)
        self.assertEqual(float(Binary((1, (1, 0, 1, 0), -2))), -2.5)
        self.assertEqual(float(Binary(-13.0 - 2 ** -10)), -13.0009765625)
        self.assertEqual(float(Binary(13.0 + 2 ** -20)), 13.000000953674316)
        self.assertEqual(float(Binary(13.0 + 2 ** -30)), 13.000000000931323)
        self.assertEqual(float(Binary("Inf")), float("Inf"))

    def test___int__(self):
        """Test __int__() method."""
        self.assertEqual(int(Binary("-1")), -1)
        self.assertEqual(int(Binary("-1.111")), -1)
        self.assertEqual(int(Binary("1.001")), 1)
        self.assertEqual(int(Binary((1, (1, 0, 1, 0), -2))), -2)
        self.assertEqual(int(Binary(-13.0 - 2 ** -10)), -13)
        self.assertEqual(int(Binary(13.0 + 2 ** -20)), 13)
        self.assertEqual(int(Binary(13.0 + 2 ** -30)), 13)
        with self.assertRaises(ValueError):
            int(Binary("Inf"))  # should fail

    def test___str__(self):
        """Test __str__() method."""
        self.assertEqual(str(Binary("-1")), "-0b1")
        self.assertEqual(str(Binary("-1.111")), "-0b1.111")
        self.assertEqual(str(Binary("1.001")), "0b1.001")
        self.assertEqual(str(Binary((1, (1, 0, 1, 0), -2))), "-0b1010e-2")
        self.assertEqual(str(Binary(-13.0 - 2 ** -10)), "-0b1101.0000000001")
        self.assertEqual(str(Binary(13.0 + 2 ** -20)), "0b1101.00000000000000000001")
        self.assertEqual(
            str(Binary(13.0 + 2 ** -30)), "0b1101.000000000000000000000000000001"
        )
        self.assertEqual(str(Binary("Nan")), _NAN)
        self.assertEqual(str(Binary("inf")), _INF)
        self.assertEqual(str(Binary("-inf")), _NINF)
        with self.assertRaises(ValueError):
            str(Binary("Info"))  # should fail

    def test_compare_representation(self):
        """Test function/method."""
        self.assertEqual(
            Binary(10.10).compare_representation(
                "1010.0001100110011001100110011001100110011001100110011"
            ),
            True,
        )
        self.assertEqual(Binary("10.111").compare_representation("10.111"), True)
        self.assertEqual(Binary(5).compare_representation("101"), True)
        self.assertEqual(
            Binary(8.3).compare_representation(
                "1000.010011001100110011001100110011001100110011001101"
            ),
            True,
        )
        self.assertEqual(Binary(0.0).compare_representation("0"), True)
        self.assertEqual(Binary(1.0).compare_representation("1"), True)
        self.assertEqual(Binary(3.5).compare_representation("11.1"), True)
        self.assertEqual(Binary(-13.75).compare_representation("-1101.11"), True)
        self.assertEqual(
            Binary(13.0 + 2 ** -10).compare_representation("1101.0000000001"), True
        )
        self.assertEqual(
            Binary(13.0 + 2 ** -20).compare_representation("1101.00000000000000000001"),
            True,
        )
        self.assertEqual(
            Binary(13.0 + 2 ** -30).compare_representation(
                "1101.000000000000000000000000000001"
            ),
            True,
        )
        self.assertEqual(
            Binary(13.0 + 2 ** -40).compare_representation(
                "1101.0000000000000000000000000000000000000001"
            ),
            True,
        )
        self.assertEqual(Binary(13.0 + 2 ** -50).compare_representation("1101"), True)
        self.assertEqual(Binary(13.0 + 2 ** -60).compare_representation("1101"), True)
        self.assertEqual(
            Binary(
                13.0
                + 2 ** -10
                + 2 ** -20
                + 2 ** -30
                + 2 ** -40
                + 2 ** -50
                + 2 ** -60
                + 2 ** -70
            ).compare_representation("1101.0000000001000000000100000000010000000001"),
            True,
        )
        self.assertEqual(Binary("1.1").round(1).compare_representation("1.1"), True)
        self.assertEqual(Binary("1.10").round(1).compare_representation("1.1"), True)
        self.assertEqual(Binary("1.101").round(1).compare_representation("1.1"), True)
        self.assertEqual(Binary("1.11").round(1).compare_representation("1.1"), True)
        self.assertEqual(Binary("1.110").round(1).compare_representation("1.1"), True)
        self.assertEqual(Binary("1.1101").round(1).compare_representation("10"), True)
        self.assertEqual(Binary("1.1111").round(1).compare_representation("10"), True)
        with self.assertRaises(TypeError):
            Binary.compare_representation(1, "1")  # should fail

    def test_no_prefix(self):
        """Test function/method."""
        self.assertEqual(Binary(-3.5).no_prefix(), "-11.1")
        self.assertEqual(Binary.no_prefix(Binary(-3.5)), "-11.1")
        self.assertEqual(Binary.no_prefix("-11.1"), "-11.1")
        self.assertEqual(Binary.no_prefix("-0b11.1"), "-11.1")
        self.assertEqual(Binary.no_prefix("0b11.1"), "11.1")
        self.assertEqual(Binary.no_prefix("+0b11.1"), "+11.1")
        with self.assertRaises(TypeError):
            Binary.no_prefix(1.5)  # should fail, 1 arg too much

    def test_np(self):
        """Test function/method."""
        self.assertEqual(Binary(-5.5).np(), "-101.1")
        self.assertEqual(Binary.np(Binary(-3.5)), "-11.1")
        with self.assertRaises(TypeError):
            Binary.np(1.5)  # should fail, 1 arg too much

    def test_simplify(self):
        """Test function simplify()."""
        self.assertEqual(Binary.simplify("-0"), "0")
        self.assertEqual(Binary.simplify("-000"), "0")
        self.assertEqual(Binary.simplify("-000.00"), "0")
        self.assertEqual(Binary.simplify("-000.00e-10"), "0")
        self.assertEqual(Binary.simplify("-1e-0"), "-1")
        self.assertEqual(Binary.simplify("-010"), "-10")
        self.assertEqual(Binary.simplify("-0010"), "-10")
        self.assertEqual(Binary.simplify("-0010.00"), "-10")
        self.assertEqual(Binary.simplify("-0010.00e-10"), "-10e-10")
        self.assertEqual(Binary.simplify("-101.01e-0"), "-101.01")
        self.assertEqual(Binary.simplify("-1e-0", True), "-0b1")
        self.assertEqual(Binary.simplify("-010", True), "-0b10")
        self.assertEqual(Binary.simplify("-0010", True), "-0b10")
        self.assertEqual(Binary.simplify("-0010.00", True), "-0b10")
        self.assertEqual(Binary.simplify("-0010.00e-10", True), "-0b10e-10")
        self.assertEqual(Binary.simplify("101.01e-0", True), "0b101.01")
        with self.assertRaises(TypeError):
            Binary.simplify(1)  # should fail
        with self.assertRaises(TypeError):
            Binary.simplify(Binary("Inf"))  # should fail

    def test_to_fraction(self):
        """Test function/method."""
        self.assertIsInstance(Binary.to_fraction("1"), Fraction)
        self.assertEqual(Binary.to_fraction("1"), Fraction(1))
        self.assertEqual(Binary.to_fraction("0"), Fraction(0))
        self.assertEqual(Binary.to_fraction("0.1"), Fraction(0.5))
        self.assertEqual(Binary.to_fraction("1.1"), Fraction(1.5))
        self.assertEqual(Binary.to_fraction("1.1"), Fraction(1.5))
        self.assertEqual(Binary.to_fraction("-1"), Fraction(-1))
        self.assertEqual(Binary.to_fraction("-0.1"), Fraction(-0.5))
        self.assertEqual(Binary.to_fraction("-1.1"), Fraction(-1.5))
        self.assertEqual(Binary.to_fraction("-1.1e2"), Fraction(-6))
        self.assertEqual(Binary.to_fraction("-1.1e0"), Fraction(-1.5))
        self.assertEqual(Binary.to_fraction("1.1e-3"), Fraction(3, 16))
        self.assertEqual(Binary.to_fraction("-1.1e-3"), Fraction(-3, 16))
        self.assertEqual(Binary.to_fraction("0"), Fraction(0))
        self.assertEqual(Binary.to_fraction("1"), Fraction(1))
        self.assertEqual(Binary.to_fraction("-0"), Fraction(0))
        self.assertEqual(Binary.to_fraction("-1"), Fraction(-1))
        self.assertEqual(Binary.to_fraction("11"), Fraction(3))
        self.assertEqual(Binary.to_fraction("-0.0"), Fraction(0))
        self.assertEqual(Binary.to_fraction("1.0"), Fraction(1))
        self.assertEqual(Binary.to_fraction("1.1"), Fraction(3, 2))
        self.assertEqual(Binary.to_fraction("-1.1"), Fraction(3, -2))
        self.assertEqual(Binary.to_fraction("-0.111"), Fraction(-0.875))
        self.assertEqual(
            Binary.to_fraction("1.1" + "0" * 2 + "1"),
            Fraction(3 * 2 ** 3 + 1, 2 ** 4),
        )
        self.assertEqual(
            Binary.to_fraction("1.1" + "0" * 100 + "1"),
            Fraction(3 * 2 ** 101 + 1, 2 ** 102),
        )
        self.assertEqual(
            Binary.to_fraction("1.1" + "0" * 1000 + "1"),
            Fraction(3 * 2 ** 1001 + 1, 2 ** 1002),
        )
        self.assertEqual(Binary.to_fraction(Binary("-0.111")), Fraction(-0.875))
        with self.assertRaises(ValueError):
            Binary.to_fraction("102")  # should fail
        with self.assertRaises(TypeError):
            Binary.to_fraction(1)  # should fail

    def test___round__(self):
        """Test function/method for rounding."""
        self.assertIsInstance(round(Binary(3.75), 1), Binary)
        self.assertEqual(round(Binary(3.75), 1), "11.1")
        self.assertEqual(round(Binary(3.75), 1), "11.1")
        self.assertEqual(round(Binary(3.75001), 1), "100.0")
        self.assertEqual(round(Binary(3.75), 2), "11.11")
        self.assertEqual(round(Binary(3.75001), 2), "11.11")
        self.assertEqual(round(Binary(-3.75), 1), "-11.1")
        self.assertEqual(round(Binary(-3.75001), 1), "-100.0")
        self.assertEqual(round(Binary(-3.75), 2), "-11.11")
        self.assertEqual(round(Binary(-3.75001), 2), "-11.11")
        self.assertEqual(round(Binary("0.1")), "0")
        self.assertEqual(round(Binary("0.10000001"), 0), "1")
        with self.assertRaises(ValueError):
            round(Binary("0.1"), -1)  # should fail
        with self.assertRaises(TypeError):
            round(Binary("0.1"), "0")  # should fail

    def test_round(self):
        """Test function/method for rounding."""
        self.assertIsInstance(Binary(3.75).round(1), Binary)
        self.assertEqual(Binary(3.75).round(1), "11.1")
        self.assertEqual(Binary(3.75001).round(1), "100.0")
        self.assertEqual(Binary(3.75).round(2), "11.11")
        self.assertEqual(Binary(3.75001).round(2), "11.11")
        self.assertEqual(Binary(-3.75).round(1), "-11.1")
        self.assertEqual(Binary(-3.75001).round(1), "-100.0")
        self.assertEqual(Binary(-3.75).round(2), "-11.11")
        self.assertEqual(Binary(-3.75001).round(2), "-11.11")
        self.assertEqual(Binary("0.1").round(), "0")
        self.assertEqual(Binary("0.10000001").round(0), "1")
        with self.assertRaises(ValueError):
            Binary("0.1").round(-1)  # should fail
        with self.assertRaises(TypeError):
            Binary("0.1").round("0")  # should fail

    def test_round_to(self):
        """Test function/method for rounding."""
        self.assertEqual(Binary.round_to("11.01e-99", 2), "0")
        self.assertEqual(Binary.round_to("11.01e+9", 2), "11010000000")
        self.assertEqual(Binary.round_to("11.01e-2", 2), "0.11")
        self.assertEqual(Binary.round_to("0.1", 0), "0")
        self.assertEqual(Binary.round_to("0.10000001", 0), "1")
        with self.assertRaises(TypeError):
            Binary.round_to(Binary(1), 0)  # should fail
        with self.assertRaises(TypeError):
            Binary.round_to("1", 0.0)  # should fail
        with self.assertRaises(ValueError):
            Binary.round_to("111", -2)  # should fail
        with self.assertRaises(ValueError):
            Binary.round_to("nan", 2)  # should fail
        with self.assertRaises(OverflowError):
            Binary.round_to("Inf", 2)  # should fail
        with self.assertRaises(OverflowError):
            Binary.round_to("-Inf", 0)  # should fail

    def test_fill(self):
        """Test function/method."""
        self.assertIsInstance(Binary(1).fill(1), Binary)
        self.assertIsInstance(Binary.fill_to("1", 1), str)
        self.assertEqual(Binary("1.1111").fill(1), "1.1111")
        self.assertEqual(Binary("1.1111").fill(4), "1.1111")
        self.assertEqual(Binary("1.1111").fill(5), "1.11110")
        self.assertEqual(Binary("1.1111").fill(6), "1.111100")
        self.assertEqual(Binary("1.1111").fill(1, True), "10.0")
        self.assertEqual(Binary("1.1111").fill(4, True), "1.1111")
        self.assertEqual(Binary("1.1111").fill(5, True), "1.11110")
        self.assertEqual(Binary("1.1111").fill(6, True), "1.111100")
        self.assertEqual(Binary("1.0011").fill(1, True), "1.0")
        with self.assertRaises(TypeError):
            Binary.fill(1, "1")  # should fail
        with self.assertRaises(ValueError):
            Binary(1).fill(-1)  # should fail

    def test_fill_to(self):
        """Test function/method."""
        self.assertIsInstance(Binary.fill_to("1", 1), str)
        self.assertEqual(Binary.fill_to("1.1111", 1), "1.1111")
        self.assertEqual(Binary.fill_to("1.1111", 4), "1.1111")
        self.assertEqual(Binary.fill_to("1.1111", 5), "1.11110")
        self.assertEqual(Binary.fill_to("1.1111", 6), "1.111100")
        self.assertEqual(Binary.fill_to("1.1111", 1, True), "10.0")
        self.assertEqual(Binary.fill_to("1.1111", 4, True), "1.1111")
        self.assertEqual(Binary.fill_to("1.1111", 5, True), "1.11110")
        self.assertEqual(Binary.fill_to("1.1111", 6, True), "1.111100")
        self.assertEqual(Binary.fill_to("1.0011", 1, True), "1.0")
        with self.assertRaises(TypeError):
            Binary.fill_to(1, "1")  # should fail
        with self.assertRaises(ValueError):
            Binary.fill_to("1", -1)  # should fail
        with self.assertRaises(OverflowError):
            Binary.fill_to("-Inf")  # should fail

    def test_to_no_mantissa(self):
        """Test function/method."""
        self.assertEqual(
            Binary("-11").to_no_mantissa().compare_representation("-11e0"),
            True,
        )
        self.assertEqual(
            Binary("-11e-0").to_no_mantissa().compare_representation("-11e0"),
            True,
        )
        self.assertEqual(
            Binary("-11e+0").to_no_mantissa().compare_representation("-11e0"),
            True,
        )
        self.assertEqual(
            Binary("+11").to_no_mantissa().compare_representation("11e0"),
            True,
        )
        self.assertEqual(
            Binary("1.1").to_no_mantissa().compare_representation("11e-1"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_no_mantissa().compare_representation("-1e-4"),
            True,
        )
        self.assertEqual(
            Binary("-1.1").to_no_mantissa().compare_representation("-11e-1"),
            True,
        )
        self.assertEqual(
            Binary("-1.1e-1").to_no_mantissa().compare_representation("-11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+1.1e-1").to_no_mantissa().compare_representation("11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+1.1000e-1").to_no_mantissa().compare_representation("11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+0001.1000e-1").to_no_mantissa().compare_representation("11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+0001.1000e+1").to_no_mantissa().compare_representation("11e0"),
            True,
        )
        self.assertEqual(
            Binary("+0001.1000e+10").to_no_mantissa().compare_representation("11e9"),
            True,
        )
        with self.assertRaises(TypeError):
            Binary(1).to_no_mantissa(1)  # should fail
        with self.assertRaises(OverflowError):
            Binary("Nan").to_no_mantissa()  # should fail

    def test_to_exponent(self):
        """Test function/method."""
        self.assertIsInstance(Binary("1").to_exponent(), Binary)
        self.assertIsInstance(Binary("1").to_exponent(-2), Binary)
        self.assertEqual(str(Binary("1.1").to_exponent(3)), "0b0.0011e3")
        self.assertEqual(str(Binary("1.1").to_exponent(-3)), "0b1100e-3")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(-6)), "-0b100e-6")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(-5)), "-0b10e-5")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(-4)), "-0b1e-4")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(-3)), "-0b0.1e-3")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(-2)), "-0b0.01e-2")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(-1)), "-0b0.001e-1")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(0)), "-0b0.0001")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(1)), "-0b0.00001e1")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(2)), "-0b0.000001e2")
        self.assertEqual(str(Binary("-0.01e-2").to_exponent(3)), "-0b0.0000001e3")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(-6)), "0b100e-6")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(-5)), "0b10e-5")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(-4)), "0b1e-4")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(-3)), "0b0.1e-3")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(-2)), "0b0.01e-2")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(-1)), "0b0.001e-1")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(0)), "0b0.0001")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(1)), "0b0.00001e1")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(2)), "0b0.000001e2")
        self.assertEqual(str(Binary("0.01e-2").to_exponent(3)), "0b0.0000001e3")
        self.assertEqual(str(Binary("+0.01e-2").to_exponent(3)), "0b0.0000001e3")
        with self.assertRaises(TypeError):
            Binary(1).to_exponent("1")  # should fail
        with self.assertRaises(OverflowError):
            Binary("Nan").to_exponent()  # should fail

    def test_to_sci_exponent(self):
        """Test function/method."""
        self.assertIsInstance(Binary("1").to_sci_exponent(), Binary)
        self.assertEqual(
            Binary("101e2").to_sci_exponent().compare_representation("1.01e4"),
            True,
        )
        self.assertEqual(str(Binary("1.1").to_sci_exponent()), "0b1.1e0")
        self.assertEqual(
            Binary("-000101e002").to_sci_exponent().compare_representation("-1.01e4"),
            True,
        )
        self.assertEqual(
            Binary("-001.100").to_sci_exponent().compare_representation("-1.1e0"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_sci_exponent().compare_representation("-1e-4"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001e-2").to_sci_exponent().compare_representation("-1e-7"),
            True,
        )
        self.assertEqual(
            Binary("+0.00001e+2").to_sci_exponent().compare_representation("1e-3"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e-2")
            .to_sci_exponent()
            .compare_representation("-1.01e-7"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e+2")
            .to_sci_exponent()
            .compare_representation("-1.01e-3"),
            True,
        )
        with self.assertRaises(TypeError):
            Binary(1).to_sci_exponent(1)  # should fail
        with self.assertRaises(OverflowError):
            Binary("Nan").to_sci_exponent()  # should fail

    def test_to_eng_exponent(self):
        """Test function/method."""
        self.assertIsInstance(Binary("1").to_eng_exponent(), Binary)
        for ii in range(-1023, 1023, 1):
            if ii < 0:
                self.assertEqual(Binary(ii).to_eng_exponent(), "-" + bin(ii)[3:])
            else:
                self.assertEqual(Binary(ii).to_eng_exponent(), bin(ii)[2:])
        self.assertEqual(
            Binary(1023).to_eng_exponent().compare_representation("1111111111"),
            True,
        )
        self.assertEqual(
            Binary(1024).to_eng_exponent().compare_representation("1e10"),
            True,
        )
        self.assertEqual(
            Binary(1025).to_eng_exponent().compare_representation("1.0000000001e10"),
            True,
        )
        self.assertEqual(
            Binary(3072).to_eng_exponent().compare_representation("11e10"),
            True,
        )
        self.assertEqual(
            Binary(1024 ** 2).to_eng_exponent().compare_representation("1e20"),
            True,
        )
        self.assertEqual(str(Binary(".11111e1").to_eng_exponent()), "0b1.1111")
        self.assertEqual(
            Binary(".01111e2").to_eng_exponent().compare_representation("1.111"),
            True,
        )
        self.assertEqual(
            Binary(".0011111e3").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("0.1").to_eng_exponent().compare_representation("1000000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("0.11").to_eng_exponent().compare_representation("1100000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("0.01").to_eng_exponent().compare_representation("100000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("0.0000000001").to_eng_exponent().compare_representation("1e-10"),
            True,
        )
        self.assertEqual(
            Binary("0.000000001").to_eng_exponent().compare_representation("10e-10"),
            True,
        )
        self.assertEqual(
            Binary("0.00000000111")
            .to_eng_exponent()
            .compare_representation("11.1e-10"),
            True,
        )
        self.assertEqual(
            Binary(".11111e1").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".011111e2").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".0011111e3").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_eng_exponent().compare_representation("-1000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.0001e-4")
            .to_eng_exponent()
            .compare_representation(
                "-100e-10",
            ),
            True,
        )
        self.assertEqual(
            Binary("-0.0001111e-4")
            .to_eng_exponent()
            .compare_representation(
                "-111.1e-10",
            ),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_eng_exponent().compare_representation("-1000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.0001e-4").to_eng_exponent().compare_representation("-100e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.0001111e-4")
            .to_eng_exponent()
            .compare_representation("-111.1e-10"),
            True,
        )
        self.assertEqual(
            Binary("101e2").to_eng_exponent().compare_representation("10100"),
            True,
        )
        self.assertEqual(
            Binary("1.1").to_eng_exponent().compare_representation("1.1"), True
        )
        self.assertEqual(
            Binary("100_000_000").to_eng_exponent().compare_representation("100000000"),
            True,
        )
        self.assertEqual(
            Binary("1_000_000_000")
            .to_eng_exponent()
            .compare_representation("1000000000"),
            True,
        )
        self.assertEqual(
            Binary("10_000_000_000").to_eng_exponent().compare_representation("1e10"),
            True,
        )
        self.assertEqual(
            Binary("-100_000_000")
            .to_eng_exponent()
            .compare_representation("-100000000"),
            True,
        )
        self.assertEqual(
            Binary("-1_000_000_000")
            .to_eng_exponent()
            .compare_representation("-1000000000"),
            True,
        )
        self.assertEqual(
            Binary("-10_000_000_000").to_eng_exponent().compare_representation("-1e10"),
            True,
        )
        self.assertEqual(
            Binary("-001.100").to_eng_exponent().compare_representation("-1.1"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_eng_exponent().compare_representation("-1000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001e-2").to_eng_exponent().compare_representation("-1000e-10"),
            True,
        )
        self.assertEqual(
            Binary("+0.00001e+2")
            .to_eng_exponent()
            .compare_representation("10000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e-2")
            .to_eng_exponent()
            .compare_representation("-1010e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e+2")
            .to_eng_exponent()
            .compare_representation("-10100000e-10"),
            True,
        )
        self.assertEqual(
            Binary("1.1").to_eng_exponent().compare_representation("1.1"),
            True,
        )
        self.assertEqual(
            Binary("1.1111").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("100.1111").to_eng_exponent().compare_representation("100.1111"),
            True,
        )
        self.assertEqual(
            Binary("1000.1111").to_eng_exponent().compare_representation("1000.1111"),
            True,
        )
        self.assertEqual(
            Binary("1").to_eng_exponent().compare_representation("1"),
            True,
        )
        self.assertEqual(
            Binary("10").to_eng_exponent().compare_representation("10"),
            True,
        )
        self.assertEqual(
            Binary("100").to_eng_exponent().compare_representation("100"),
            True,
        )
        self.assertEqual(
            Binary("1000").to_eng_exponent().compare_representation("1000"),
            True,
        )
        self.assertEqual(
            Binary("10000").to_eng_exponent().compare_representation("10000"),
            True,
        )
        self.assertEqual(
            Binary("100000").to_eng_exponent().compare_representation("100000"),
            True,
        )
        self.assertEqual(
            Binary("1000000").to_eng_exponent().compare_representation("1000000"),
            True,
        )
        self.assertEqual(
            Binary("1_000_000_000")
            .to_eng_exponent()
            .compare_representation("1000000000"),
            True,
        )
        self.assertEqual(
            Binary("10_000_000_000").to_eng_exponent().compare_representation("1e10"),
            True,
        )
        self.assertEqual(
            Binary("10_000_000_001.101")
            .to_eng_exponent()
            .compare_representation("1.0000000001101e10"),
            True,
        )
        self.assertEqual(
            Binary("1010_000_000_001.101")
            .to_eng_exponent()
            .compare_representation("101.0000000001101e10"),
            True,
        )
        self.assertEqual(
            str(Binary("1010_000_000_001.10101010101010101").to_eng_exponent()),
            "0b101.000000000110101010101010101e10",
        )
        self.assertEqual(
            str(
                Binary(
                    "1010_000_000_001.1010101010101010110101010101010101"
                ).to_eng_exponent()
            ),
            "0b101.00000000011010101010101010110101010101010101e10",
        )
        self.assertEqual(
            str(
                Binary(
                    "1_010_001_010_000_000_001.1010101010101010110101010101010101"
                ).to_eng_exponent()
            ),
            "0b101000101.00000000011010101010101010110101010101010101e10",
        )
        self.assertEqual(
            str(
                Binary(
                    "11_010_001_010_000_000_001.1010101010101010110101010101010101"
                ).to_eng_exponent()
            ),
            "0b1101000101.00000000011010101010101010110101010101010101e10",
        )
        self.assertEqual(
            str(
                Binary(
                    "111_010_001_010_000_000_001.1010101010101010110101010101010101"
                ).to_eng_exponent()
            ),
            "0b1.110100010100000000011010101010101010110101010101010101e20",
        )
        self.assertEqual(
            Binary("100000.1111")
            .to_eng_exponent()
            .compare_representation("100000.1111"),
            True,
        )
        self.assertEqual(
            Binary("1000000.1111")
            .to_eng_exponent()
            .compare_representation("1000000.1111"),
            True,
        )
        self.assertEqual(
            Binary("1.1111e0").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("11.111e-1").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("111.11e-2").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("1111.1e-3").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("11111.e-4").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".11111e1").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".011111e2").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".0011111e3").to_eng_exponent().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_eng_exponent().compare_representation("-1000000e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.0001e-4").to_eng_exponent().compare_representation("-100e-10"),
            True,
        )
        self.assertEqual(
            Binary("-0.0001111e-4")
            .to_eng_exponent()
            .compare_representation("-111.1e-10"),
            True,
        )
        with self.assertRaises(TypeError):
            Binary(1).to_eng_exponent(1)  # should fail
        with self.assertRaises(OverflowError):
            Binary("Nan").to_eng_exponent()  # should fail

    def test_get_components(self):
        """Test function/method."""
        self.assertEqual(Binary.get_components("-0.01e-2"), (1, "0", "01", -2))
        self.assertEqual(Binary.get_components("+0.01e-2"), (0, "0", "01", -2))
        self.assertEqual(Binary.get_components(".01e-2"), (0, "0", "01", -2))
        self.assertEqual(Binary.get_components("1.00e-2"), (0, "1", "", -2))
        self.assertEqual(Binary.get_components("-0.01e+2"), (1, "0", "01", 2))
        self.assertEqual(Binary.get_components("+0.01e2"), (0, "0", "01", 2))
        self.assertEqual(Binary.get_components("-101010.e+2"), (1, "101010", "", 2))
        self.assertEqual(Binary.get_components("+101010e2"), (0, "101010", "", 2))
        with self.assertRaises(ValueError):
            Binary.get_components("inf")  # should fail
        with self.assertRaises(TypeError):
            Binary.get_components(0.0)  # should fail
        with self.assertRaises(TypeError):
            Binary.get_components(Binary(1))  # should fail

    def test_components(self):
        """Test function/method."""
        self.assertEqual(Binary("-0.01e-2").components(), (1, "0", "01", -2))
        self.assertEqual(Binary("+0.01e-2").components(), (0, "0", "01", -2))
        self.assertEqual(Binary(".01e-2").components(), (0, "0", "01", -2))
        self.assertEqual(Binary("1.00e-2").components(), (0, "1", "", -2))
        self.assertEqual(Binary("-0.01e+2").components(), (1, "0", "01", 2))
        self.assertEqual(Binary("+0.01e2").components(), (0, "0", "01", 2))
        self.assertEqual(Binary("-101010.e+2").components(), (1, "101010", "", 2))
        self.assertEqual(Binary("+101010e2").components(), (0, "101010", "", 2))
        with self.assertRaises(ValueError):
            Binary("inf").components()  # should fail
        with self.assertRaises(TypeError):
            Binary.components()  # should fail
        with self.assertRaises(TypeError):
            Binary.components("1")  # should fail

    def test_isinfinity(self):
        """Test function/method."""
        self.assertEqual(Binary(-3.5).isinfinity(), False)
        self.assertEqual(Binary(float("nan")).isinfinity(), False)
        self.assertEqual(Binary("Nan").isinfinity(), False)
        self.assertEqual(Binary(float("-inf")).isinfinity(), True)
        self.assertEqual(Binary("-inf").isinfinity(), True)
        self.assertEqual(Binary(float("inf")).isinfinity(), True)
        self.assertEqual(Binary("inf").isinfinity(), True)
        self.assertEqual(Binary("10.1").isinfinity(), False)

    def test_isnegativeinfinity(self):
        """Test function/method."""
        self.assertEqual(Binary(-3.5).isnegativeinfinity(), False)
        self.assertEqual(Binary(float("nan")).isnegativeinfinity(), False)
        self.assertEqual(Binary("Nan").isnegativeinfinity(), False)
        self.assertEqual(Binary(float("-inf")).isnegativeinfinity(), True)
        self.assertEqual(Binary("-inf").isnegativeinfinity(), True)
        self.assertEqual(Binary(float("inf")).isnegativeinfinity(), False)
        self.assertEqual(Binary("inf").isnegativeinfinity(), False)
        self.assertEqual(Binary("10.1").isnegativeinfinity(), False)

    def test_ispositiveinfinity(self):
        """Test function/method."""
        self.assertEqual(Binary(-3.5).ispositiveinfinity(), False)
        self.assertEqual(Binary(float("nan")).ispositiveinfinity(), False)
        self.assertEqual(Binary("Nan").ispositiveinfinity(), False)
        self.assertEqual(Binary(float("-inf")).ispositiveinfinity(), False)
        self.assertEqual(Binary("-inf").ispositiveinfinity(), False)
        self.assertEqual(Binary(float("inf")).ispositiveinfinity(), True)
        self.assertEqual(Binary("inf").ispositiveinfinity(), True)
        self.assertEqual(Binary("10.1").ispositiveinfinity(), False)

    def test_isnan(self):
        """Test function/method."""
        self.assertEqual(Binary(-3.5).isnan(), False)
        self.assertEqual(Binary(float("nan")).isnan(), True)
        self.assertEqual(Binary("Nan").isnan(), True)
        self.assertEqual(Binary("10.1").isnan(), False)

    def test_isint(self):
        """Test function/method."""
        self.assertEqual(Binary(-3).isint(), True)
        self.assertEqual(Binary(-3.0).isint(), True)
        self.assertEqual(Binary(+3).isint(), True)
        self.assertEqual(Binary(+3.0).isint(), True)
        self.assertEqual(Binary("-11").isint(), True)
        self.assertEqual(Binary("11").isint(), True)
        self.assertEqual(Binary("-11.0").isint(), True)
        self.assertEqual(Binary("11.00").isint(), True)
        self.assertEqual(Binary("-0b11").isint(), True)
        self.assertEqual(Binary("0b11").isint(), True)
        self.assertEqual(Binary("-11.1").isint(), False)
        self.assertEqual(Binary("11.1").isint(), False)
        self.assertEqual(Binary("-11.1e-2").isint(), False)
        self.assertEqual(Binary("11.1e2").isint(), True)
        self.assertEqual(Binary(-3.5).isint(), False)
        self.assertEqual(Binary(float("inf")).isint(), False)
        self.assertEqual(Binary("-inf").isint(), False)
        self.assertEqual(Binary(float("nan")).isint(), False)
        self.assertEqual(Binary("Nan").isint(), False)
        self.assertEqual(Binary("10.1").isint(), False)

    def test_fraction(self):
        """Test function/method."""
        self.assertEqual(isinstance(Binary(0).fraction(), Fraction), True)
        self.assertEqual(isinstance(Binary("0").fraction(), Fraction), True)

    def test_string(self):
        """Test function/method."""
        self.assertEqual(isinstance(Binary(0).string(), str), True)
        self.assertEqual(isinstance(Binary("0").string(), str), True)

    def test_fraction_to_string(self):
        """Test function/method."""
        self.assertEqual(Binary.fraction_to_string(0), "0")
        self.assertEqual(Binary.fraction_to_string(1), "1")
        self.assertEqual(Binary.fraction_to_string(2), "10")
        self.assertEqual(Binary.fraction_to_string(13), "1101")
        self.assertEqual(Binary.fraction_to_string(-0), "0")
        self.assertEqual(Binary.fraction_to_string(-1), "-1")
        self.assertEqual(Binary.fraction_to_string(-2), "-10")
        self.assertEqual(Binary.fraction_to_string(-13), "-1101")
        self.assertEqual(Binary.fraction_to_string(0.0), "0")
        self.assertEqual(Binary.fraction_to_string(1.0), "1")
        self.assertEqual(Binary.fraction_to_string(2.0), "10")
        self.assertEqual(Binary.fraction_to_string(13.0), "1101")
        self.assertEqual(Binary.fraction_to_string(-0.0), "0")
        self.assertEqual(Binary.fraction_to_string(-1.0), "-1")
        self.assertEqual(Binary.fraction_to_string(-2.0), "-10")
        self.assertEqual(Binary.fraction_to_string(-13.0), "-1101")
        self.assertEqual(Binary.fraction_to_string(Fraction(0.0)), "0")
        self.assertEqual(Binary.fraction_to_string(Fraction(1.0)), "1")
        self.assertEqual(Binary.fraction_to_string(Fraction(2.0)), "10")
        self.assertEqual(Binary.fraction_to_string(Fraction(13.0)), "1101")
        self.assertEqual(Binary.fraction_to_string(Fraction(-0.0)), "0")
        self.assertEqual(Binary.fraction_to_string(Fraction(-1.0)), "-1")
        self.assertEqual(Binary.fraction_to_string(Fraction(-2.0)), "-10")
        self.assertEqual(Binary.fraction_to_string(Fraction(-13.0)), "-1101")
        self.assertEqual(
            Binary.fraction_to_string(Fraction(2 ** 100 + 2 ** 0)),
            "1" + "0" * 99 + "1",
        )
        self.assertEqual(
            Binary.fraction_to_string(Fraction(-(2 ** 100) - 2 ** 0)),
            "-1" + "0" * 99 + "1",
        )
        self.assertEqual(
            Binary.fraction_to_string(Fraction(2 ** 100 + 2 ** 0, 2 ** 101)),
            "0.1" + "0" * 99 + "1",
        )
        self.assertEqual(
            Binary.fraction_to_string(Fraction(2 ** 100 + 2 ** 0, -1 * 2 ** 101)),
            "-0.1" + "0" * 99 + "1",
        )
        self.assertEqual(
            Binary.fraction_to_string(
                Fraction(2 ** 1000 + 2 ** 0, -1 * 2 ** 1001), ndigits=10000
            ),
            "-0.1" + "0" * 999 + "1",
        )
        self.assertEqual(
            Binary.fraction_to_string(
                Fraction(2 ** 1000 + 2 ** 0, -1 * 2 ** 1001), ndigits=10
            ),
            "-0.1",
        )
        self.assertEqual(
            Binary.fraction_to_string(
                Fraction(2 ** 1000 + 2 ** 0, -1 * 2 ** 1001), ndigits=10, simplify=False
            ),
            "-0.1" + "0" * 9,
        )
        with self.assertRaises(TypeError):
            Binary.fraction_to_string(Binary(1))  # should fail

    def test_isclose(self):
        """Test function/method."""
        self.assertEqual(Binary("inf").isclose("infinity"), False)
        self.assertEqual(Binary("-inf").isclose("-infinity"), False)
        self.assertEqual(Binary("nan").isclose(1), False)
        self.assertEqual(Binary("nan").isclose("NaN"), False)
        self.assertEqual(Binary("nan").isclose("nan"), False)
        self.assertEqual(Binary("nan").isclose("inf"), False)
        self.assertEqual(Binary("-inf").isclose("infinity"), False)
        self.assertEqual(Binary("-0.01e-2").isclose("-1e-4"), True)
        self.assertEqual(Binary("-0.01e-2").isclose(Fraction(-1, 16)), True)
        self.assertEqual(Binary("+1.1").isclose(Fraction(3, 2)), True)
        self.assertEqual(Binary("+1.1").isclose(Fraction(3, 2)), True)
        self.assertEqual(Binary("+1.1").isclose(3 / 2), True)
        self.assertEqual(Binary("+1.1").isclose(1.5), True)
        self.assertEqual(Binary("+1.0").isclose(1), True)
        self.assertEqual(Binary("+1.0e+1").isclose(2), True)
        self.assertEqual(Binary("-100.0e-1").isclose(-2), True)
        self.assertEqual(Binary("+1.1").isclose(Fraction(4, 2)), False)
        self.assertEqual(Binary("+1.1").isclose(Fraction(4, 2)), False)
        self.assertEqual(Binary("+1.1").isclose(4 / 2), False)
        self.assertEqual(Binary("+1.1").isclose(2.5), False)
        self.assertEqual(Binary("+1.0").isclose(2), False)
        self.assertEqual(Binary("+1.0e+1").isclose(3), False)
        self.assertEqual(Binary("-100.0e-1").isclose(4), False)
        self.assertEqual(
            Binary("0.000000000000000101").isclose(Fraction(5, 2 ** 18)), True
        )
        self.assertEqual(
            Binary("-100.00000001e-100").isclose("-100.0000000101e-100"), False
        )
        self.assertEqual(
            Binary("-100.00000001e-100").isclose("-100.0000000101e-100", 0.1), True
        )
        self.assertEqual(
            Binary("-100.00000001e-100").isclose(
                "-100.000000010000000000000000000000000001e-100"
            ),
            True,
        )
        with self.assertRaises(ValueError):
            Binary("-0.01e-2").isclose("102")  # should fail
        with self.assertRaises(TypeError):
            Binary("-0.01e-2").isclose(complex(1, 1))  # should fail

    def test___eq__(self):
        """Test function/method."""
        # indirect test of test__cmp()
        self.assertEqual(Binary("inf") == Binary("infinity"), True)
        self.assertEqual(Binary("-inf") == Binary("-infinity"), True)
        self.assertEqual(Binary("nan") == 1, False)
        self.assertEqual(Binary("nan") == "NaN", False)
        self.assertEqual(Binary("nan") == Binary("nan"), False)
        self.assertEqual(Binary("nan") == Binary("inf"), False)
        self.assertEqual(Binary("-inf") == Binary("infinity"), False)
        self.assertEqual(Binary("-0.01e-2") == Binary("-1e-4"), True)
        self.assertEqual(Binary("-0.01e-2") == Binary(Fraction(-1, 16)), True)
        self.assertEqual(Binary("+1.1") == Binary(Fraction(3, 2)), True)
        self.assertEqual(Binary("+1.1") == Fraction(3, 2), True)
        self.assertEqual(Binary("+1.1") == (3 / 2), True)
        self.assertEqual(Binary("+1.1") == 1.5, True)
        self.assertEqual(Binary("+1.0") == 1, True)
        self.assertEqual(Binary("+1.0e+1") == 2, True)
        self.assertEqual(Binary("-100.0e-1") == -2, True)
        self.assertEqual(Binary("+1.1") == Binary(Fraction(4, 2)), False)
        self.assertEqual(Binary("+1.1") == Fraction(4, 2), False)
        self.assertEqual(Binary("+1.1") == (4 / 2), False)
        self.assertEqual(Binary("+1.1") == 2.5, False)
        self.assertEqual(Binary("+1.0") == 2, False)
        self.assertEqual(Binary("+1.0e+1") == 3, False)
        self.assertEqual(Binary("-100.0e-1") == 4, False)
        self.assertEqual(Binary("0.000000000000000101") == Fraction(5, 2 ** 18), True)
        with self.assertRaises(ArithmeticError):
            Binary._cmp(Binary("Nan"), "Nan")  # should fail
        with self.assertRaises(ValueError):
            Binary("-0.01e-2") == "102"  # should fail
        with self.assertRaises(TypeError):
            Binary("-0.01e-2") == complex(1, 1)  # should fail

    def test___lt__(self):
        """Test function/method."""
        # indirect test of test__cmp()
        self.assertEqual(Binary("inf") < Binary("infinity"), False)
        self.assertEqual(Binary("-inf") < Binary("-infinity"), False)
        self.assertEqual(Binary("nan") < 1, False)
        self.assertEqual(Binary("nan") < "NaN", False)
        self.assertEqual(Binary("nan") < Binary("nan"), False)
        self.assertEqual(Binary("nan") < Binary("inf"), False)
        self.assertEqual(Binary("-inf") < Binary("inf"), True)
        self.assertEqual(Binary("-0.0101e-2") < Binary("-1.0e-4"), True)
        self.assertEqual(Binary("-0.01e-2") < Binary(Fraction(-0, 16)), True)
        self.assertEqual(Binary("+1.1") < Binary(Fraction(4, 2)), True)
        self.assertEqual(Binary("+1.1") < Fraction(4, 2), True)
        self.assertEqual(Binary("+1.1") < (4 / 2), True)
        self.assertEqual(Binary("+1.1") < 1.6, True)
        self.assertEqual(Binary("+1.0") < 1.01, True)
        self.assertEqual(Binary("+1.0e+1") < 2.2, True)
        self.assertEqual(Binary("-100.0e-1") < -1.2, True)
        self.assertEqual(Binary("+1.1") < Binary(Fraction(1, 2)), False)
        self.assertEqual(Binary("+1.1") < Fraction(1, 2), False)
        self.assertEqual(Binary("+1.1") < (1 / 2), False)
        self.assertEqual(Binary("+1.1") < 0.5, False)
        self.assertEqual(Binary("+1.0") < 0.5, False)
        self.assertEqual(Binary("+1.0e+1") < 1, False)
        self.assertEqual(Binary("-100.0e-1") < -13, False)
        self.assertEqual(Binary("0.000000000000000101") < Fraction(6, 2 ** 18), True)
        with self.assertRaises(ValueError):
            Binary("-0.01e-2") < "102"  # should fail
        with self.assertRaises(TypeError):
            Binary("-0.01e-2") < complex(1, 1)  # should fail

    def test___gt__(self):
        """Test function/method."""
        # indirect test of test__cmp()
        self.assertEqual(Binary("inf") > Binary("infinity"), False)
        self.assertEqual(Binary("-inf") > Binary("-infinity"), False)
        self.assertEqual(Binary("nan") > 1, False)
        self.assertEqual(Binary("nan") > "NaN", False)
        self.assertEqual(Binary("nan") > Binary("nan"), False)
        self.assertEqual(Binary("nan") > Binary("inf"), False)
        self.assertEqual(Binary("-inf") > Binary("inf"), False)
        self.assertEqual(Binary("-0.0101e-2") > Binary("-1.0e-4"), False)
        self.assertEqual(Binary("-0.01e-2") > Binary(Fraction(-0, 16)), False)
        self.assertEqual(Binary("+1.1") > Binary(Fraction(4, 2)), False)
        self.assertEqual(Binary("+1.1") > Fraction(4, 2), False)
        self.assertEqual(Binary("+1.1") > (4 / 2), False)
        self.assertEqual(Binary("+1.1") > 1.6, False)
        self.assertEqual(Binary("+1.0") > 1.01, False)
        self.assertEqual(Binary("+1.0e+1") > 2.2, False)
        self.assertEqual(Binary("-100.0e-1") > -1.2, False)
        self.assertEqual(Binary("+1.1") > Binary(Fraction(1, 2)), True)
        self.assertEqual(Binary("+1.1") > Fraction(1, 2), True)
        self.assertEqual(Binary("+1.1") > (1 / 2), True)
        self.assertEqual(Binary("+1.1") > 0.5, True)
        self.assertEqual(Binary("+1.0") > 0.5, True)
        self.assertEqual(Binary("+1.0e+1") > 1, True)
        self.assertEqual(Binary("-100.0e-1") > -13, True)
        self.assertEqual(Binary("0.000000000000000101") > Fraction(6, 2 ** 18), False)
        with self.assertRaises(ValueError):
            Binary("-0.01e-2") > "102"  # should fail
        with self.assertRaises(TypeError):
            Binary("-0.01e-2") > complex(1, 1)  # should fail

    def test___le__(self):
        """Test function/method."""
        # indirect test of test__cmp()
        self.assertEqual(Binary("inf") <= Binary("infinity"), True)
        self.assertEqual(Binary("-inf") <= Binary("-infinity"), True)
        self.assertEqual(Binary("nan") <= 1, False)
        self.assertEqual(Binary("nan") <= "NaN", False)
        self.assertEqual(Binary("nan") <= Binary("nan"), False)
        self.assertEqual(Binary("nan") <= Binary("inf"), False)
        self.assertEqual(Binary("-inf") <= Binary("inf"), True)
        self.assertEqual(Binary("-0.0101e-2") <= Binary("-1.0e-4"), True)
        self.assertEqual(Binary("-0.01e-2") <= Binary(Fraction(-0, 16)), True)
        self.assertEqual(Binary("+1.1") <= Binary(Fraction(4, 2)), True)
        self.assertEqual(Binary("+1.1") <= Fraction(4, 2), True)
        self.assertEqual(Binary("+1.1") <= (4 / 2), True)
        self.assertEqual(Binary("+1.1") <= 1.6, True)
        self.assertEqual(Binary("+1.0") <= 1.01, True)
        self.assertEqual(Binary("+1.0e+1") <= 2.2, True)
        self.assertEqual(Binary("-100.0e-1") <= -1.2, True)
        self.assertEqual(Binary("+1.1") <= Binary(Fraction(1, 2)), False)
        self.assertEqual(Binary("+1.1") <= Fraction(1, 2), False)
        self.assertEqual(Binary("+1.1") <= (1 / 2), False)
        self.assertEqual(Binary("+1.1") <= 0.5, False)
        self.assertEqual(Binary("+1.0") <= 0.5, False)
        self.assertEqual(Binary("+1.0e+1") <= 1, False)
        self.assertEqual(Binary("-100.0e-1") <= -13, False)
        self.assertEqual(Binary("0.000000000000000101") <= Fraction(6, 2 ** 18), True)
        self.assertEqual(Binary("1") <= Binary("1"), True)
        self.assertEqual(Binary(1) <= Binary(1), True)
        self.assertEqual(Binary(1 / 2) <= Binary(1 / 2), True)
        with self.assertRaises(ValueError):
            Binary("-0.01e-2") <= "102"  # should fail
        with self.assertRaises(TypeError):
            Binary("-0.01e-2") <= complex(1, 1)  # should fail

    def test___ge__(self):
        """Test function/method."""
        # indirect test of test__cmp()
        self.assertEqual(Binary("inf") >= Binary("infinity"), True)
        self.assertEqual(Binary("-inf") >= Binary("-infinity"), True)
        self.assertEqual(Binary("nan") >= 1, False)
        self.assertEqual(Binary("nan") >= "NaN", False)
        self.assertEqual(Binary("nan") >= Binary("nan"), False)
        self.assertEqual(Binary("nan") >= Binary("inf"), False)
        self.assertEqual(Binary("-inf") >= Binary("inf"), False)
        self.assertEqual(Binary("-0.0101e-2") >= Binary("-1.0e-4"), False)
        self.assertEqual(Binary("-0.01e-2") >= Binary(Fraction(-0, 16)), False)
        self.assertEqual(Binary("+1.1") >= Binary(Fraction(4, 2)), False)
        self.assertEqual(Binary("+1.1") >= Fraction(4, 2), False)
        self.assertEqual(Binary("+1.1") >= (4 / 2), False)
        self.assertEqual(Binary("+1.1") >= 1.6, False)
        self.assertEqual(Binary("+1.0") >= 1.01, False)
        self.assertEqual(Binary("+1.0e+1") >= 2.2, False)
        self.assertEqual(Binary("-100.0e-1") >= -1.2, False)
        self.assertEqual(Binary("+1.1") >= Binary(Fraction(1, 2)), True)
        self.assertEqual(Binary("+1.1") >= Fraction(1, 2), True)
        self.assertEqual(Binary("+1.1") >= (1 / 2), True)
        self.assertEqual(Binary("+1.1") >= 0.5, True)
        self.assertEqual(Binary("+1.0") >= 0.5, True)
        self.assertEqual(Binary("+1.0e+1") >= 1, True)
        self.assertEqual(Binary("-100.0e-1") >= -13, True)
        self.assertEqual(Binary("0.000000000000000101") >= Fraction(6, 2 ** 18), False)
        self.assertEqual(Binary(1) >= Binary(1), True)
        self.assertEqual(Binary(1 / 2) >= Binary(1 / 2), True)
        with self.assertRaises(ValueError):
            Binary("-0.01e-2") >= "102"  # should fail
        with self.assertRaises(TypeError):
            Binary("-0.01e-2") >= complex(1, 1)  # should fail

    def test___add__(self):
        """Test function/method."""
        self.assertEqual(Binary("inf") + Binary("inf"), Binary("infinity"))
        self.assertEqual(Binary("inf") + 1, Binary("infinity"))
        self.assertEqual(Binary("-inf") + Binary("-inf"), Binary("-infinity"))
        self.assertEqual(Binary("-inf") + 1, Binary("-infinity"))
        self.assertEqual((Binary("-inf") + Binary("inf")).isnan(), True)
        self.assertEqual((Binary("inf") + Binary("-inf")).isnan(), True)
        self.assertEqual((Binary("nan") + 1).isnan(), True)
        self.assertEqual((Binary("inf") + Binary("nan")).isnan(), True)
        self.assertEqual((Binary("-inf") + Binary("nan")).isnan(), True)
        self.assertEqual(Binary(1) + Binary("1"), 2)
        self.assertEqual(Binary(-1) + Binary("1"), 0)
        self.assertEqual(Binary(0.5) + Binary(0.5), 1)
        self.assertEqual(Binary("-1.1") + Binary("0.1"), -1)
        self.assertEqual(Binary(1) + 1, 2)
        self.assertEqual(Binary(-1) + 1, 0)
        self.assertEqual(Binary(0.5) + 0.5, 1)
        self.assertEqual(Binary("-1.1") + 0.5, -1)
        with self.assertRaises(ValueError):
            Binary("102") + "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) + complex(1, 1)  # should fail

    def test___sub__(self):
        """Test function/method."""
        self.assertEqual((Binary("inf") - Binary("inf")).isnan(), True)
        self.assertEqual(Binary("inf") - 1, Binary("infinity"))
        self.assertEqual((Binary("-inf") - Binary("-inf")).isnan(), True)
        self.assertEqual(Binary("-inf") - 1, Binary("-infinity"))
        self.assertEqual(Binary("-inf") - Binary("inf"), Binary("-infinity"))
        self.assertEqual(Binary("inf") - Binary("-inf"), Binary("infinity"))
        self.assertEqual((Binary("nan") - 1).isnan(), True)
        self.assertEqual((Binary("inf") - Binary("nan")).isnan(), True)
        self.assertEqual((Binary("-inf") - Binary("nan")).isnan(), True)
        self.assertEqual(
            Binary(Fraction(1, 3)) - Binary(Fraction(2, 3)), Fraction(-1, 3)
        )
        self.assertEqual(Binary(1) - Binary(1), 0)
        self.assertEqual(Binary(0) - Binary(1), -1)
        self.assertEqual(Binary(0.1) - Binary(0.2), -0.1)
        self.assertEqual(Binary(1) - Binary(0.5), 0.5)
        self.assertEqual(Binary(1) - 1, 0)
        self.assertEqual(Binary(0) - 1, -1)
        self.assertEqual(Binary(0.1) - 0.2, -0.1)
        self.assertEqual(Binary(1) - 0.5, 0.5)
        with self.assertRaises(ValueError):
            Binary("102") - "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) - complex(1, 1)  # should fail

    def test___mul__(self):
        """Test function/method."""
        self.assertEqual(Binary("inf") * Binary("inf"), Binary("inf"))
        self.assertEqual(Binary("inf") * 1, Binary("infinity"))
        self.assertEqual(Binary("-inf") * Binary("-inf"), Binary("inf"))
        self.assertEqual(Binary("-inf") * 1, Binary("-infinity"))
        self.assertEqual(Binary("-inf") * Binary("inf"), Binary("-infinity"))
        self.assertEqual(Binary("inf") * Binary("-inf"), Binary("-infinity"))
        self.assertEqual((Binary("nan") * 1).isnan(), True)
        self.assertEqual((Binary("inf") * Binary("nan")).isnan(), True)
        self.assertEqual((Binary("-inf") * Binary("nan")).isnan(), True)
        self.assertEqual(Binary(0) * Binary(1), 0)
        self.assertEqual(Binary(1) * Binary(1), 1)
        self.assertEqual(Binary(100) * Binary(Fraction(1, 10)), 10)
        self.assertEqual(Binary(0) * 1, 0)
        self.assertEqual(Binary(1) * 1, 1)
        self.assertEqual((Binary(100) * (1 / 10)).isclose(10), True)
        self.assertEqual(Binary(1) * 1.5, 1.5)
        self.assertEqual((Binary(100) * (1.11 / 10)).isclose(11.1), True)
        with self.assertRaises(ValueError):
            Binary("102") * "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) * complex(1, 1)  # should fail

    def test___truediv__(self):
        """Test function/method."""
        self.assertEqual((Binary("inf") / Binary("inf")).isnan(), True)
        self.assertEqual(Binary("inf") / 1, Binary("infinity"))
        self.assertEqual((Binary("-inf") / Binary("-inf")).isnan(), True)
        self.assertEqual(Binary("-inf") / 1, Binary("-infinity"))
        self.assertEqual((Binary("-inf") / Binary("inf")).isnan(), True)
        self.assertEqual((Binary("inf") / Binary("-inf")).isnan(), True)
        self.assertEqual((Binary("nan") / 1).isnan(), True)
        self.assertEqual((Binary("inf") / Binary("nan")).isnan(), True)
        self.assertEqual((Binary("-inf") / Binary("nan")).isnan(), True)
        self.assertEqual(Binary(100) / Binary(Fraction(1, 10)), 1000)
        self.assertEqual(Binary(0) / Binary(10), 0)
        self.assertEqual(Binary(1) / Binary(2), 0.5)
        self.assertEqual(Binary(100) / Fraction(1, 10), 1000)
        self.assertEqual(Binary(0) / 10, 0)
        self.assertEqual(Binary(1) / 2, 0.5)
        self.assertEqual(Binary(0) / 10.5, 0)
        self.assertEqual((Binary(1) / 2.5).isclose(0.4), True)
        self.assertEqual(Binary(-1) / Fraction(5, 2), Fraction(-4, 10))
        self.assertEqual((Binary(1) / (-2.5)).isclose(-0.4), True)
        with self.assertRaises(ZeroDivisionError):
            Binary(1) / Binary(0)
        with self.assertRaises(ZeroDivisionError):
            Binary(1) / 0.0
        with self.assertRaises(ZeroDivisionError):
            Binary(1) / 0
        with self.assertRaises(ValueError):
            Binary("102") / "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) / complex(1, 1)  # should fail

    def test___floordiv__(self):
        """Test function/method."""
        self.assertEqual((Binary("inf") // Binary("inf")).isnan(), True)
        self.assertEqual((Binary("inf") // 1).isnan(), True)
        self.assertEqual((Binary("-inf") // Binary("-inf")).isnan(), True)
        self.assertEqual((Binary("-inf") // 1).isnan(), True)
        self.assertEqual((Binary("-inf") // Binary("inf")).isnan(), True)
        self.assertEqual((Binary("inf") // Binary("-inf")).isnan(), True)
        self.assertEqual((Binary("nan") // 1).isnan(), True)
        self.assertEqual((Binary("inf") // Binary("nan")).isnan(), True)
        self.assertEqual((Binary("-inf") // Binary("nan")).isnan(), True)
        self.assertEqual(Binary(1234) // Binary(Fraction(1, 10)), 12340)
        self.assertEqual(Binary(0) // Binary(10), 0)
        self.assertEqual(Binary(1) // Binary(2), 0)
        self.assertEqual(Binary(100) // Fraction(1, 10), 1000)
        self.assertEqual(Binary(0) // 10, 0)
        self.assertEqual(Binary(1) // 2, 0.0)
        self.assertEqual(Binary(0) // 10.5, 0)
        self.assertEqual((Binary(1) // 2.5).isclose(0), True)
        self.assertEqual(Binary(-1) // Fraction(5, 2), -1)
        self.assertEqual((Binary(1) // (-2.5)).isclose(-1), True)
        self.assertEqual(Binary(10) // Binary(3), 3)
        self.assertEqual(Binary(7) // Binary(2), 3)
        self.assertEqual(Binary(8) // Binary(3), 2)
        self.assertEqual(Binary(-10) // Binary(3), -4)
        self.assertEqual(Binary(-7) // Binary(2), -4)
        self.assertEqual(Binary(-8) // Binary(3), -3)
        self.assertEqual(Binary(-6) // Binary(2), -3)
        self.assertEqual(Binary(-6) // Binary("inf"), -1)
        self.assertEqual(Binary(+6) // Binary("inf"), 0)
        self.assertEqual(Binary(-6) // Binary("-inf"), 0)
        self.assertEqual(Binary(+6) // Binary("-inf"), -1)
        with self.assertRaises(ZeroDivisionError):
            Binary(1) // Binary(0)
        with self.assertRaises(ZeroDivisionError):
            Binary(1) // 0.0
        with self.assertRaises(ZeroDivisionError):
            Binary(1) // 0
        with self.assertRaises(ValueError):
            Binary("102") // "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) // complex(1, 1)  # should fail

    def test___mod__(self):
        """Test function/method."""
        self.assertEqual((Binary("inf") % Binary("inf")).isnan(), True)
        self.assertEqual((Binary("inf") % 1).isnan(), True)
        self.assertEqual((Binary("-inf") % Binary("-inf")).isnan(), True)
        self.assertEqual((Binary("-inf") % 1).isnan(), True)
        self.assertEqual((Binary("-inf") % Binary("inf")).isnan(), True)
        self.assertEqual((Binary("inf") % Binary("-inf")).isnan(), True)
        self.assertEqual((Binary("nan") % 1).isnan(), True)
        self.assertEqual((Binary("inf") % Binary("nan")).isnan(), True)
        self.assertEqual((Binary("-inf") % Binary("nan")).isnan(), True)
        self.assertEqual(Binary(1234) % Binary(Fraction(1, 10)), 0)
        self.assertEqual(Binary(0) % Binary(10), 0)
        self.assertEqual(Binary(1) % Binary(2), 1)
        self.assertEqual(Binary(100) % Fraction(1, 10), 0)
        self.assertEqual((Binary(100.23) % Fraction(1, 10)).isclose(0.03), True)
        self.assertEqual(Binary(0) % 10, 0)
        self.assertEqual(Binary(1) % 2, 1)
        self.assertEqual(Binary(0) % 10.5, 0)
        self.assertEqual((Binary(1) % 2.5).isclose(1), True)
        self.assertEqual(Binary(-1) % Fraction(5, 2), 1.5)
        self.assertEqual((Binary(1) % (-2.5)).isclose(-1.5), True)
        self.assertEqual(Binary(10) % Binary(3), 1)
        self.assertEqual(Binary(7) % Binary(2), 1)
        self.assertEqual(Binary(8) % Binary(3), 2)
        self.assertEqual(Binary(-10) % Binary(3), 2)
        self.assertEqual(Binary(-7) % Binary(2), 1)
        self.assertEqual(Binary(-8) % Binary(3), 1)
        self.assertEqual(Binary(-6) % Binary(2), 0)
        self.assertEqual(Binary(-6) % Binary("inf"), Binary("inf"))
        self.assertEqual(Binary(+6) % Binary("inf"), 6)
        self.assertEqual(Binary(-6) % Binary("-inf"), -6)
        self.assertEqual(Binary(+6) % Binary("-inf"), Binary("-inf"))
        self.assertEqual(Binary(5) % Binary(3), 2)
        self.assertEqual(Binary(5.5) % Binary(3), 2.5)
        self.assertEqual(Binary(7) % Binary(4), 3)
        self.assertEqual(Binary("111") % Binary("11"), 1)
        self.assertEqual(Binary(5.0) % Binary(1.5), 0.5)
        self.assertEqual(Binary("-101.0") % Binary("-1.1"), -0.5)
        with self.assertRaises(ZeroDivisionError):
            Binary(1) % Binary(0)
        with self.assertRaises(ZeroDivisionError):
            Binary(1) % 0.0
        with self.assertRaises(ZeroDivisionError):
            Binary(1) % 0
        with self.assertRaises(ValueError):
            Binary("102") % "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) % complex(1, 1)  # should fail

    def test___pow__(self):
        """Test function/method."""
        self.assertEqual((Binary("inf") ** Binary("inf")).ispositiveinfinity(), True)
        self.assertEqual((Binary("inf") ** 1).ispositiveinfinity(), True)
        self.assertEqual(Binary("-inf") ** Binary("-inf"), 0)
        self.assertEqual((Binary("-inf") ** 1).isnegativeinfinity(), True)
        self.assertEqual((Binary("-inf") ** Binary("inf")).ispositiveinfinity(), True)
        self.assertEqual(Binary("inf") ** Binary("-inf"), 0)
        self.assertEqual((Binary("nan") ** 1).isnan(), True)
        self.assertEqual((Binary("inf") ** Binary("nan")).isnan(), True)
        self.assertEqual((Binary("-inf") ** Binary("nan")).isnan(), True)
        self.assertEqual(Binary(1234) ** Binary(Fraction(1, 10)), 1234 ** 0.1)
        self.assertEqual(Binary(0) ** Binary(10), 0)
        self.assertEqual(Binary(1) ** Binary(2), 1)
        self.assertEqual(Binary(100) ** Fraction(1, 10), 100 ** 0.1)
        self.assertEqual(
            (Binary(100.23) ** Fraction(1, 10)).isclose(100.23 ** 0.1), True
        )
        self.assertEqual(Binary(0) ** 10, 0)
        self.assertEqual(Binary(1) ** 2, 1)
        self.assertEqual(Binary(0) ** 10.5, 0)
        self.assertEqual((Binary(1) ** 2.5).isclose(1), True)
        self.assertEqual((Binary(1) ** (-2.5)).isclose(1), True)
        self.assertEqual(Binary(10) ** Binary(3), 1000)
        self.assertEqual(Binary(7) ** Binary(2), 49)
        self.assertEqual(Binary(8) ** Binary(3), 64 * 8)
        self.assertEqual(Binary(-10) ** Binary(3), -1000)
        self.assertEqual(Binary(-7) ** Binary(2), 49)
        self.assertEqual(Binary(-8) ** Binary(3), -64 * 8)
        self.assertEqual(Binary(-6) ** Binary(2), 36)
        self.assertEqual(Binary(-6) ** Binary("inf"), Binary("inf"))
        self.assertEqual(Binary(+6) ** Binary("inf"), Binary("inf"))
        self.assertEqual(Binary(-6) ** Binary("-inf"), 0)
        self.assertEqual(Binary(+6) ** Binary("-inf"), 0)
        self.assertEqual(Binary(5) ** Binary(3), 125)
        self.assertEqual(Binary(5.5) ** Binary(3), 5.5 ** 3)
        self.assertEqual(Binary(7) ** Binary(4), 49 * 49)
        self.assertEqual(Binary("111") ** Binary("11"), 49 * 7)
        self.assertEqual(Binary(5.0) ** Binary(1.5), 5 ** 1.5)
        self.assertEqual((Binary(-3.4) ** Binary(-4)).isclose((-3.4) ** (-4)), True)
        self.assertEqual((Binary(-3.4) ** Binary(+4)).isclose((-3.4) ** (+4)), True)
        self.assertEqual((Binary(+3.4) ** Binary(-3.4)).isclose((+3.4) ** (-3.4)), True)
        self.assertEqual(Binary(1) ** Binary(0), 1)
        self.assertEqual(Binary(1) ** 0.0, 1)
        self.assertEqual(Binary(1) ** 0, 1)
        with self.assertRaises(ValueError):
            Binary("102") ** "103"  # should fail
        with self.assertRaises(ArithmeticError):
            Binary(-3.4) ** Binary(-3.4)  # should fail
        with self.assertRaises(ArithmeticError):
            Binary(-3.4) ** Binary(+3.4)  # should fail
        with self.assertRaises(TypeError):
            Binary(1) ** complex(1, 1)  # should fail

    def test___abs__(self):
        """Test function/method."""
        self.assertIsInstance(abs(Binary(5)), Binary)
        self.assertEqual(abs(Binary("inf")), Binary("inf"))
        self.assertEqual(abs(Binary("-inf")), Binary("inf"))
        self.assertEqual(abs(Binary("nan")).isnan(), True)
        self.assertEqual(abs(Binary(5)), 5)
        self.assertEqual(abs(Binary(-7)), 7)
        self.assertEqual(abs(Binary("111")), 7)
        self.assertEqual(abs(Binary(-1.5)), 1.5)
        self.assertEqual(abs(Binary("-101.1")), 5.5)
        with self.assertRaises(ValueError):
            abs(Binary("102"))  # should fail
        with self.assertRaises(TypeError):
            Binary.__abs__(1)  # should fail

    def test___ceil__(self):
        """Test function/method."""
        self.assertIsInstance(math.ceil(Binary(5)), int)
        self.assertEqual(math.ceil(Binary(5)), math.ceil(5))
        self.assertEqual(math.ceil(Binary(-7)), math.ceil(-7))
        self.assertEqual(math.ceil(Binary("111")), math.ceil(7))
        self.assertEqual(math.ceil(Binary(-1.5)), math.ceil(-1.5))
        self.assertEqual(math.ceil(Binary("-101.1")), math.ceil(-5.5))
        with self.assertRaises(ValueError):
            math.ceil(Binary("102"))  # should fail
        with self.assertRaises(TypeError):
            Binary.__ceil__(1)  # should fail
        with self.assertRaises(ValueError):
            math.ceil(Binary("Nan"))  # should fail
        with self.assertRaises(OverflowError):
            math.ceil(Binary("inf"))  # should fail
        with self.assertRaises(OverflowError):
            math.ceil(Binary("-inf"))  # should fail

    def test_ceil(self):
        """Test function/method."""
        self.assertIsInstance(Binary(5).ceil(), Binary)
        self.assertEqual(Binary(5).ceil(), Binary(math.ceil(5)))
        self.assertEqual(Binary(-7).ceil(), Binary(math.ceil(-7)))
        self.assertEqual(Binary("111").ceil(), Binary(math.ceil(7)))
        self.assertEqual(Binary(-1.5).ceil(), Binary(math.ceil(-1.5)))
        self.assertEqual(Binary("-101.1").ceil(), Binary(math.ceil(-5.5)))
        with self.assertRaises(ValueError):
            Binary("102").ceil()  # should fail
        with self.assertRaises(TypeError):
            Binary.ceil(1)  # should fail
        with self.assertRaises(ValueError):
            Binary("Nan").ceil()  # should fail
        with self.assertRaises(OverflowError):
            Binary("inf").ceil()  # should fail
        with self.assertRaises(OverflowError):
            Binary("-inf").ceil()  # should fail

    def test___floor__(self):
        """Test function/method."""
        self.assertIsInstance(math.floor(Binary(5)), int)
        self.assertEqual(math.floor(Binary(5)), math.floor(5))
        self.assertEqual(math.floor(Binary(-7)), math.floor(-7))
        self.assertEqual(math.floor(Binary("111")), math.floor(7))
        self.assertEqual(math.floor(Binary(-1.5)), math.floor(-1.5))
        self.assertEqual(math.floor(Binary("-101.1")), math.floor(-5.5))
        with self.assertRaises(ValueError):
            math.floor(Binary("102"))  # should fail
        with self.assertRaises(TypeError):
            Binary.__floor__(1)  # should fail
        with self.assertRaises(ValueError):
            math.floor(Binary("Nan"))  # should fail
        with self.assertRaises(OverflowError):
            math.floor(Binary("inf"))  # should fail
        with self.assertRaises(OverflowError):
            math.floor(Binary("-inf"))  # should fail

    def test_floor(self):
        """Test function/method."""
        self.assertIsInstance(Binary(5).floor(), Binary)
        self.assertEqual(Binary(5).floor(), Binary(math.floor(5)))
        self.assertEqual(Binary(-7).floor(), Binary(math.floor(-7)))
        self.assertEqual(Binary("111").floor(), Binary(math.floor(7)))
        self.assertEqual(Binary(-1.5).floor(), Binary(math.floor(-1.5)))
        self.assertEqual(Binary("-101.1").floor(), Binary(math.floor(-5.5)))
        with self.assertRaises(ValueError):
            Binary("102").floor()  # should fail
        with self.assertRaises(TypeError):
            Binary.floor(1)  # should fail
        with self.assertRaises(ValueError):
            Binary("Nan").floor()  # should fail
        with self.assertRaises(OverflowError):
            Binary("inf").floor()  # should fail
        with self.assertRaises(OverflowError):
            Binary("-inf").floor()  # should fail

    def test___rshift__(self):
        """Test function/method."""
        self.assertIsInstance(Binary(1) >> 1, Binary)
        self.assertEqual(Binary("inf") >> 1, Binary("inf"))
        self.assertEqual(Binary("-inf") >> 1, Binary("-inf"))
        self.assertEqual((Binary("nan") >> 1).isnan(), True)
        self.assertEqual(Binary(1) >> 1, 0.5)
        self.assertEqual(Binary(2) >> 3, 0.25)
        self.assertEqual(Binary(0.25) >> 1, Fraction(1, 8))
        self.assertEqual(Binary("1e1") >> 1, 1)
        self.assertEqual(Binary("101e2") >> 2, 5)
        self.assertEqual(Binary("101e2") >> 3, Fraction(5, 2 ** 1))
        self.assertEqual(Binary("101e2") >> 3, Binary(Fraction(5, 2 ** 1)))
        self.assertEqual(Binary("101e2") >> 4, Binary(Fraction(5, 2 ** 2)))
        self.assertEqual(Binary("101e2") >> 4, Binary("101e-2"))
        self.assertEqual(Binary("101e2") >> 20, Binary("101e-18"))
        self.assertEqual(Binary("101e2") >> 20, Binary(Fraction(5, 2 ** 18)))
        self.assertEqual(
            (Binary("101e2") >> 20).compare_representation("101e-18"), True
        )
        self.assertEqual((Binary("101e2") >> 2).compare_representation("101"), True)
        self.assertEqual((Binary("101e-2") >> 2).compare_representation("101e-4"), True)
        self.assertEqual(
            (Binary("101e2") >> 20).compare_representation("101e-18"), True
        )
        self.assertEqual((Binary("101") >> 2).compare_representation("1.01"), True)
        self.assertEqual(
            (Binary("101") >> 20).compare_representation("0." + "0" * 17 + "101"), True
        )
        self.assertEqual(
            (Binary("101.01e2") >> 0).compare_representation("101.01e2"), True
        )
        self.assertEqual(
            (Binary("101.01e2") >> 1).compare_representation("101.01e1"), True
        )
        self.assertEqual(
            (Binary("101.01e2") >> 20).compare_representation("101.01e-18"), True
        )
        self.assertEqual((Binary("101.01") >> 2).compare_representation("1.0101"), True)
        self.assertEqual((Binary("101.01") >> 1).compare_representation("10.101"), True)
        self.assertEqual(
            (Binary("101.01") >> 3).compare_representation("0.10101"), True
        )
        self.assertEqual(
            (Binary("101.01") >> 20).compare_representation("0." + "0" * 17 + "10101"),
            True,
        )
        with self.assertRaises(ValueError):
            Binary("10") >> -3  # should fail
        with self.assertRaises(TypeError):
            Binary(1) >> complex(1, 1)  # should fail

    def test___lshift__(self):
        """Test function/method."""
        self.assertIsInstance(Binary(1) << 1, Binary)
        self.assertEqual(Binary("inf") >> 1, Binary("inf"))
        self.assertEqual(Binary("-inf") >> 1, Binary("-inf"))
        self.assertEqual((Binary("nan") >> 1).isnan(), True)
        self.assertEqual(Binary(1) << 1, 2)
        self.assertEqual(Binary(2) << 3, 16)
        self.assertEqual(Binary(0.25) << 1, 0.5)
        self.assertEqual(Binary(0.125) << 3, 1)
        self.assertEqual(Binary("1e1") << 2, 8)
        self.assertEqual(Binary("101e2") << 2, 5 * 2 ** 4)
        self.assertEqual(Binary("101e2") << 20, 5 * 2 ** 22)
        self.assertEqual((Binary("101e-2") << 2).compare_representation("101"), True)
        self.assertEqual((Binary("101e2") << 2).compare_representation("101e4"), True)
        self.assertEqual((Binary("101e2") << 20).compare_representation("101e22"), True)
        self.assertEqual((Binary("101") << 2).compare_representation("10100"), True)
        self.assertEqual(
            (Binary("101") << 20).compare_representation("101" + "0" * 20), True
        )
        self.assertEqual(
            (Binary("101.01e2") << 2).compare_representation("101.01e4"), True
        )
        self.assertEqual(
            (Binary("101.01e2") << 20).compare_representation("101.01e22"), True
        )
        self.assertEqual((Binary("101.01") << 2).compare_representation("10101"), True)
        self.assertEqual((Binary("101.01") << 1).compare_representation("1010.1"), True)
        self.assertEqual((Binary("101.01") << 3).compare_representation("101010"), True)
        self.assertEqual(
            (Binary("101.01") << 20).compare_representation("10101" + "0" * 18), True
        )
        with self.assertRaises(ValueError):
            Binary("10") << -3  # should fail
        with self.assertRaises(TypeError):
            Binary(1) << complex(1, 1)  # should fail

    def test___bool__(self):
        """Test function/method."""
        self.assertIsInstance(bool(Binary(1)), bool)
        self.assertEqual(bool(Binary("inf")), True)
        self.assertEqual(bool(Binary("-inf")), True)
        self.assertEqual(bool(Binary("Nan")), True)
        self.assertEqual(bool(Binary(9)), True)
        self.assertEqual(bool(Binary(-10.5)), True)
        self.assertEqual(bool(Binary(0)), False)
        self.assertEqual(bool(Binary(0.0)), False)
        with self.assertRaises(TypeError):
            Binary.__bool__(complex(1, 1))  # should fail

    def test___not__(self):
        """Test function/method."""
        self.assertIsInstance(not Binary(1), bool)
        self.assertEqual(not Binary("inf"), False)
        self.assertEqual(not Binary("-inf"), False)
        self.assertEqual(not Binary("Nan"), False)
        self.assertEqual(not Binary(9), False)
        self.assertEqual(not Binary(-10.5), False)
        self.assertEqual(not Binary(0), True)
        self.assertEqual(not Binary(0.0), True)
        with self.assertRaises(TypeError):
            not Binary(complex(1, 1))  # should fail

    def test___and__(self):
        """Test function/method."""
        self.assertIsInstance(Binary(1) & Binary(1), Binary)
        self.assertEqual(Binary(1) & Binary(1), Binary(1))
        self.assertEqual(Binary(0) & Binary(1), Binary(0))
        for ii in range(-30, 30, 1):
            for jj in range(-30, 30, 1):
                self.assertEqual(Binary(ii) & Binary(jj), ii & jj)
        self.assertEqual(Binary("1000") & Binary("0"), Binary(0))
        self.assertEqual(Binary("1010") & Binary("10"), Binary("10"))
        self.assertEqual(Binary("1010") & Binary("11"), Binary("10"))
        self.assertEqual(Binary("1111") & Binary("10"), Binary("10"))
        self.assertEqual(Binary("1.1000") & Binary("0.0"), Binary(0))
        self.assertEqual(Binary("1.1010") & Binary("0.10"), Binary("0.1"))
        self.assertEqual(Binary("1.1010") & Binary("0.11"), Binary("0.1"))
        self.assertEqual(Binary("1.1111") & Binary("0.10"), Binary("0.1"))
        self.assertEqual(Binary("-0.1") & Binary("+1"), 1)
        self.assertEqual(Binary(-5) & Binary(-6), -6)
        self.assertEqual(Binary(-5) & Binary(-7), -7)
        self.assertEqual(Binary(-5) & Binary(-8), -8)
        self.assertEqual(Binary(-5) & Binary(-9), -13)
        self.assertEqual(Binary(-5) & Binary(-10), -14)
        self.assertEqual(Binary(5) & Binary(-10), 4)
        self.assertEqual(Binary(5) & Binary(-9), 5)
        self.assertEqual(Binary(5) & Binary(-8), 0)
        self.assertEqual(Binary(5) & Binary(-7), 1)
        self.assertEqual(Binary(5) & Binary(-6), 0)
        self.assertEqual(Binary(5) & Binary(-5), 1)
        with self.assertRaises(ValueError):
            Binary("102") & "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) & complex(1, 1)  # should fail
        with self.assertRaises(ArithmeticError):
            Binary("inf") & Binary(1)
        with self.assertRaises(ArithmeticError):
            Binary(1) & Binary("inf")
        with self.assertRaises(ArithmeticError):
            Binary("nan") & Binary(1)
        with self.assertRaises(ArithmeticError):
            Binary(1) & Binary("nan")
        with self.assertRaises(ArithmeticError):
            Binary("-inf") & Binary("-inf")

    def test___or__(self):
        """Test function/method."""
        self.assertIsInstance(Binary(1) | Binary(1), Binary)
        self.assertEqual(Binary(1) | Binary(1), Binary(1))
        self.assertEqual(Binary(0) | Binary(1), Binary(1))
        for ii in range(-30, 30, 1):
            for jj in range(-30, 30, 1):
                self.assertEqual(Binary(ii) | Binary(jj), ii | jj)
        self.assertEqual(Binary("1000") | Binary("0"), Binary("1000"))
        self.assertEqual(Binary("1010") | Binary("10"), Binary("1010"))
        self.assertEqual(Binary("1010") | Binary("11"), Binary("1011"))
        self.assertEqual(Binary("1111") | Binary("10"), Binary("1111"))
        self.assertEqual(Binary("1.1000") | Binary("0.0"), Binary("1.1000"))
        self.assertEqual(Binary("1.1010") | Binary("0.10"), Binary("1.1010"))
        self.assertEqual(Binary("1.1010") | Binary("0.11"), Binary("1.1110"))
        self.assertEqual(Binary("1.1111") | Binary("0.10"), Binary("1.1111"))
        self.assertEqual(Binary("-0.1") | Binary("+1"), -0.5)
        self.assertEqual(Binary(-5) | Binary(-6), -5 | -6)
        self.assertEqual(Binary(-5) | Binary(-7), -5 | -7)
        self.assertEqual(Binary(-5) | Binary(-8), -5 | -8)
        self.assertEqual(Binary(-5) | Binary(-9), -5 | -9)
        self.assertEqual(Binary(-5) | Binary(-10), -5 | -10)
        self.assertEqual(Binary(5) | Binary(-10), 5 | -10)
        self.assertEqual(Binary(5) | Binary(-9), 5 | -9)
        self.assertEqual(Binary(5) | Binary(-8), 5 | -8)
        self.assertEqual(Binary(5) | Binary(-7), 5 | -7)
        self.assertEqual(Binary(5) | Binary(-6), 5 | -6)
        self.assertEqual(Binary(5) | Binary(-5), 5 | -5)
        with self.assertRaises(ValueError):
            Binary("102") | "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) | complex(1, 1)  # should fail
        with self.assertRaises(ArithmeticError):
            Binary("inf") | Binary(1)
        with self.assertRaises(ArithmeticError):
            Binary(1) | Binary("inf")
        with self.assertRaises(ArithmeticError):
            Binary("nan") | Binary(1)
        with self.assertRaises(ArithmeticError):
            Binary(1) | Binary("nan")
        with self.assertRaises(ArithmeticError):
            Binary("-inf") | Binary("-inf")

    def test___xor__(self):
        """Test function/method."""
        self.assertIsInstance(Binary(1) ^ Binary(1), Binary)
        self.assertEqual(Binary(1) ^ Binary(1), Binary(0))
        self.assertEqual(Binary(0) ^ Binary(1), Binary(1))
        for ii in range(-30, 30, 1):
            for jj in range(-30, 30, 1):
                self.assertEqual(Binary(ii) ^ Binary(jj), ii ^ jj)
        self.assertEqual(Binary("1000") ^ Binary("0"), Binary("1000"))
        self.assertEqual(Binary("1010") ^ Binary("10"), Binary("1000"))
        self.assertEqual(Binary("1010") ^ Binary("11"), Binary("1001"))
        self.assertEqual(Binary("1111") ^ Binary("10"), Binary("1101"))
        self.assertEqual(Binary("1.1000") ^ Binary("0.0"), Binary("1.1000"))
        self.assertEqual(Binary("1.1010") ^ Binary("0.10"), Binary("1.0010"))
        self.assertEqual(Binary("1.1010") ^ Binary("0.11"), Binary("1.0110"))
        self.assertEqual(Binary("1.1111") ^ Binary("0.10"), Binary("1.0111"))
        self.assertEqual(Binary("-0.1") ^ Binary("+1"), -1.5)
        self.assertEqual(Binary(-5) ^ Binary(-6), -5 ^ -6)
        self.assertEqual(Binary(-5) ^ Binary(-7), -5 ^ -7)
        self.assertEqual(Binary(-5) ^ Binary(-8), -5 ^ -8)
        self.assertEqual(Binary(-5) ^ Binary(-9), -5 ^ -9)
        self.assertEqual(Binary(-5) ^ Binary(-10), -5 ^ -10)
        self.assertEqual(Binary(5) ^ Binary(-10), 5 ^ -10)
        self.assertEqual(Binary(5) ^ Binary(-9), 5 ^ -9)
        self.assertEqual(Binary(5) ^ Binary(-8), 5 ^ -8)
        self.assertEqual(Binary(5) ^ Binary(-7), 5 ^ -7)
        self.assertEqual(Binary(5) ^ Binary(-6), 5 ^ -6)
        self.assertEqual(Binary(5) ^ Binary(-5), 5 ^ -5)
        with self.assertRaises(ValueError):
            Binary("102") ^ "103"  # should fail
        with self.assertRaises(TypeError):
            Binary(1) ^ complex(1, 1)  # should fail
        with self.assertRaises(ArithmeticError):
            Binary("inf") ^ Binary(1)
        with self.assertRaises(ArithmeticError):
            Binary(1) ^ Binary("inf")
        with self.assertRaises(ArithmeticError):
            Binary("nan") ^ Binary(1)
        with self.assertRaises(ArithmeticError):
            Binary(1) ^ Binary("nan")
        with self.assertRaises(ArithmeticError):
            Binary("-inf") ^ Binary("-inf")

    def test___invert__(self):
        """Test function/method."""
        self.assertIsInstance(~Binary(1), Binary)
        self.assertEqual(~Binary(-2), 1)
        self.assertEqual(~Binary(-1), 0)
        self.assertEqual(~Binary(0), -1)
        self.assertEqual(~Binary(1), -2)
        self.assertEqual(~Binary(9), Binary(-10))
        self.assertEqual(~Binary(-10), Binary(9))
        self.assertEqual(~~Binary(-109), Binary(-109))
        self.assertEqual(~~Binary(9), Binary(9))
        with self.assertRaises(ValueError):
            ~Binary("-10.5")  # should fail
        with self.assertRaises(ValueError):
            ~Binary("+10.5")  # should fail
        with self.assertRaises(TypeError):
            ~Binary(complex(1, 1))  # should fail
        with self.assertRaises(ArithmeticError):
            ~Binary("inf")
        with self.assertRaises(ArithmeticError):
            ~Binary("-inf")
        with self.assertRaises(ArithmeticError):
            ~Binary("nan")

    def test_to_twoscomplement(self):
        """Test function/method."""
        self.assertIsInstance(Binary(1).to_twoscomplement(), str)
        self.assertEqual(Binary("10").to_twoscomplement(), Binary("10"))
        self.assertEqual(Binary("1010").to_twoscomplement(), Binary("1010"))
        self.assertEqual(Binary("-1").to_twoscomplement(length=12), "1" * 12)
        self.assertEqual(Binary("-1.0").to_twoscomplement(length=12), "1" * 12)
        self.assertEqual(Binary("-1.0010").to_twoscomplement(), "10.111")
        self.assertEqual(Binary("-0.0010").to_twoscomplement(), "1.111")
        self.assertEqual(Binary("-0.111").to_twoscomplement(), "1.001")
        self.assertEqual(Binary("-0.10").to_twoscomplement(), "1.1")
        self.assertEqual(Binary(0.25).to_twoscomplement(), "0.01")
        self.assertEqual(Binary(-0.125).to_twoscomplement(), "1.111")
        self.assertEqual(Binary(-0.25).to_twoscomplement(), "1.11")
        self.assertEqual(Binary(-0.5).to_twoscomplement(), "1.1")
        self.assertEqual(Binary(-1.0).to_twoscomplement(), "1")
        self.assertEqual(Binary(-2).to_twoscomplement(), "10")
        self.assertEqual(Binary(-3).to_twoscomplement(), "101")
        self.assertEqual(Binary(-1.5).to_twoscomplement(), "10.1")
        self.assertEqual(Binary(-2.5).to_twoscomplement(), "101.1")
        self.assertEqual(Binary(-2).to_twoscomplement(4), "1110")
        self.assertEqual(Binary(-3).to_twoscomplement(3), "101")
        self.assertEqual(Binary(-1.5).to_twoscomplement(4), "10.1")
        self.assertEqual(Binary(-2.5).to_twoscomplement(6), "1101.1")
        self.assertEqual(Binary(+2).to_twoscomplement(5), "00010")
        self.assertEqual(Binary(3).to_twoscomplement(3), "011")
        self.assertEqual(Binary(1.5).to_twoscomplement(4), "01.1")
        self.assertEqual(Binary(2.5).to_twoscomplement(6), "0010.1")
        self.assertEqual(Binary(2).to_twoscomplement(8), "00000010")
        self.assertEqual(Binary(+1975).to_twoscomplement(length=12), "011110110111")
        self.assertEqual(Binary(+1975).to_twoscomplement(length=13), "0011110110111")
        self.assertEqual(Binary(+1975).to_twoscomplement(length=16), "0000011110110111")
        self.assertEqual(Binary(-1975).to_twoscomplement(length=12), "100001001001")
        self.assertEqual(Binary(-1975).to_twoscomplement(length=16), "1111100001001001")
        with self.assertRaises(OverflowError):
            Binary(-3).to_twoscomplement(2)
        with self.assertRaises(OverflowError):
            Binary(3).to_twoscomplement(2)
        with self.assertRaises(OverflowError):
            Binary(-1.5).to_twoscomplement(3)
        with self.assertRaises(OverflowError):
            Binary(1.5).to_twoscomplement(2)
        with self.assertRaises(OverflowError):
            Binary(+3).to_twoscomplement(1)
        with self.assertRaises(ValueError):
            Binary(+3).to_twoscomplement(-2)
        with self.assertRaises(TypeError):
            Binary(+3).to_twoscomplement("1")
        with self.assertRaises(TypeError):
            Binary(+3).to_twoscomplement(1.0)
        with self.assertRaises(ArithmeticError):
            Binary("Inf").to_twoscomplement()
        with self.assertRaises(ArithmeticError):
            Binary("-inf").to_twoscomplement()
        with self.assertRaises(ArithmeticError):
            Binary("nan").to_twoscomplement()

    def test_from_twoscomplement(self):
        """Test function/method."""
        self.assertIsInstance(Binary.from_twoscomplement(TwosComplement("1")), str)
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("01")), "1")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("0")), "0")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("1")), "-1")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("11")), "-1")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("111")), "-1")
        for ii in [-12, -11.57, -8, -1, -0.87, 0, 0.76, 1.2, 2, 2.4, 8, 2322.2343]:
            self.assertEqual(
                Binary(Binary.from_twoscomplement(Binary(ii).to_twoscomplement())),
                Binary(ii),
            )
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("10.1")), "-1.1")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("11.1")), "-0.1")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("11.11")), "-0.01")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("11.111")), "-0.001")
        self.assertEqual(
            Binary.from_twoscomplement(TwosComplement("110.111")), "-1.001"
        )
        self.assertEqual(
            Binary.from_twoscomplement(TwosComplement("110.001")), "-1.111"
        )
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("110")), "-10")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("00")), "0")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("01")), "1")
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("00.11")), "0.11")
        self.assertEqual(
            Binary.from_twoscomplement(TwosComplement("00.11111111111110")),
            "0.1111111111111",
        )
        self.assertEqual(
            Binary.from_twoscomplement(TwosComplement("00.11e-5")), "0.11e-5"
        )
        self.assertEqual(
            Binary.from_twoscomplement(TwosComplement("00.11111111111110")),
            "0.1111111111111",
        )
        self.assertEqual(
            Binary.from_twoscomplement(
                TwosComplement("011100.00e+00", simplify=False), simplify=False
            ),
            "011100.00e+00",
        )
        self.assertEqual(
            Binary.from_twoscomplement(
                TwosComplement("1110.00e+00", simplify=False), simplify=False
            ),
            "-10e0",
        )
        self.assertEqual(
            Binary.from_twoscomplement(
                TwosComplement("1110.00e2", simplify=False), simplify=False
            ),
            "-10e2",
        )
        self.assertEqual(
            Binary.from_twoscomplement(
                TwosComplement("1110.01e2", simplify=False), simplify=False
            ),
            "-1.11e2",
        )
        self.assertEqual(
            Binary.from_twoscomplement(
                TwosComplement("1110.01e-2", simplify=False), simplify=False
            ),
            "-1.11e-2",
        )
        self.assertEqual(
            Binary.from_twoscomplement(
                TwosComplement("00.00", simplify=False), simplify=False
            ),
            "00.00",
        )
        with self.assertRaises(TypeError):
            Binary.from_twoscomplement("10")  # should fail
        with self.assertRaises(ValueError):
            Binary.from_twoscomplement(TwosComplement("102"))  # should fail
        with self.assertRaises(ValueError):
            Binary.from_twoscomplement(TwosComplement("0b10"))  # should fail
        with self.assertRaises(TypeError):
            Binary.from_twoscomplement(Binary(1))  # should fail
        with self.assertRaises(TypeError):
            Binary.from_twoscomplement("inf")
        with self.assertRaises(TypeError):
            Binary.from_twoscomplement("-Inf")
        with self.assertRaises(TypeError):
            Binary.from_twoscomplement("Nan")


##########################################################################
# Useful Constants (internal use only)
##########################################################################

""" Reusable defaults """
_Infinity = Binary(_INF)  # "Inf"
_NegativeInfinity = Binary(_NINF)  # "-Inf"
_NaN = Binary(_NAN)  # "NaN"
_Zero = Binary(0)
_One = Binary(1)
_NegativeOne = Binary(-1)

# End of class
