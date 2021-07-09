#!/usr/bin/python3

"""# Floating-point Binary Fractions: Do math in base 2!

<p align="center">
  <a href="https://pypi.org/project/binary-fractions/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/binary-fractions">
  </a>
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
</p>

![logo](binary-fractions.svg)

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

An implementation of a floating-point binary fractions class and module
in Python. Work with binary fractions and binary floats with ease!

This module allows one to represent integers, floats and fractions as
binary strings.
- e.g. the integer 3 will be represented as string '0b11'.
- e.g. the float -3.75 will be represented as string '-0b11.11'.
- e.g. the fraction 1/2 will be represented as string '0b0.1'
- Exponential representation is also possible:
'-0b0.01111e3', '-0b11.1e1' or '-0b1110e-2' all represent float -3.75.
- two's complement representation possible too:
'11.11' for -1.25, or '-0b1.01'.

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
     ||   |    | exponent in base 10 (ool(base 2!)
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
- constructors for various types: int, float, Fraction, Binary, str
- supports many operators: +, -, *, /, //, %, **, <<, >>, ~, &, ...
- supports many methods: not, abs, round, floor, ceil, ...
- very high precision
- many operations are lossless, i.e. with no rounding errors or loss of precision
- supports very long binary fractions
- supports exponential representations
- well documented.
    - Please read the documentation inside the source code
  ([binary.py](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/binary.py)).
    - Or look at the pydoc-generated documentation in
  [README.md](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/README.md).


## Sample usage, Example calls:

Please have a look at the short example program that uses the
`Binary` class and module. See file
[binary_sample.py](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/binary_sample.py).

```
$ python # sample usage, examples
>>> from binary import Binary
>>> Binary()
Binary(0, 0, False)
>>> Binary(1)
Binary(1, 0, False)
>>> Binary(2)
Binary(10, 0, False)
>>> Binary('11')
Binary(11, 0, False)
>>> Binary('11.11')
Binary(11.11, 0, False)
>>> Binary('11.11e-2')
Binary(1111e-4, 0, False)
>>> Binary('-11.11e-2')
Binary(-1111e-4, 1, False)
>>> Binary('NaN')
Binary(NaN, 0, True)
>>> Binary('-Infinity')
Binary(-Infinity, 1, True)
>>> Binary(-8.5)
Warning: mixing floats and Binary
Binary(-1000.1, 1, False)
>>> Binary('-0b111001.0001001e-12')
Binary(-1110010001001e-19, 1, False)
>>> Binary('-111001.0001001e-12')
Binary(-1110010001001e-19, 1, False)
>>> Binary('111001.0001001e-12')
Binary(1110010001001e-19, 0, False)
>>> Binary(3/4)
Binary(0.11, 0, False)
>>> Binary(17/19)
Binary(0.11100101000011010111100101000011, 0, False)
>>> Binary(128+32+8+2+17/19)
Binary(10101010.11100101000011010111100101000011, 0, False)
Binary(2**20+128+32+8+2+17/19)
Binary(100000000000010101010.11100101000011010111100101000011, 0, False)
>>> Binary((1, (1,0,0,1,1,0,0,0,1), -3))
Binary(-100110001e-3, 1, False)

>>> b=Binary(2**20+128+32+8+2+17/19)
>>> b.float()
1048746.894736842
>>> b.to_not_exponential()
Binary(100000000000010101010.11100101000011010111100101000011, 0, False)
>>> b.round(2)
Binary(100000000000010101011, 0, False)
>>> b.round(3)
Binary(100000000000010101010.111, 0, False)
>>> b.round(4)
Binary(100000000000010101010.111, 0, False)
>>> b.fill(10)
'100000000000010101010.11100101000011010111100101000011'
>>> b.fill(10,True)
'100000000000010101010.1110010100'
>>> b.fill(64)
'100000000000010101010.1110010100001101011110010100001100000000000000000000000000000000'
>>> b.fill(64,True)
'100000000000010101010.1110010100001101011110010100001100000000000000000000000000000000'
>>> b.to_simple_exponential() # no decimal point
Binary(10000000000001010101011100101000011010111100101000011e-32, 0, False)
>>> b.to_sci_exponential() # 1 digit before decimal point
Binary(1.0000000000001010101011100101000011010111100101000011e20, 0, False)
>>> b2=Binary(7)
>>> b2.to_sci_exponential()
Binary(1.11e2, 0, False)
>>> b2=Binary('111')
>>> b2.to_sci_exponential()
Binary(1.11e2, 0, False)
>>> b2.components()
(0, '111', '', 0)
>>> b3=b2.to_sci_exponential()
>>> b3.components()
(0, '1', '11', 2)
>>> b3.isinfinity()
False
>>> b2.compare(b3) # same value, returns equal
Binary(0, 0, False)
>>> b2 == b3  # same value, returns equal
True
0
>>> b2.compare_representation(b3) # different representation, returns unequal
False
>>> b2
Binary(111, 0, False)
>>> str(b2)
'0b111'
>>> b4=Binary(7.125)
>>> str(b4)
'0b111.001'
>>> b4.np() # no prefix, '0b' prefix removed
'111.001'
>>> # simple math
>>> Binary('111') + Binary(3)
Binary(1010, 0, False)
>>> Binary('111.1') - Binary(3)
Binary(100.1, 0, False)
>>> Binary('111.1') * Binary(2.0)
Binary(1111, 0, False)
>>> Binary('111.1') / Binary(4.0)
Binary(1.111, 0, False)
>>> Binary('111.1') // Binary(4.0)
Binary(1, 0, False)
>>> float(Binary('111.1'))
7.5
>>> int(Binary('111.1'))
7
>>> # works with large numbers
>>> Binary('11100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111.100000000000000000000000000000000000000010101010101010101010101010101010101010101010101010101') * Binary('11111111111111111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111111100000000000000000000000000000000000000111111111111.0111111111111111111111111111111111111111111111111111111111100000000000000000000000000011111111111111111111e-12')
Binary(1101111111111111111111111111111111111111111111111111111111111111100100000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000001101111111111111111111111111100111111111111111111111110010000000000001010101010101010101011001010101010011100101010101010011111111111101011001010101010101010101001110010101010101010101011000110011111111101111110010000000000000000001000000000000110101010101100101010101010101010101010101010101001.1101010001011001010101010101010101110101111111111111100101010101010101100101010101010101010100101000101010111110101011001010101, 0, False)
>>> # and so much more

```

## Requirements:
- Python 3
- requires no `pip` packages (uses built-in `math` and `fractions` modules)

## Installation:
- see [https://pypi.org/project/binary-fractions/](https://pypi.org/project/binary-fractions/)
- `pip install binary-fractions`

## Contributions:
- PRs are welcome and very much appreciated!
  Please run
  [selftest()](https://github.com/Jonny-exe/binary-fractions/blob/a44ec44cb58e97dac661bae6b6baffdf9d94425e/binary_fractions/binary.py#L1237)
  before issuing a PR to be sure all test cases pass.
- File Format: linted/beautified with black

Enjoy :heart: !

"""

from __future__ import annotations  # to allow type hinting in class methods
from fractions import Fraction
import math
import re
import sys
import unittest
from typing import Union


# TODO: go to stackoverflow.com, search for "binary math", "binary fractions"
# and where there are matches add comment/entry to reference this module
# in PyPi

_BINARY_WARNED_ABOUT_FLOAT = False
_BINARY_RELATIVE_TOLERANCE = 1e-10
_BINARY_PRECISION = 128  # number of binary digits to the right of decimal point
_PREFIX = "0b"
_EXP = "e"
_NAN = "NaN"
_INF = "Inf"
_NINF = "-Inf"
# _BINARY_VERSION will be set automatically with git hook upon commit
_BINARY_VERSION = "20210709-191327"  # format: date +%Y%m%d-%H%M%S
# _BINARY_TOTAL_TESTS will be set automatically with git hook upon commit
_BINARY_TOTAL_TESTS = 1150  # number of asserts in .py file

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
    """Floating point class for representing twos-complement."""

    def __new__(
        cls,
        value: Union[int, float, str, Fraction] = 0,
        length: int = -1,
        rel_tol: float = _BINARY_RELATIVE_TOLERANCE,
        simplify: bool = True,
        warn_on_float: bool = False,
    ) -> TwosComplement:
        """Constructor.

        Use __new__ and not __init__ because it is immutable.
        Allows string, float, integer, and Fraction as input for constructor.
        If instance is contructed from a string, attention is paid to *not*
        modify the string or to modify it as little as possible.
        For example, if given '1e1' it will remain as '1e1', it will not change it
        to '1'. Same with '1000', it will not change it to '1e4'. We try to keep then
        string representation as close to the original as possible.

        Parameters:
        value (int, float, str): value of number
        simplify (bool): if True try to simplify string representation
            if False, try to leave the string representation as much as is
        warn_on_float (bool): if True print a warning statement to stdout to
            warn about possible loss in precision in case of conversion from
            float to TwosComplement.
            If False, print no warning to stdout.

        Returns:
        TwosComplement: created immutable instance
        """
        if isinstance(value, int):
            return str.__new__(cls, TwosComplement._int2twoscomp(value, length))
        if isinstance(value, float):
            return str.__new__(
                cls, TwosComplement._float2twoscomp(value, length, rel_tol)
            )
        if isinstance(value, Fraction):
            return str.__new__(cls, TwosComplement._fraction2twoscomp(value, length))
        if isinstance(value, str):
            return str.__new__(cls, TwosComplement._str2twoscomp(value, length))
        # any other types
        raise TypeError(f"Cannot convert {value} to TwosComplement")

    def _int2twoscomp(value: int, length: int = -1) -> str:
        """Computes the 2's complement of int value.

        This is a utility function.
        Users should use the constructor instead.
        """
        # bits = number of bits required to represent this
        # negastive number in twos-complement
        if value == 0:
            bits = 1
        elif value > 0:
            # TODO switch to int implementation for more precision
            # add 1 for leading '0' in positive numbers
            bits = math.ceil(math.log(abs(value + 1), 2)) + 1
        else:  # negative
            bits = math.ceil(math.log(abs(value), 2)) + 1
        if length == -1:
            length = bits
        if length < bits:
            raise OverflowError(f"Argument {value} does not fit into {length} bits.")
        if value == 0:
            string = "0" * length
        elif value < 0:  # negative
            value = value - (1 << length)  # compute negative value
            string = bin(value & ((2 ** length) - 1)).replace(_PREFIX, "")
            string = "1" * (len(string) - length) + string
        else:  # positive
            string = "0" + bin(value).replace(_PREFIX, "")
            string = "0" * (length - len(string)) + string
        return string

    def _frac2twoscomp(
        value: float, length: int = -1, rel_tol: float = _BINARY_RELATIVE_TOLERANCE
    ) -> str:
        """Computes the 2's complement of the fractional part (mantissa) of a float.

        E.g. for -3.5 it computes the twos-complement of -0.5
        So, _frac2twoscomp(-3.5) returns '1.1'.
        _frac2twoscomp(+3.5) returns '0.1'.
        _frac2twoscomp(-3.375) returns '1.101'.
        _frac2twoscomp(+3.375) returns '1.11'.
        The returned string always has one integer digit, followed by a decimal point.
        The integer digit indicates the sign.
        The decimal part consists of at least 1 bit.
        So, the shortest values are 0.0, 0.1, 1.0, and 1.1.
        This function as rounding errors as it deals with floats.
        _frac2twoscomp(+1.0000000000000000000000000000000001) returns '0.0'.
        _frac2twoscomp(-0.9999999999999999999999999999999999) returns '1.0' because it is rounded to -1.

        This current implementation is inprecise because it uses float.
        # TODO switch to Fraction computation for more precision
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
        value: float, length: int = -1, rel_tol: float = _BINARY_RELATIVE_TOLERANCE
    ) -> str:
        """Converts float to twos-complement."""
        if math.isnan(value) or math.isinf(value):
            raise ArithmeticError(
                f"ArithmeticError: argument {value} is NaN or infinity."
            )
        # more precise to use Fraction than float
        return TwosComplement._fraction2twoscomp(Fraction(value), length)

    def _float2twoscomp_old_implementation_with_less_precision(
        value: float, length: int = -1, rel_tol: float = _BINARY_RELATIVE_TOLERANCE
    ) -> str:
        """Converts float to twos-complement."""
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
            raise OverflowError(f"Argument {value} does not fit into {length} bits.")
        if length != -1:
            sign = result[0]
            result = sign * (length - len(result)) + result
        return result

    def _fraction2twoscomp(
        value: Fraction,
        length: int = -1,
        ndigits: int = _BINARY_PRECISION,
        strict: bool = False,
    ) -> str:
        """Converts fractions to twos-complement."""
        # TODO: implement length, document ndigits and strict (see fraction_to_string)
        # TODO document
        if value.denominator == 1:
            result = TwosComplement._int2twoscomp(value.numerator)
            # print(f"_fraction2twoscomp: in={value}  out={result}")
            return result
        # TODO switch to Fraction computation for more precision
        if value.numerator >= 0:  # positive
            result = Binary.fraction_to_string(value, ndigits, strict)
            if result[0] != "0":
                result = "0" + result
        else:  # negative
            absvalue = -value
            digits = len(bin(int(absvalue))) - 1  # -2 for 0b + 1
            resultintpart = 2 ** digits - math.ceil(absvalue)
            result = bin(resultintpart).replace(_PREFIX, "")
            # print(f"_fraction2twoscomp: integerpart={result}")
            # remove duplicate 1s on left
            while len(result) > 1:
                if result[0] == "1" and result[1] == "1":
                    result = result[1:]
                else:
                    break
            fraction_number = absvalue - int(absvalue)
            if fraction_number > 0:
                result = result + "."
                rest = Fraction(1)
                ii = 1
                while ii < ndigits + 1:
                    b = Fraction(1, 2 ** ii)
                    if rest - b < fraction_number:
                        result += "0"
                    elif rest - b > fraction_number:
                        rest -= b
                        result = result + "1"
                    elif rest - b == fraction_number:
                        result = result + "1"
                        break
                    ii += 1
        # remove 0s on right
        if "." in result:
            result = result.rstrip("0")
        # print(f"_fraction2twoscomp: in={value}  out={result}")
        return result

    def _str2twoscomp(value: str, length: int = -1) -> str:
        """TODO"""
        if TwosComplement.istwoscomplement(value):
            if length < len(value) and length != -1:
                raise OverflowError(
                    f"Argument {value} does not fit into {length} bits."
                )
            if length != -1:
                sign = value[0]
                value = sign * (length - len(value)) + value
            return value
        else:
            raise ValueError(f"Argument {value} not a valid twos-complement.")

    def istwoscomplement(value: str) -> bool:
        """Determine if string is a valid twos-complement syntax.

        Parameters:
        self (str): string to check

        Returns:
        bool: is or is not valid twos-complement
        """
        try:
            TwosComplement.components(value)
            # don't catch TypeError
        except ValueError:
            return False
        return True

    def components(
        self_value: Union[str, TwosComplement], strict: bool = False
    ) -> tuple:
        """Return sign, intpart (indicates sign in first bit), fracpart, exp.

        This is both a function and a method.

        Examples for strict:
        Example: 3.25*4, input '11.01e2' returns (1, '11', '01', 2).
        Example: 0, input '0' returns (0, '0', '', 0).
        Example: -1, input '1' returns (1, '1', '', 0).
        Example: 1, input '01' returns (0, '01', '', 0).
        Example: -0.5, input 1.1 returns (1, '1', '1', 0).
        Example: neg. number, input 101.010e-4 returns (1, '101', '010', -4).
        Example: pos number, input 0101.010e-2 returns (0, '0101', '010', -4).
        Examples for not strict:
        Example: -3.25*4, input '1111101.11e2' returns (1, '101', '11', 2).
        Example: -3.25*4, input '11111111.0111e4' returns (1, '1', '0111', 4).
        Example: 0, input '0' returns (0, '0', '', 0).
        Example: -1, input '1' returns (1, '1', '', 0).
        Example: 1, input '01' returns (0, '01', '', 0).
        Example: -0.5, input 1.1 returns (1, '1', '1', 0).
        Example: neg. number, input 111101.0100e-4 returns (1, '101', '01', -4).
        Example: pos number, input 0000101.0100e-2 returns (0, '0101', '01', -4).

        Parameters:
        self_value (str): respresentation of a twos-complement string,
            string to extract components from
        strict (bool): if False simplify output by removing unnecessary digits
            strict==False: cleanup, remove unnecessary digits, do cleanup
            strict==True: produce exact twos-complement, no cleanup or simplifications

        Returns:
        tuple: tuple of sign, intpart, fracpart, exp
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
        if not strict:
            fracpart = fracpart.rstrip("0")
            if sign:  # neg
                intpart = "1" + intpart.lstrip("1")
            else:  # pos
                intpart = "0" + intpart.lstrip("0")
        return (sign, intpart, fracpart, exp)

    def simplify(self_value: Union[str, TwosComplement]) -> Union[str, TwosComplement]:
        """Simplifies twos-complement.

        Remove duplicate 1s on left.
        Remove duplicate 0s after decimal point.
        Remove unnecessary exponent.
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
            # while len(intpart) > 1:
            #     if intpart[0] == "1" and intpart[1] == "1":
            #         intpart = intpart[1:]
            #     else:
            #         break
            intpart = "1" + intpart.lstrip("1")
        elif len(intpart) and intpart[0] == "0":
            # remove duplicate 0s on left
            # while len(intpart) > 1:
            #     if intpart[0] == "0" and intpart[1] == "0":
            #         intpart = intpart[1:]
            #     else:
            #         break
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
        """Converts twos-complement to Fraction.

        This is a utility function as well as a method.

        Do NOT use it on negative binary fractions strings!
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
        """Converts twos-complement to float."""
        return float(TwosComplement.to_fraction(self_value))

    def to_no_mantissa(
        self_value: Union[str, TwosComplement], length: int = -1
    ) -> Union[str, TwosComplement]:
        """Adjust exponent such that there is no fractional part, no mantissa.

        This is a utility function as well as a method.
        """
        if not isinstance(self_value, str) and not isinstance(
            self_value, TwosComplement
        ):
            raise TypeError(
                f"Argument {self_value} must be of type str or TwosComplement."
            )
        value = str(self_value)
        length = len(value)
        sign, intpart, fracpart, exp = TwosComplement.components(value)
        fracpartlen = len(fracpart)
        exp -= fracpartlen
        intpart += fracpart
        result = intpart + _EXP + str(exp) if exp else intpart
        if isinstance(self_value, TwosComplement):
            result = TwosComplement(result)
        return result
        # TODO: implement LENGTH argument

    def to_not_exponential(
        self_value: Union[str, TwosComplement], length: int = -1, strict: bool = False
    ) -> Union[str, TwosComplement]:
        """Remove exponent part from twos-complement string.

        This is a utility function as well as a method.

        Do NOT use it on negative binary fractions strings!
        This function does not validate the input string.
        Input string is assumed to be a syntactically valid twos-complement string.
        Invalid input strings can lead to undefined results.

        See to_twoscomplement() function description for more details
        on twos-complement format.

        It removes the exponent, and returns a fully "decimal" twos-complement string.
        Example: converts '011.01e-2' to '0.1101'.
        Example: converts 0.25, '0.1e-1' to '0.01'.
        Example: converts -0.125, '1.111e0' to '1.111'.
        Example: converts -0.25, '1.11e0' to '1.11'.
        Example: converts -0.5, '1.1e0' to '1.1'.
        Example: converts -1.0, '1.e0' to '1'.
        Example: converts -2.0, '1.e1' to '10'.
        Example: converts -3.0, '1.01e2' to '101'.
        Example: converts -1.5, '1.01e1' to '10.1'.
        Example: converts -2.5, '1.011e2' to '101.1'.

        Parameters:
        value (str): binary string representation of number
        length (int): the length of the returned number.
             -1 is the minimum amount of bits required.
             0 and negatives numbers, except -1, are not allowed.
             Length includes the possible decimal point.
             Example of length 3 is: '1.1'

        Returns:
        str: binary string representation of number
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
        # print(f"component {value}.")
        sign, intpart, fracpart, exp = TwosComplement.components(value, strict)
        # print(f"component {value} {intpart} {fracpart}")
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
        if not strict:
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
        self_value: Union[str, TwosComplement], strict: bool = False
    ) -> Union[str, TwosComplement]:
        """Inverts (bitwise negates) string that is in twos-complement format.

        This is a utility function as well as a method.

        It negates (flips) every bit in the string.
        Input must be of format: twos-complement format.
        Do NOT use this function on negative binary fractions strings.

        Examples for input "value" string are:
            # leading 0: positive
            0...0
            01...1
            010...2
            011...3
            0100...4
            01.1...1.5
            010.11...2.75
            01.1e-4...1.5e-4
            010.11e-4...2.75e-4,
            # leading 1: negative
            1...-1
            11...-1, 111...-1, 111111111...-1
            10...-2, 111110...-2
            110...-2, 1110...-2,
            1101...-3, 111101...-3
            111.1...-0.5
            111.11...-0.25
            111.1e3...-0.5e3
            111.11e3...-0.25e3

            invert('01') returns '10' (like decimal: ~1==-2)
            invert('0') returns 1  (like decimal: ~0==-1)
            invert('1') returns 0  (like decimal: ~-1==0)
            invert('1..1') raises exception, 2 decimal points
            invert('34') raises exception, not binary
            invert('1ee2') raises exception, two exponential signs
            invert('1e') raises exception, missing exponent digit
            invert('10') returns '01'  (like decimal: ~-2==1)
            invert('101010') returns '010101'
            invert('0101010') returns '1010101'
            invert('0101010e-34') returns '1010101e-34'
            invert('101010e34') returns '0101011111111111111111111111111111111111'
            invert(invert('0101010e-34')) returns '0101010e-34'
            invert(invert('101010e34')) returns '1010100000000000000000000000000000000000'

            invert(invert(n)) == for all valid n

        Arguments:
        value (str): string representation of twos-complement
        strict (bool): if True try to change the string as little as
            possible in format
            if False, returned string will also be simplified
            by removing unnecessary digits.

        Returns:
        str: bitwise negated string, a twos-complement formated string
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

        # TODO: do you handle exp part?
        # TODO: do you handle negative numbers?

        # TODO : rethink EXP
        if _EXP in value:
            sign, intpart, fracpart, exp = TwosComplement.components(value, strict)
            if exp > 0:
                # strict = true to not miss any bits on the right
                value = TwosComplement.to_not_exponential(value, strict=True)
                # print(f" {self_value} and {value} ")
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
        if not strict:
            result = TwosComplement.simplify(result)
        if isinstance(self_value, TwosComplement):
            result = TwosComplement(result)
        return result


##########################################################################
# CLASS BINARY
##########################################################################


class Binary(object):
    """Floating point class for binary fractions and arithmetic."""

    def __new__(
        cls,
        value: Union[int, float, str, Fraction] = "0",
        simplify: bool = True,
        warn_on_float: bool = False,
    ) -> Binary:
        """Constructor.

        Use __new__ and not __init__ because it is immutable.
        Allows string, float, integer, and Fraction as input for constructor.
        If instance is contructed from a string, attention is paid to *not*
        modify the string or to modify it as little as possible.
        For example, if given '1e1' it will remain as '1e1', it will not change it
        to '1'. Same with '1000', it will not change it to '1e4'. We try to keep then
        string representation as close to the original as possible.

        Parameters:
        value (int, float, str): value of number
        simplify (bool): if True try to simplify string representation
            if False, try to leave the string representation as much as is
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
        self._is_special = False  # TODO
        self._warn_on_float = warn_on_float
        self._fraction = Fraction()
        # TODO: not yet implemented, indicate if operations were lossless
        self._is_lossless = False

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
                        self._value = _NAN  # "NaN"  # N
                    else:
                        self._value = _NAN  # "NaN"  # n
                else:
                    # infinity
                    self._value = sign + "Infinity"  # F
            # self._value = Binary.to_not_exponential(self._value) # not strictly needed
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
            # self._value = Binary.to_not_exponential(self._value) # not strictly needed
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
            self._fraction = Fraction(value)
            self._value = Binary.fraction_to_string(value)
            self._sign = 1 if value < 0 else 0
            return self

        # any other types
        raise TypeError(f"Cannot convert {value} to Binary")

    def to_float(value: str) -> Union[float, int]:
        """Convert from Binary string to float or integer.

        This is a utility function that converts
        a Binary string to a float or integer
        (Binary string --> float or integer).

        Parameters:
        value (str): binary string representation of number

        Returns:
        float or integer: number as float or integer
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
        value = Binary.to_not_exponential(value)
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
        float to Binary (float --> Binary).

        Parameters:
        value (float): value of number
        rel_tol (float): relative tolerance to know when to stop converting
            relates to precision

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

    def to_not_exponential(
        self_value: Union[Binary, str], add_prefix: bool = False, strict: bool = False
    ) -> str:
        """Normalize string representation. Remove exponent part.

        This is both a method as well as a utility function.
        Do NOT use it on Twos-complement strings!
        This function does not validate the input string.
        Input string is assumed to be a syntactically valid binary fraction string.
        Invalid strings can lead to undefined results.

        It removes the exponent, and returns a fully "decimal" binary string.
        Example: converts '11.01e-2' to '0.1101'

        Parameters:
        self_value (Binary, str): a Binary instance or
            a binary string representation of number
        add_prefix (bool):
            if self_value is a string:
                if True add 0b prefix to returned output,
                if False then do not add prefix to returned output
            if self_value is a Binary instance:
                always forces to True, will always show prefix 0b

        Returns:
        str: binary string representation of number
        """
        if not (isinstance(self_value, str) or isinstance(self_value, Binary)):
            raise TypeError(f"Argument {self_value} must be of type Binary or str.")
        if isinstance(self_value, Binary):
            return Binary.to_not_exponential(self_value._value, True)
        if self_value == "":
            raise ValueError(f"Argument {self_value} must be empty string.")
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
        if not strict:
            result = Binary.simplify(result, add_prefix)
        # print(f"after normalize {result}")
        return result

    def to_fraction(self_value: Union[str, Binary]) -> Fraction:
        """Convert string representation of Binary to Fraction.

        This is a utility function.

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

        Parameters:
        value (str): binary number as string

        Returns:
        Fraction: value as fraction
        """
        if _EXP in value:
            value = Binary.to_not_exponential(value)
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

        If you are curious about Two's complement:
        - https://janmr.com/blog/2010/07/bitwise-operators-and-negative-numbers/
        - https://en.wikipedia.org/wiki/Two%27s_complement

        The twos-complement format is as follows.
            there is sign bit per se
            positive numbers must have a leading 0 to be recognized as positive
            hence positive numbers by definition always start with a 0
            negative numbers always start with a 1
            negative numbers can have an arbitrary number of additional leading 1s
            positive numbers can have an arbitrary number of additional leading 0s
            0 or more decimal bits
            optional decimal point
            0 or more fractional bits
            optional exponent in decimal (e.g. e-12)

            [0,1]+[.][0,1]*e[-,+][0-9]+
            integer bits (at least 1 bit required, leading bit indicates pos or neg)
                decimal point (optional, one or none)
                    fractional bits (optional, zero or more)
                        exponent (optional, possible with sign -)

            decimal |   binary fraction | twos-complement
            ---------------------------------------------
            -6      |       -110        | 1010
            -5      |       -101        | 1011
            -4      |       -100        | 100
            -3      |       -11         | 101
            -2      |       -10         | 10
            -1      |       -1          | 1
            0       |       0           | 0
            1       |       1           | 01
            2       |       10          | 010
            3       |       11          | 011
            4       |       100         | 0100
            5       |       101         | 0101
            0.5     |       0.1         | 0.1
            0.25    |       0.01        | 0.01
            -0.5    |       -0.1        | 1.1
            -0.25   |       -0.01       | 1.11
            -0.125  |       -0.001      | 1.111
            -1.5    |       -1.1        | 10.1
            -2.5    |       -10.1       | 101.1


        This is a method returning a string.
        Examples:
            convert '-11.1e-2' to '1101.1e-2' (-3/4)
            convert '-11' to '1101'
            convert '-0.5' to '11.1'
            Converts '-1' to '11' (-1)
            Converts '-10' to '110' (-2)
            Converts '-11' to '101' (-3)
            Converts '-100' to '1100' (-4)
            Converts '-1.5' to '10.1'
            Converts '-2.5' to '101.1'
            Converts '-2.5e89' to '101.1e89'

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
        str: binary string representation in twos-complement
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

        # TODO, BUG: we changed our mind, now '0' is a valid binary fraction
        # TODO: BUG: 0 is 0 in decimal, 0 in binary fraction, 0 in twos-complement
        # TODO: don't prefix 0.xxx with another 0. 00.xxxx is not nice.

        if self._fraction >= 0:
            result = self._value
            if result[0] != "0":
                result = "0" + result
            result = (length - len(result)) * "0" + result
            if len(result) > length and length != -1:
                raise OverflowError
            return TwosComplement(result)

        if _EXP in self._value:
            return TwosComplement(
                "0" + self._value if self._value[0] != "0" else self._value
            )

        sign, intpart, fracpart, exp = self.components()
        if fracpart != "":
            intpart = bin(abs(int(intpart, 2)) + 1)[2:]
        intpart = abs(int(intpart, 2))
        intpart = bin(intpart)[2:]
        intpart = TwosComplement.invert(intpart)
        new_intpart = bin(int(intpart, 2) + 1)[2:]
        if len(intpart) > len(new_intpart):
            intpart = (len(intpart) - len(new_intpart)) * "0" + new_intpart
        else:
            intpart = new_intpart

        if fracpart != "" and int(fracpart) != 0:
            fracpart = fracpart.rstrip("0")
            fracl = len(fracpart)
            fracpart = bin(2 ** fracl - int(fracpart, 2))[2:]
            fracpart = "." + (fracl - len(fracpart)) * "0" + fracpart
        else:
            fracpart = ""
        result = intpart + fracpart
        if result[0] != "1":
            result = "1" + result
        result = (length - len(result)) * "1" + result
        if len(result) > length and length != -1:
            raise OverflowError
        return TwosComplement(result)

    def from_twoscomplement(value: TwosComplement, strict: bool = False) -> str:
        """The opposite of to_twoscomplement() function.

        This is a utility function that converts from twos-complement format
        to binary fraction format.

        See to_twoscomplement() function description for more details
        on twos-complement format.

        Converts '1101' to '-11' (-3)
        convert '1101.1e-2' to '-11.1e-2'  (-3.5/4)

        Parameters:
        value (str): string in twos-complement format
        strict (bool):
            If strict is True, leaves it as much as unchanged as possible.
            If strict is False simplifies returned binary string representation.

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

        # TODO zzz should we prefix return value with 0b ???
        sign, intpart, fracpart, exp = TwosComplement.components(value, strict=strict)
        if sign == 0:
            if strict:
                return value
            result = intpart[1:] if len(intpart) > 1 else intpart
            fracpart = fracpart.rstrip("0")
        else:
            result = "-"
            intpart = intpart.lstrip("0") if "1" in intpart else intpart
            intl = len(intpart)
            intpart = bin(2 ** intl - int(intpart, 2))[2:]
            result += intpart

            if "1" in fracpart:
                fracpart = fracpart.rstrip("0")
                fracl = len(fracpart)
                fracpart = bin(2 ** fracl - int(fracpart, 2))[2:]
                fracpart = (fracl - len(fracpart)) * "0" + fracpart
            else:
                fracpart = ""

        if fracpart.rstrip("0") != "" and not strict:
            result += "." + fracpart
        if _EXP in value:
            result += f"e{exp}"
        return result

    def __float__(self: Binary) -> [float, int]:
        """Convert from Binary to float.

        This is a method that convert Binary to float (or if possible to
        integer). (Binary --> float or integer)

        Returns:
        float: number as float or integer
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

    def __int__(self: Binary):
        """Convert from Binary to int.

        method
        Binary --> float or integer

        Returns:
        float: number as integer
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isinfinity():
            raise ValueError(
                f"Argument {self} is infinity. Infinity cannot be converted to integer."
            )
        else:
            result = int(self._fraction)
        # alternative implementation of float
        # result = Binary.to_float(self._value)
        return result  # float or integer

    def __str__(self: Binary) -> str:
        """Stringify self.

        Method that implements the string conversion.
        Return format is e.g. -0b101.101e-23.
        Note the prefix of '0b'.

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

    def compare_representation(self: Binary, other: Union[str, Binary]) -> int:
        """Compare representation of self to representation of other string.

        Does NOT compare values! '1.1' does NOT equal to '11e-1' !
        Only '11e-1' equals to '11e-1' !
        Returns integer.

        Parameters:
        other (str, Binary): object to compare to

        Returns:
        int: -1 s<o, 0 equal, 1 s>o
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        # compare representation to another Binary
        if isinstance(other, Binary):
            return str(self._value) == str(other._value)
        if isinstance(other, str):
            return str(self._value) == other
        else:
            return str(self._value) == str(other)

    def __repr__(self: Boolean) -> str:
        """Represent self."""
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return (
            f"{self.__class__.__name__}"
            + f"({self._value}, {self._sign}, {self._is_special})"
        )

    def no_prefix(self_value: Union[str, Binary]) -> str:
        """Remove prefix '0b' from string representation.

        A method as well as a utility function.
        Return format is e.g. -101.101e-23.

        Parameters:
        value (str, Binary): string from where to remove prefix

        Returns:
        str: without prefix
        """
        if not isinstance(self_value, str) and not isinstance(self_value, Binary):
            raise TypeError(f"Argument {self_value} must be of type str or Binary.")
        if isinstance(self_value, str):
            return self_value.replace(_PREFIX, "")
        else:
            return str(self_value._value)

    def np(self_value: Union[str, Binary]) -> str:  # no prefix
        """Remove prefix '0b' from string representation.

        Same as no_prefix().

        Parameters:
        value (str, Binary): string from where to remove prefix

        Returns:
        str: without prefix
        """
        return Binary.no_prefix(self_value)

    def version() -> str:
        """Give version number.

        Is a utility function.

        Returns:
        str: version number as date in format "YYMMDD-HHMMSS", e.g. "20210622-103815"
        """
        return _BINARY_VERSION

    def simplify(value: str, add_prefix: bool = False) -> str:
        """Simplify string representation.

        This is a utility function.
        Do NOT use it on Twos-complement strings!
        This function does not validate the input string.
        Input string is assumed to be a syntactically valid binary fraction string.
        Invalid strings can lead to undefined results.
        Example: converts '11.0' to '11' or '0011.0e-0' to '11'.

        Parameters:
        value (str): binary string representation of number
        add_prefix (bool): if True add 0b prefix to returned output,
            if False then do not add prefix to returned output

        Returns:
        str: simplified binary string representation of number
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
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

    def __round__(self: Binary, ndigits: int = 0):
        """Normalize and round number to n digits after decimal point.

        A method. Same as function round(). See also utility function round_to().

        Parameters:
        ndigits (int): number of digits after decimal point, precision

        Returns:
        Binary: binary string representation of number
        """
        return self.round(ndigits)

    def round(self: Binary, ndigits: int = 0):
        """Normalize and round number to n digits after decimal point.

        A method. Same as __round__() (round()). See also function round_to().

        Parameters:
        ndigits (int): number of digits after decimal point, precision

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        value = self._value
        result = Binary.round_to(value, ndigits)
        return Binary(result)

    def round_to(value: str, ndigits: int = 0) -> str:
        """Normalize and round number to n digits after decimal point.

        This is a utility function.
        Example: converts '11.01e-2' to '0.11' with ndigits==2.
        Converts '0.1' to '0' with ndigits==0.
        Converts '0.10000001' to '1' with ndigits==0.

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
        # print(f"value is {value} of type {type(value)}")
        value = Binary.to_not_exponential(value)
        value = value.replace(_PREFIX, "")
        li = value.split(".")
        intpart = li[0]
        if len(li) == 1:
            fracpart = ""
        else:
            fracpart = li[1]

        # print(f"fracpart is {fracpart}")
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
        """Normalize and fill number to n digits after decimal point.

        This is a method. See also function fill_to().

        Parameters:
        ndigits (int): number of digits after decimal point, precision
        strict (bool): cut off by rounding if input is too long,
            remove precision if True and necessary

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        value = self._value
        return Binary(Binary.fill_to(value, ndigits, strict))

    def fill_to(value: str, ndigits: int = 0, strict: bool = False) -> str:
        """Normalize and fill number to n digits after decimal point.

        This is a utility function.
        If strict==False then if value is longer, don't touch, don't shorten it.
        If strict==True then if value is longer, then shorten to strictly ndigits.

        Parameters:
        ndigits (int): number of digits after decimal point, precision
        strict (bool): cut off by rounding if input is too long,
            remove precision if True and necessary

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
        value = Binary.to_not_exponential(value)
        # print(f"norm. value is {value}")
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

    def to_simple_exponential(self: Binary) -> Binary:
        """Convert to exponential representation without fraction.

        A method that changes the string representation of a number
        so that the resulting string has no decimal point.
        Examples: '1.1' ==> '11e-1',  '-0.01e-2' ==> '-1e-4'

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

        return Binary(intpart + _EXP + str(exp), False)

    def to_sci_exponential(self: Binary) -> str:
        """Convert to exp. representation in scientific notation.

        Scientific notation is an exponent representation with a single
        binary digit before decimal point.

        Method that changes string representation of number.
        Examples are: '1.1' ==> '1.1e0',  '-0.01e-2' ==> '-1e-4', '1'
        The result has only 1 digit before decimal point.

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

        # TODO print("Parts: ", intpart, fracpart)
        if fracpart == "" or fracpart == "0":
            result = sign + intpart + _EXP + str(exp)
        else:
            result = sign + intpart + "." + fracpart + _EXP + str(exp)
        return Binary(result, False)

    def to_eng_exponential(self: Binary) -> str:
        """Convert to exp. representation in engineering notation.

        See https://www.purplemath.com/modules/exponent4.htm.
        See https://en.wikipedia.org/wiki/Engineering_notation.

        Engineering notation is an exponent representation with the exponent
        modulo 3 being 0 and 1, 2 or 3 digit before the decimal point.
        The integer part must not be 0. Integer part is from 1 to 999.

        Method that changes string representation of number.
        Examples are:
            '1.1' ==> '1.1'
            '1.1111' ==> '1.1111'
            '100.1111' ==> '100.1111'
            '1000.1111' ==> '1.0001111e3'
            '1' ==> '1'
            '10' ==> '10'
            '100' ==> '100'
            '1000' ==> '1e3'
            '10000' ==> '10e3'
            '100000' ==> '100e3'
            '1000000' ==> '1e6'
            '1.1111' ==> '1.1111'
            '10.1111' ==> '10.1111'
            '100.1111' ==> '100.1111'
            '1000.1111' ==> '1e3.1111'
            '10000.1111' ==> '10e3.1111'
            '100000.1111' ==> '100e3.1111'
            '1000000.1111' ==> '1e6.1111'
            '1.1111e0' ==> '1.1111'
            '11.111e-1' ==> '1.1111'
            '111.11e-2' ==> '1.1111'
            '1111.1e-3' ==> '1.1111'
            '11111.e-4' ==> '1.1111'
            '.11111e1' ==> '1.1111'
            '.011111e2' ==> '1.1111'
            '.0011111e3' ==> '1.1111'
            '-0.01e-2' ==> '-1e-3',
            '-0.0001e-4' == -0.00000001 ==> '-10e-9',
            '-0.0001111e-4' == -0.00000001111 ==> '-11.11e-9',

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
        # TODO needs to be implemented
        # ZZZ
        return Binary(self)  # TODO to be implemented

    def get_components(value: str) -> tuple:
        """Return sign, intpart (without sign), fracpart, exp.

        Example: -11.01e2 ==> (1, '11', '01', 2)

        Parameters:
        value (str): respresentation of a binary

        Returns:
        tuple: tuple of sign, intpart (without sign), fracpart, exp
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
        """Return sign, intpart (without sign), fracpart, exp.

        Example: -11.01e2 ==> (1, '11', '01', 2)
        intpart does not have a sign

        Parameters:
        none

        Returns:
        tuple: tuple of sign, intpart (without sign), fracpart, exp
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return Binary.get_components(self._value)

    def isinfinity(self: Binary) -> bool:
        """Determine if object is positive or negative Infinity.

        Parameters:
        none

        Returns:
        bool: is or is not any kind of infinity or negative infinity
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _INF in self._value

    def isnegativeinfinity(self: Binary) -> bool:
        """Determine if object is Negative Infinity.

        Parameters:
        none

        Returns:
        bool: is or is not negative infinity
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _NINF in self._value

    def ispositiveinfinity(self: Binary) -> bool:
        """Determine if object is Positive Infinity.

        Parameters:
        none

        Returns:
        bool: is or is not positive infinity
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _INF in self._value and not _NINF in self._value

    def isnan(self: Binary) -> bool:
        """Determine if object is not-a-number (NaN).

        Parameters:
        none

        Returns:
        bool: is or is not a NaN (division by zero)
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return _NAN in self._value  # "NaN"

    def isint(self: Binary) -> bool:
        """Determines if binary fraction is an integer.

        This is a utility function.

        Returns:
        bool: True if int, False otherwise (Fraction, float)
        """
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
        se = Binary.to_simple_exponential(self)
        sign, intpart, fracpart, exp = Binary.components(se)
        if fracpart != "":
            raise ValueError(
                f"Invalid literal: {se._value}. Internal error. "
                "Fraction part should be empty."
            )
        return exp + len(intpart) - 1

    def fraction(self: Binary) -> Fraction:
        """Extract Fractional representation from Binary instance.

        A method to get the Binary as a Fraction.

        Parameters:
        None

        Returns:
        Fraction: binary number in Fraction representation
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return self._fraction

    def value(self: Binary) -> str:
        """Extract string representation from Binary instance.

        A method to get the Binary as a Fraction.

        Parameters:
        None

        Returns:
        Fraction: binary number in string representation
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return self._value

    def fraction_to_string(
        number: Union[int, float, Fraction],
        ndigits: int = _BINARY_PRECISION,
        strict: bool = False,
    ) -> str:
        """Convert number representation (int, float, or Fraction) to string.

        This is a utility function.

        Parameters:
        number (int,float,Fraction): binary number in number representation
        strict (bool): cut off by rounding if input is too long,
            remove precision if True and necessary

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
        return "".join(result) if strict else Binary.simplify("".join(result))

    def isclose(
        self: Binary, other: Any, rel_tol: float = _BINARY_RELATIVE_TOLERANCE
    ) -> bool:
        """Compare two objects to see if they are mathematically close.

        This is a utility function. Useful for floats that have been converted
        to binary fractions. A substitute for == for binary fractions
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

          == comparisons involving a quiet NaN always return False
          != comparisons involving a quiet NaN always return True
          == or != comparisons involving a signaling NaN signal
             InvalidOperation, and return False or True as above if the
             InvalidOperation is not trapped.
          <, >, <= and >= comparisons involving a (quiet or signaling)
             NaN signal InvalidOperation, and return False if the
             InvalidOperation is not trapped.

        That Decimal behavior is designed to conform as closely as possible to
        that specified by IEEE 754.

        Here in Binary we take a similar approach and try to follow Decimal.

        Parameters:
        other (Any, str, Binary, int, float, Fraction): object to compare to

        Returns:
        int: -1 s<o, 0 equal, 1 s>o
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

        # this does string comparison
        # TODO: this code is never reached
        # TODO: cleanup, save this code as string comparisons
        if self._sign and self._value[0] != "-":
            raise ValueError(
                f"Invalid literal: {self._value}. Internal error. Wrong sign."
            )
        if other._sign and other._value[0] != "-":
            raise ValueError(
                f"Invalid literal: {other._value}. Internal error. Wrong sign."
            )

        # check for zeros;  Binary('0') == Binary('-0')
        if not self:
            if not other:
                return 0
            else:
                return -((-1) ** other._sign)
        if not other:
            return (-1) ** self._sign

        # If different signs, neg one is less
        if other._sign < self._sign:
            return -1
        if self._sign < other._sign:
            return 1

        self_se = Binary.to_simple_exponential(self)
        other_se = Binary.to_simple_exponential(other)
        self_adjusted = self_se._adjusted()
        other_adjusted = other_se._adjusted()
        if self_adjusted == other_adjusted:
            self_sign, self_intpart, _, self_exp = Binary.components(self_se)
            other_sign, other_intpart, _, other_exp = Binary.components(other_se)
            self_padded = self_intpart + "0" * (self_exp - other_exp)
            other_padded = other_intpart + "0" * (other_exp - self_exp)
            if self_padded == other_padded:
                return 0
            elif self_padded < other_padded:
                return -((-1) ** self._sign)
            else:
                return (-1) ** self._sign
        elif self_adjusted > other_adjusted:
            return (-1) ** self._sign
        else:  # self_adjusted < other_adjusted
            return -((-1) ** self._sign)

    def compare(self: Binary, other: Any) -> Binary:
        """Compare self to other. Return a Binary value.

        a or b is a NaN ==> Binary('NaN')
        a < b           ==> Binary('-1')
        a == b          ==> Binary('0')
        a > b           ==> Binary('1')

        Parameters:
        other (str, Binary): object to compare to

        Returns:
        Binary: -1 s<o, 0 equal, 1 s>o
        """
        return Binary(self._cmp(other))

    def __eq__(self: Binary, other: Any) -> bool:
        """Implements equal, implements operand ==.

        See _cmp() for details.

        Method that implements "==" operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

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

        Method that implements "<" operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

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

        Method that implements ">" operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

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

        Method that implements "<=" operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

        Returns:
        bool: result
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return False  # see comments in _cmp()
        return not self._cmp(other) == 1

    def __ge__(self: Binary, other: Any) -> bool:
        """Greater or equal operation.

        Method that implements ">=" operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

        Returns:
        bool: result
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if not isinstance(other, Binary):
            other = Binary(other)
        if self.isnan() or other.isnan():
            return False  # see comments in _cmp()
        return not self._cmp(other) == -1

    def __add__(self: Binary, other: Any) -> Binary:
        """Add operation.

        Method that implements the + operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

        Returns:
        Binary: addittion of the two numbers
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

        Method that implements the - operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

        Returns:
        Binary: addittion of the two numbers
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

        Method that implements the * operand.

        Parameters:
        self (Binary): binary number
        other (Any): number

        Returns:
        Binary: multiplication of the two numbers
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

        Method that implements the / operand.

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

        Method that implements the // operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

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
        """Compute modulo operation.

        Method that implements modulo, i.e. it returns the integer remainder.
        Method that implements the % operand.

        Parameters:
        self (Binary): binary number
        other (Any): binary number

        Returns:
        Binary: modulation of the two numbers
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

        Method that implements the ** operand.

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
        """Compute absolute value.

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
        """Perform math ceiling operation.

        Method that implements ceiling. Method for "ceil".
        For example, '1.11' will return '10'.
        Note, that math.ceil() will return an int.

        Parameters:
        self (Binary): binary number

        Returns:
        int: ceiling of the number
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

    def __floor__(self: Binary) -> int:
        """Perform math floor operation.

        Method that implements floor.
        For example, '1.11' will return '1'.
        Note, that math.floor() will return an int.

        Parameters:
        self (Binary): binary number

        Returns:
        Binary: floor of the number
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

    def __rshift__(self: Binary, ndigits: int) -> Binary:
        """Shifts number n digits (bits) to the right.

        Method that implementes >> operand.

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
        """Shifts number n digits (bits) to the left.

        Method that implementes << operand.

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
        """Boolean transformation. Used for bool() and not operand.

        Method that implements transformation to boolean. This
        boolian transformation is then used by operations like "not".

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

        Method that implements the 'not' operand.
        Do not confuse it with the 'bitwise not' operand ~.

        If self is 0, then method returns True.
        For all other values it returns False.

        For example: not Binary(0) returns True.
        For example: not Binary(3.5) returns False.

        Parameters:
        self (Binary): number

        Returns:
        Binary: 'boolean not' of number
        """
        return not self._fraction

    def __and__(self: Binary, other: Any) -> Binary:
        """Return the bitwise 'and' of self and other.

        Method that implements the & operand.

        For example, '11.1' & '10.1' will return '10.1'
        '-0.1' & '+1' will return '-1' because twos-complement of
        '-0.1' is 1.1; and 1.1 & 01.0 results in twos-complement 1.0;
        and 1.0 in twos-complement is '-1' in binary fraction.
        In short, any negative number will be converted into twos-complement
        representation, than bitwise-and will be done, then the resulting
        number will be converted back from twos-complement to
        binary string format.

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
        # TODO needs to be implemented
        return Binary._and_or(self, other, "and")

    def __or__(self: Binary, other: Any) -> Binary:
        """Return the bitwise 'or' of self and other.

        Method that implements the | operand.

        For example, '11.1' | '10.1' will return '11.1'
        '-0.1' | '+1' will return '-0.1' because twos-complement of
        '-0.1' is 1.1; and 1.1 | 01.0 results in twos-complement 1.1;
        and 1.1 in twos-complement is '-0.1' in binary fraction.
        In short, any negative number will be converted into twos-complement
        representation, than bitwise-or will be done, then the resulting
        number will be converted back from twos-complement to
        binary string format.

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
        # TODO needs to be implemented
        return Binary._and_or(self, other, "or")

    def __xor__(self: Binary, other: Any) -> Binary:
        """Return the bitwise 'xor' of self and other.

        Method that implements the ^ operand.

        For example, '11.1' ^ '10.1' will return '1'.
        '-0.1' ^ '+1' will return '-1.1' because twos-complement of
        '-0.1' is 1.1; and 1.1 ^ 01.0 results in twos-complement 10.1;
        and 10.1 in twos-complement is '-1.1' in binary fraction.
        In short, any negative number will be converted into twos-complement
        representation, than bitwise-or will be done, then the resulting
        number will be converted back from twos-complement to
        binary string format.

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
        # TODO needs to be implemented
        return Binary._and_or(self, other, "xor")

    def _and_or(this: Binary, other: Binary, which: str) -> Binary:
        """Performs bitwise 'and', 'or', or 'xor' on two binary fractions.

        This is a function, not a method.

        Parameters:
        this (Binary): number, binary fraction
        other (Binary): number, binary fraction
        which (str): 'and' or 'or' or 'xor'

        Returns:
        Binary: 'and'ed or 'or'ed binary fraction
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

        # TODO: make this work with negative numbers
        # TODO: make this work for 'xor'
        # TODO: I have not looked at this function at all, but I doubt that it will be correct
        # remove exponent on both args, operate on strings
        # convert any of the 2 negative args into twos-complement representation
        # TODO needs to be implemented

        sign1, intpart1, fracpart1, exp1 = this.components()
        sign2, intpart2, fracpart2, exp2 = other.components()
        # print("Fracpart: ", fracpart1, fracpart2)

        def operation(a, b, li):
            number = ""
            for i in range(li):
                if which == "and":
                    if a[i] == b[i]:
                        number += a[i]
                    else:
                        number += "0"
                elif which == "or":
                    if int(a[i]) or int(b[i]):
                        number += "1"
                    else:
                        number += "0"
            return number

        if sign1 == 0 and sign2 == 0:
            intl = len(intpart1) if len(intpart1) > len(intpart2) else len(intpart2)
            fracl = (
                len(fracpart1) if len(fracpart1) > len(fracpart2) else len(fracpart2)
            )
            intpart1 = (intl - len(intpart1)) * "0" + intpart1
            intpart2 = (intl - len(intpart2)) * "0" + intpart2
            fracpart1 = fracpart1 + (fracl - len(fracpart1)) * "0"
            fracpart2 = fracpart2 + (fracl - len(fracpart2)) * "0"

            result = operation(intpart1, intpart2, intl)
            if len(result) > 1 and int(result) == 0:
                result = "0"
            result += "."
            result += operation(fracpart1, fracpart2, fracl)

        else:  # TODO: this looks buggy: nothing to do for negative numbers?
            result = "0"
        return Binary(Binary.simplify(result))

    def __invert__(self: Binary) -> Binary:
        """Returns the 'bitwise not' of self.

        Method that implements the ~ operand.
        This is also called the 'invert' operand, or the 'bitwise not' operand.
        Do not confuse it with the 'boolean not' operand implemented
        via the 'not' operand and the __not__() method.

        It is only defined for integers. If self is not an integer it
        will raise an exception. For integers ~ is defined as
        ~n = -(n+1). For example, ~9 will return -10. ~-10 will return 9.
        For more information, see also the invert() function.

        Parameters:
        self (Binary): number

        Returns:
        Binary: 'bitwise not' of integer number
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
                "~ operand only allowed on integers or fractions. "
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

        Binary uses module unittest for unit testing.
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

    def test_to_not_exponential(self):
        """Test function/method."""
        self.assertEqual(TwosComplement.to_not_exponential("0"), "0")
        self.assertEqual(TwosComplement.to_not_exponential("1"), "1")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e4"), "10100")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e3"), "1010")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e2"), "101")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e1"), "10.1")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e0"), "1.01")
        self.assertEqual(
            TwosComplement.to_not_exponential("11.01e4", strict=True), "110100"
        )
        self.assertEqual(
            TwosComplement.to_not_exponential("11.01e3", strict=True), "11010"
        )
        self.assertEqual(
            TwosComplement.to_not_exponential("11.01e2", strict=True), "1101"
        )
        self.assertEqual(
            TwosComplement.to_not_exponential("11.01e1", strict=True), "110.1"
        )
        self.assertEqual(
            TwosComplement.to_not_exponential("11.01e0", strict=True), "11.01"
        )
        self.assertEqual(TwosComplement.to_not_exponential("11.01e-1"), "1.101")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e-2"), "1.1101")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e-3"), "1.11101")
        self.assertEqual(TwosComplement.to_not_exponential("11.01e-4"), "1.111101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e4"), "0110100")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e3"), "011010")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e2"), "01101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e1"), "0110.1")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e0"), "011.01")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-1"), "01.101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-2"), "0.1101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-3"), "0.01101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-4"), "0.001101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e2"), "01101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e+2"), "01101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e4"), "0110100")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-4"), "0.001101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-2"), "0.1101")
        self.assertEqual(TwosComplement.to_not_exponential("0.1e-1"), "0.01")
        self.assertEqual(TwosComplement.to_not_exponential("1.111e0"), "1.111")
        self.assertEqual(TwosComplement.to_not_exponential("1.11e0"), "1.11")
        self.assertEqual(TwosComplement.to_not_exponential("1.1e0"), "1.1")
        self.assertEqual(TwosComplement.to_not_exponential("1.e0"), "1")
        self.assertEqual(TwosComplement.to_not_exponential("1.e1"), "10")
        self.assertEqual(TwosComplement.to_not_exponential("1.01e2"), "101")
        self.assertEqual(TwosComplement.to_not_exponential("1.01e1"), "10.1")
        self.assertEqual(TwosComplement.to_not_exponential("1.011e2"), "101.1")
        self.assertEqual(TwosComplement.to_not_exponential("1111000e-0"), "1000")
        self.assertEqual(TwosComplement.to_not_exponential("1111000e-3"), "1")
        self.assertEqual(TwosComplement.to_not_exponential("1111000000.e-3"), "1000")
        self.assertEqual(TwosComplement.to_not_exponential("1111000e+3"), "1000000")
        self.assertEqual(TwosComplement.to_not_exponential("1111e+3"), "1000")
        self.assertEqual(TwosComplement.to_not_exponential("1111.1e+3"), "100")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-02"), "0.1101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-02", -1), "0.1101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-02", 7), "00.1101")
        self.assertEqual(TwosComplement.to_not_exponential("011.01e-02", 8), "000.1101")
        self.assertEqual(TwosComplement.to_not_exponential("0.01"), "0.01")
        self.assertEqual(TwosComplement.to_not_exponential("1.111"), "1.111")
        self.assertEqual(TwosComplement.to_not_exponential("1.11"), "1.11")
        self.assertEqual(TwosComplement.to_not_exponential("1.1"), "1.1")
        self.assertEqual(TwosComplement.to_not_exponential("111"), "1")
        self.assertEqual(TwosComplement.to_not_exponential("10.000"), "10")
        self.assertEqual(TwosComplement.to_not_exponential("101.000e0"), "101")
        self.assertEqual(TwosComplement.to_not_exponential("10.10"), "10.1")
        self.assertEqual(TwosComplement.to_not_exponential("101.1e-0"), "101.1")
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("0b1")  # leading 0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("0b01")  # leading 0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("-0b1")  # leading -0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("-0b01")  # leading -0b not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("-1")  # leading - not allowed
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("")  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("1", 0)  # should fail
        with self.assertRaises(OverflowError):
            TwosComplement.to_not_exponential("11100", 1)  # should fail
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("111", 0)  # should fail
        with self.assertRaises(OverflowError):
            TwosComplement.to_not_exponential("0111", 2)  # should fail
        with self.assertRaises(OverflowError):
            TwosComplement.to_not_exponential("011.01e-02", 5)
        with self.assertRaises(ValueError):
            TwosComplement.to_not_exponential("-0b10")  # should fail
        with self.assertRaises(TypeError):
            TwosComplement.to_not_exponential(1)  # should fail
        with self.assertRaises(TypeError):
            TwosComplement.to_not_exponential("1", "-1")  # should fail

    def test_invert(self):
        """Test function/method."""
        self.assertIsInstance(TwosComplement.invert("1"), str)
        self.assertEqual(TwosComplement.invert("0001000", True), "1110111")
        self.assertEqual(TwosComplement.invert("0001000", strict=False), "10111")
        self.assertEqual(TwosComplement.invert("1110110", strict=False), "01001")
        self.assertEqual(TwosComplement.invert("0.1101", strict=True), "1.0010")
        self.assertEqual(TwosComplement.invert("0.1101", strict=False), "1.001")
        self.assertEqual(TwosComplement.invert("11.1101", strict=False), "0.001")
        self.assertEqual(TwosComplement.invert("00.1101", strict=False), "1.001")
        self.assertEqual(TwosComplement.invert("01"), "10")
        self.assertEqual(TwosComplement.invert("0"), "1")
        self.assertEqual(TwosComplement.invert("1"), "0")
        self.assertEqual(TwosComplement.invert("10"), "01")
        self.assertEqual(TwosComplement.invert("101"), "010")
        self.assertEqual(TwosComplement.invert("101010"), "010101")
        self.assertEqual(TwosComplement.invert("0101010"), "1010101")
        self.assertEqual(TwosComplement.invert("101.010"), "010.101")
        self.assertEqual(TwosComplement.invert("010.1010"), "101.0101")
        self.assertEqual(TwosComplement.invert("1e1"), "01")
        self.assertEqual(TwosComplement.invert("0101010e-3", strict=True), "1010101e-3")
        self.assertEqual(TwosComplement.invert("0101010e-3"), "1010101e-3")
        self.assertEqual(TwosComplement.invert("1010101e0"), "0101010")
        self.assertEqual(TwosComplement.invert("0101010e-0"), "1010101")
        self.assertEqual(TwosComplement.invert("1010101e-34"), "0101010e-34")
        self.assertEqual(TwosComplement.invert("0101010e-34"), "1010101e-34")
        self.assertEqual(
            TwosComplement.invert("101010e34"),
            "0101011111111111111111111111111111111111",
        )
        self.assertEqual(TwosComplement.invert("010.1010e-34"), "101.0101e-34")
        self.assertEqual(
            TwosComplement.invert("101.010e34"), "0101011111111111111111111111111111111"
        )
        self.assertEqual(
            TwosComplement.invert(TwosComplement.invert("0101010e-34")), "0101010e-34"
        )
        self.assertEqual(
            TwosComplement.invert(TwosComplement.invert("101010e34")),
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

        Binary uses module unittest for unit testing.
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

    def test_from_float(self):
        """Testing from_float() function."""
        self.assertEqual(Binary.from_float(float("inf")), "inf")
        self.assertEqual(Binary.from_float(float("-inf")), "-inf")
        self.assertEqual(Binary.from_float(float("-nan")), "nan")
        self.assertEqual(Binary.from_float(-3.5), "-0b11.1")
        self.assertEqual(Binary.from_float(-0.0), "0b0")
        self.assertEqual(Binary.from_float(8.25), "0b1000.01")
        with self.assertRaises(TypeError):
            Binary.from_float("1")  # should fail

    def test_to_float(self):
        """Test to_float() function."""
        self.assertEqual(Binary.to_float("inf"), float("inf"))
        self.assertEqual(Binary.to_float("-inf"), float("-inf"))
        self.assertEqual(math.isnan(Binary.to_float("-nan")), True)
        self.assertEqual(Binary.to_float("-0b11.1"), -3.5)
        self.assertEqual(Binary.to_float("0b0"), 0)
        self.assertEqual(Binary.to_float("0b1000.01"), 8.25)
        with self.assertRaises(ValueError):
            Binary.to_float("2")  # should fail

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

    def test_to_not_exponential(self):
        """Test function/method."""
        self.assertEqual(Binary.to_not_exponential("-0"), "0")
        self.assertEqual(Binary.to_not_exponential("11.01e-2"), "0.1101")
        self.assertEqual(Binary.to_not_exponential("-11.01e-2"), "-0.1101")
        self.assertEqual(Binary.to_not_exponential("-11.01e-3"), "-0.01101")
        self.assertEqual(Binary.to_not_exponential("-11.01e-4"), "-0.001101")
        self.assertEqual(Binary.to_not_exponential("11.01e2"), "1101")
        self.assertEqual(Binary.to_not_exponential("-11.01e+2"), "-1101")
        self.assertEqual(Binary.to_not_exponential("11.01e4"), "110100")
        self.assertEqual(Binary.to_not_exponential("-11.01e+4"), "-110100")
        self.assertEqual(Binary.to_not_exponential("11.01e4", True), "0b110100")
        self.assertEqual(Binary.to_not_exponential("-11.01e+4", True), "-0b110100")
        self.assertEqual(Binary.to_not_exponential(Binary("Inf")), "Infinity")
        self.assertEqual(Binary.to_not_exponential(Binary("-0")), "0b0")
        self.assertEqual(Binary.to_not_exponential(Binary("11.01e-2")), "0b0.1101")
        self.assertEqual(Binary.to_not_exponential(Binary("-11.01e-2")), "-0b0.1101")
        self.assertEqual(Binary.to_not_exponential(Binary("-11.01e-3")), "-0b0.01101")
        self.assertEqual(Binary.to_not_exponential(Binary("-11.01e-4")), "-0b0.001101")
        self.assertEqual(Binary.to_not_exponential(Binary("11.01e2")), "0b1101")
        self.assertEqual(Binary.to_not_exponential(Binary("-11.01e+2")), "-0b1101")
        self.assertEqual(Binary.to_not_exponential(Binary("11.01e4")), "0b110100")
        self.assertEqual(Binary.to_not_exponential(Binary("-11.01e+4")), "-0b110100")
        with self.assertRaises(ValueError):
            Binary.to_not_exponential("")  # should fail
        with self.assertRaises(TypeError):
            Binary.to_not_exponential(1)  # should fail

    def test_to_fraction(self):
        """Test function/method."""
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
        self.assertEqual(round(Binary(3.75), 1), "11.1")
        # TODO

    def test_round(self):
        """Test function/method for rounding."""
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

    def test_to_simple_exponential(self):
        """Test function/method."""
        self.assertEqual(
            Binary("-11").to_simple_exponential().compare_representation("-11e0"),
            True,
        )
        self.assertEqual(
            Binary("-11e-0").to_simple_exponential().compare_representation("-11e0"),
            True,
        )
        self.assertEqual(
            Binary("-11e+0").to_simple_exponential().compare_representation("-11e0"),
            True,
        )
        self.assertEqual(
            Binary("+11").to_simple_exponential().compare_representation("11e0"),
            True,
        )
        self.assertEqual(
            Binary("1.1").to_simple_exponential().compare_representation("11e-1"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_simple_exponential().compare_representation("-1e-4"),
            True,
        )
        self.assertEqual(
            Binary("-1.1").to_simple_exponential().compare_representation("-11e-1"),
            True,
        )
        self.assertEqual(
            Binary("-1.1e-1").to_simple_exponential().compare_representation("-11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+1.1e-1").to_simple_exponential().compare_representation("11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+1.1000e-1")
            .to_simple_exponential()
            .compare_representation("11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+0001.1000e-1")
            .to_simple_exponential()
            .compare_representation("11e-2"),
            True,
        )
        self.assertEqual(
            Binary("+0001.1000e+1")
            .to_simple_exponential()
            .compare_representation("11e0"),
            True,
        )
        self.assertEqual(
            Binary("+0001.1000e+10")
            .to_simple_exponential()
            .compare_representation("11e9"),
            True,
        )
        with self.assertRaises(TypeError):
            Binary(1).to_simple_exponential(1)  # should fail
        with self.assertRaises(OverflowError):
            Binary("Nan").to_simple_exponential()  # should fail

    def test_to_sci_exponential(self):
        """Test function/method."""
        self.assertEqual(
            Binary("101e2").to_sci_exponential().compare_representation("1.01e4"),
            True,
        )
        self.assertEqual(
            Binary("1.1").to_sci_exponential().compare_representation("1.1e0"), True
        )
        self.assertEqual(
            Binary("-000101e002")
            .to_sci_exponential()
            .compare_representation("-1.01e4"),
            True,
        )
        self.assertEqual(
            Binary("-001.100").to_sci_exponential().compare_representation("-1.1e0"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_sci_exponential().compare_representation("-1e-4"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001e-2").to_sci_exponential().compare_representation("-1e-7"),
            True,
        )
        self.assertEqual(
            Binary("+0.00001e+2").to_sci_exponential().compare_representation("1e-3"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e-2")
            .to_sci_exponential()
            .compare_representation("-1.01e-7"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e+2")
            .to_sci_exponential()
            .compare_representation("-1.01e-3"),
            True,
        )
        with self.assertRaises(TypeError):
            Binary(1).to_sci_exponential(1)  # should fail
        with self.assertRaises(OverflowError):
            Binary("Nan").to_sci_exponential()  # should fail

    def test_to_eng_exponential(self):
        """Test function/method."""
        self.assertEqual(
            Binary("101e2").to_eng_exponential().compare_representation("10.1e3"),
            True,
        )
        self.assertEqual(
            Binary("1.1").to_eng_exponential().compare_representation("1.1"), True
        )
        self.assertEqual(
            Binary("-000101e002")
            .to_eng_exponential()
            .compare_representation("-10.1e3"),
            True,
        )
        self.assertEqual(
            Binary("-001.100").to_eng_exponential().compare_representation("-1.1"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_eng_exponential().compare_representation("-100e-6"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001e-2")
            .to_eng_exponential()
            .compare_representation("-100e-9"),
            True,
        )
        self.assertEqual(
            Binary("+0.00001e+2").to_eng_exponential().compare_representation("1e-3"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e-2")
            .to_eng_exponential()
            .compare_representation("-101e-9"),
            True,
        )
        self.assertEqual(
            Binary("-0.00001010e+2")
            .to_eng_exponential()
            .compare_representation("-1.01e-3"),
            True,
        )
        self.assertEqual(
            Binary("1.1").to_eng_exponential().compare_representation("1.1"),
            True,
        )
        self.assertEqual(
            Binary("1.1111").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("100.1111").to_eng_exponential().compare_representation("100.1111"),
            True,
        )
        self.assertEqual(
            Binary("1000.1111")
            .to_eng_exponential()
            .compare_representation("1.0001111e3"),
            True,
        )
        self.assertEqual(
            Binary("1").to_eng_exponential().compare_representation("1"),
            True,
        )
        self.assertEqual(
            Binary("10").to_eng_exponential().compare_representation("10"),
            True,
        )
        self.assertEqual(
            Binary("100").to_eng_exponential().compare_representation("100"),
            True,
        )
        self.assertEqual(
            Binary("1000").to_eng_exponential().compare_representation("1e3"),
            True,
        )
        self.assertEqual(
            Binary("10000").to_eng_exponential().compare_representation("10e3"),
            True,
        )
        self.assertEqual(
            Binary("100000").to_eng_exponential().compare_representation("100e3"),
            True,
        )
        self.assertEqual(
            Binary("1000000").to_eng_exponential().compare_representation("1e6"),
            True,
        )
        self.assertEqual(
            Binary("1.1111").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("10.1111").to_eng_exponential().compare_representation("10.1111"),
            True,
        )
        self.assertEqual(
            Binary("100.1111").to_eng_exponential().compare_representation("100.1111"),
            True,
        )
        self.assertEqual(
            Binary("1000.1111").to_eng_exponential().compare_representation("1e3.1111"),
            True,
        )
        self.assertEqual(
            Binary("10000.1111")
            .to_eng_exponential()
            .compare_representation("10e3.1111"),
            True,
        )
        self.assertEqual(
            Binary("100000.1111")
            .to_eng_exponential()
            .compare_representation("100e3.1111"),
            True,
        )
        self.assertEqual(
            Binary("1000000.1111")
            .to_eng_exponential()
            .compare_representation("1e6.1111"),
            True,
        )
        self.assertEqual(
            Binary("1.1111e0").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("11.111e-1").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("111.11e-2").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("1111.1e-3").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("11111.e-4").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".11111e1").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".011111e2").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary(".0011111e3").to_eng_exponential().compare_representation("1.1111"),
            True,
        )
        self.assertEqual(
            Binary("-0.01e-2").to_eng_exponential().compare_representation("-1e-3"),
            True,
        )
        self.assertEqual(
            Binary("-0.0001e-4" == -0.00000001)
            .to_eng_exponential()
            .compare_representation("-10e-9"),
            True,
        )
        self.assertEqual(
            Binary("-0.0001111e-4" == -0.00000001111)
            .to_eng_exponential()
            .compare_representation("-11.11e-9"),
            True,
        )
        with self.assertRaises(TypeError):
            Binary(1).to_eng_exponential(1)  # should fail
        with self.assertRaises(OverflowError):
            Binary("Nan").to_eng_exponential()  # should fail

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

    def test_value(self):
        """Test function/method."""
        self.assertEqual(isinstance(Binary(0).value(), str), True)
        self.assertEqual(isinstance(Binary("0").value(), str), True)

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
                Fraction(2 ** 1000 + 2 ** 0, -1 * 2 ** 1001), ndigits=10, strict=True
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
        self.assertEqual(Binary("1000") & Binary("0"), Binary(0))
        self.assertEqual(Binary("1010") & Binary("10"), Binary("10"))
        self.assertEqual(Binary("1010") & Binary("11"), Binary("10"))
        self.assertEqual(Binary("1111") & Binary("10"), Binary("10"))
        self.assertEqual(Binary("1.1000") & Binary("0.0"), Binary(0))
        self.assertEqual(Binary("1.1010") & Binary("0.10"), Binary("0.1"))
        self.assertEqual(Binary("1.1010") & Binary("0.11"), Binary("0.1"))
        self.assertEqual(Binary("1.1111") & Binary("0.10"), Binary("0.1"))
        self.assertEqual(Binary("-0.1") & Binary("+1"), -1)
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
        for ii in [-12, -11.57, -8, -1, -0.87, 0, 0.76, 1.2, 2, 2.4, 8, 2322.2343]:
            self.assertEqual(
                Binary(Binary.from_twoscomplement(Binary(ii).to_twoscomplement())),
                Binary(ii),
            )
        self.assertEqual(Binary.from_twoscomplement(TwosComplement("10.1")), "-1.1")
        self.assertEqual(Binary.from_twoscomplement("11"), "-1")
        self.assertEqual(Binary.from_twoscomplement("11.111"), "-1.001")
        self.assertEqual(Binary.from_twoscomplement("110.111"), "-10.001")
        self.assertEqual(Binary.from_twoscomplement("110.001"), "-10.111")
        self.assertEqual(Binary.from_twoscomplement("110"), "-10")
        self.assertEqual(Binary.from_twoscomplement("00"), "0")
        self.assertEqual(Binary.from_twoscomplement("01"), "1")
        self.assertEqual(Binary.from_twoscomplement("00.11"), "0.11")
        self.assertEqual(
            Binary.from_twoscomplement("00.11111111111110"), "0.1111111111111"
        )
        self.assertEqual(Binary.from_twoscomplement("00.11e-5"), "0.11e-5")
        self.assertEqual(
            Binary.from_twoscomplement("00.11111111111110"), "0.1111111111111"
        )
        self.assertEqual(Binary.from_twoscomplement("00.00", strict=True), "00.00")
        with self.assertRaises(ValueError):
            Binary.from_twoscomplement("102")  # should fail
        with self.assertRaises(ValueError):
            Binary.from_twoscomplement("0b10")  # should fail
        with self.assertRaises(TypeError):
            Binary.from_twoscomplement(Binary(1))  # should fail
        with self.assertRaises(ArithmeticError):
            Binary.from_twoscomplement("inf")
        with self.assertRaises(ArithmeticError):
            Binary.from_twoscomplement("-Inf")
        with self.assertRaises(ArithmeticError):
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
