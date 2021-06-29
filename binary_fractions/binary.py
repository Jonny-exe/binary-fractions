#!/usr/bin/python3


"""# Floating-point Binary Fractions: Do math in base 2!

![logo](binary-fractions.svg)

```
 █████      ███
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

    ██████                                █████     ███
   ███░░███                              ░░███     ░░░
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

Many operations and transformations are offered.
You can sum, subtract, multiply, divide, compute power of, etc.
of long floating-point binary fractions.

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
     ||   |    | exponent in base 10 (not base 2!)
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
- supports many methods: lshift, rshift, not, round, floor, ceil, ...
- very high precision
- many operations are lossless, i.e. with no rounding errors or loss of precision
- supports very long binary fractions
- supports exponential representations
- well documented. Please read the documentation inside the source code
  ([binary.py](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/binary.py)).
  Or look at the pydoc-generated documentation in
  [README.md](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/README.md).


## Sample usage, Example calls:

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
>>> b.to_simple_exponential() # no comma
Binary(10000000000001010101011100101000011010111100101000011e-32, 0, False)
>>> b.to_sci_exponential() # 1 digit before comma
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
```

"""

# TODO: go to stackoverflow.com, search for "binary math", "binary fractions"
# and where there are matches add comment/entry to reference this module
# in PyPi

from fractions import Fraction
import math  # isclose()
import re
import sys

_BINARY_WARNED_ABOUT_FLOAT = False
_BINARY_RELATIVE_TOLERANCE = 1e-10
_BINARY_PRECISION = 128  # number of binary digits to the right of decimal point
_PREFIX = "0b"
_EXP = "e"
# _BINARY_VERSION will be set automatically with git hook upon commit
_BINARY_VERSION = "20210622-155037"  # format: date +%Y%m%d-%H%M%S

# see implementation of class Decimal:
# https://github.com/python/cpython/blob/3.9/Lib/_pydecimal.py
# https://docs.python.org/3/library/decimal.html
# see implementation of class Fraction:
# https://github.com/python/cpython/blob/3.9/Lib/fractions.py
# https://docs.python.org/3/library/fractions.html
# https://github.com/bradley101/fraction/blob/master/fraction/Fraction.py


class Binary(object):
    """Floating point class for binary fractions and arithmetic."""

    def __new__(cls, value: [int, float, str, Fraction] = "0", simplify: bool = True):
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
                        # # version A: this normalizes to remove comma
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
                        self._value = "NaN"  # N
                    else:
                        self._value = "NaN"  # n
                else:
                    # infinity
                    self._value = sign + "Infinity"  # F
            # self._value = Binary.to_not_exponential(self._value) # not strictly needed
            if not self._is_special:
                self._fraction = Binary.string_to_fraction(self._value)
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
                    self._value = "NaN"
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
                self._fraction = Binary.string_to_fraction(self._value)
            return self

        # From another Binary
        if isinstance(value, Binary):
            self._sign = value._sign
            self._value = value._value
            self._fraction = value._fraction
            self._is_lossless = value._is_lossless
            self._is_special = value._is_special
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
            if not _BINARY_WARNED_ABOUT_FLOAT:
                _BINARY_WARNED_ABOUT_FLOAT = True
                print("Warning: mixing floats and Binary")
            self._fraction = Fraction(value)
            self._value = Binary.fraction_to_string(value)
            self._sign = 1 if value < 0 else 0
            return self

        # any other types
        raise TypeError(f"Cannot convert {value} to Binary")

    def test___new__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed

        # type should be Binary, not string
        re = Binary.testcase(tc, "Binary" in str(type(Binary(5))), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, isinstance(Binary.version(), str), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary("0")), 0.0)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary("1.1")), 1.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary("-1.11")), -1.75)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(-3.5), "-11.1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(-3.5), "-0b11.1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, str(Binary(-3.5)), "-0b11.1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary((1, (1, 0, 1, 0), -2)).compare_representation("-1010e-2"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("102")  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(complex(1, 1))  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def version() -> str:
        """Give version number.

        Is a utility function.

        Returns:
        str: version number as date in format "YYMMDD-HHMMSS", e.g. "20210622-103815"
        """
        return _BINARY_VERSION

    def test_version(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, len(Binary.version()), len("20210622-103815"))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.version()[8], "-")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def from_float(value: float, rel_tol: float = _BINARY_RELATIVE_TOLERANCE):
        """Convert from float to Binary.

        utility function
        float --> Binary
        could also use method float.hex()

        Parameters:
        value (float): value of number
        rel_tol (float): relative tolerance to know when to stop converting
            relates to precision

        Returns:
        str: string representation of Binary
        """
        if not isinstance(value, float):
            raise TypeError(f"Argument {value} must be of type float.")
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
        return Binary.clean(sign + intpart + "." + fracpart)

    def __float__(self):
        """Convert from Binary to float.

        method
        Binary --> float or integer

        Returns:
        float: number as float or integer
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self.isinfinity():
            result = float("Inf")
        else:
            result = float(self._fraction)
        # alternative implementation of float
        # result = Binary.to_float(self._value)
        return result  # float or integer

    def test___float__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, float(Binary("-1")), -1.0)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary("-1.1")), -1.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary("1.001")), 1.125)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary((1, (1, 0, 1, 0), -2))), -2.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary(-13.0 - 2 ** -10)), -13.0009765625)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary(13.0 + 2 ** -20)), 13.000000953674316)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary(13.0 + 2 ** -30)), 13.000000000931323)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, float(Binary("Inf")), float("Inf"))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __int__(self):
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

    def test___int__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, int(Binary("-1")), -1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, int(Binary("-1.111")), -1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, int(Binary("1.001")), 1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, int(Binary((1, (1, 0, 1, 0), -2))), -2)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, int(Binary(-13.0 - 2 ** -10)), -13)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, int(Binary(13.0 + 2 ** -20)), 13)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, int(Binary(13.0 + 2 ** -30)), 13)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            int(Binary("Inf"))  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def to_float(value: str):
        """Convert from Binary string to float or integer.

        utility function
        Binary string --> float or integer
        could also use inverse of method float.hex()

        Parameters:
        value (str): binary string representation of number

        Returns:
        float or integer: number as float or integer
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # print(f"not normalized is {value}")
        value = Binary.to_not_exponential(value)
        # print(f"normalized is {value}")
        li = value.split(".")
        intpart = li[0]
        result = int(intpart, 2)
        if result < 0:
            sign = -1
        else:
            sign = 1
        # print(f"int result is {result}")
        if len(li) == 1:
            fracpart = ""
            return result  # an integer
        else:
            fracpart = li[1]

        # print(f"fracpart is {fracpart}")
        le = len(fracpart)
        for i in range(le):
            if fracpart[i] == "1":
                result += (2 ** -(i + 1)) * sign
        return result  # float

    def clean(value: str) -> str:
        """Clean up string representation.

        utility function
        Example: convert '11.0' to '11'

        Parameters:
        value (str): binary string representation of number

        Returns:
        str: binary string representation of number
        """
        if "." in value:
            result = value.rstrip("0").rstrip(".")
        elif "1" in value:
            result = value
        else:
            result = value
        if result == "-0":
            result = "0"
        return result

    def to_not_exponential(value: str) -> str:
        """Normalize string representation. Remove exponent part.

        utility function
        remove exponent, fully "decimal"
        Example: convert '11.01e-2' to '0.1101'

        Parameters:
        value (str): binary string representation of number

        Returns:
        str: binary string representation of number
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # print(f"before normalize {value}")
        if _EXP not in value:
            result = Binary.clean(value)
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
                    intpart = "0" * (abs(exp) - lenintpart) + intpart
                    result = "0." + intpart + fracpart
                else:
                    fracpart = intpart[exp:] + fracpart
                    if intpart[:exp] == "" or intpart[:exp] == "-":
                        intpart = "0"
                    else:
                        intpart = intpart[:exp]
                    result = intpart + "." + fracpart
        result = Binary.clean(result)
        # print(f"after normalize {result}")
        return result

    def twos_complement_to_not_exponential(value: str):
        sign, intpart, fracpart, exp = Binary.get_twoscomplement_components()
        # # TODO: you only wrote 2 lines of code???
        return None  # TODO

    def binary_string_to_fraction(value):
        """Convert string representation of binary to Fraction.

        utility function

        Parameters:
        value (str): binary number as string

        Returns:
        Fraction: value as fraction
        """
        sign, intpart, fracpart, exp = Binary.get_components(value)
        exp -= len(fracpart)
        if exp > 0:
            result = Fraction((-1) ** sign * int(intpart + fracpart, 2) * (2 ** exp), 1)
        else:
            result = Fraction((-1) ** sign * int(intpart + fracpart, 2), 2 ** -exp)
        return result

    def test_binary_string_to_fraction(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed

        re = Binary.testcase(tc, Binary.binary_string_to_fraction("1"), Fraction(1))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.binary_string_to_fraction("0"), Fraction(0))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.binary_string_to_fraction("0.1"), Fraction(0.5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.binary_string_to_fraction("1.1"), Fraction(1.5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.binary_string_to_fraction("1.1"), Fraction(1.5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.binary_string_to_fraction("-1"), Fraction(-1))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.binary_string_to_fraction("-0.1"), Fraction(-0.5)
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.binary_string_to_fraction("-1.1"), Fraction(-1.5)
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.binary_string_to_fraction("-1.1e2"), Fraction(-6)
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.binary_string_to_fraction("-1.1e0"), Fraction(-1.5)
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.binary_string_to_fraction("1.1e-3"), Fraction(3, 16)
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.binary_string_to_fraction("-1.1e-3"), Fraction(-3, 16)
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.binary_string_to_fraction("102")  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.binary_string_to_fraction(Binary(1))  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __round__(self):
        """Normalize and round number to n digits after comma.

        method, see round_to()

        Parameters:
        ndigits (int): number of digits after comma, precision

        Returns:
        Binary: binary string representation of number
        """
        ndigits = 0
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        result = Binary.round_to(value, ndigits)
        return Binary(result)

    def round(self, ndigits=0):
        """Normalize and round number to n digits after comma.

        method, see round_to()

        Parameters:
        ndigits (int): number of digits after comma, precision

        Returns:
        Binary: binary string representation of number
        """
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        result = Binary.round_to(value, ndigits)
        return Binary(result)

    def round_to(value, ndigits=0):
        """Normalize and round number to n digits after comma.

        utility function
        Example: convert '11.01e-2' to '0.11' with ndigits==2
        convert '0.1' to '0' with ndigits==0
        convert '0.10000001' to '1' with ndigits==0

        Parameters:
        value (str): binary string representation of number
        ndigits (int): number of digits after comma, precision

        Returns:
        str: binary string representation of number
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # print(f"value is {value} of type {type(value)}")
        value = Binary.to_not_exponential(value)
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
            return intpart + "." + fracpart[0:ndigits]
            # round down from 0.10xxx1 to 0.11000 ==> 0.1
        else:
            # round up from 0.1xxxx1 to 0.111111 ==> 1.0
            digits = intpart + fracpart[0:ndigits]
            digits = bin(int(digits, 2) + 1)[2:]  # rounded up
            # print(f'digits is {digits}')
            le = len(digits)
            result = digits[: le - ndigits] + "." + digits[le - ndigits :]
            return Binary.clean(result)

    def fill(self, ndigits=0, strict=False):
        """Normalize and fill number to n digits after comma.

        This is a method. See also function fill_to().

        Parameters:
        ndigits (int): number of digits after comma, precision
        strict (bool): cut off by rounding if input is too long,
            remove precision if True and necessary

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        value = self._value
        return Binary.fill_to(value, ndigits, strict)

    def test_fill(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary("1.1111").fill(1), "1.1111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.1111").fill(4), "1.1111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.1111").fill(5), "1.11110")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.1111").fill(6), "1.111100")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.1111").fill(1, True), "10.0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.1111").fill(4, True), "1.1111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.1111").fill(5, True), "1.11110")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.1111").fill(6, True), "1.111100")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1.0011").fill(1, True), "1.0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.fill(1, "1")  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1).fill(-1)  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def fill_to(value, ndigits=0, strict=False):
        """Normalize and fill number to n digits after comma.

        utility function
        strict==False: if value is longer, don't touch, don't shorten
        strict==True: if value is longer, then shorten, strictly ndigits

        Parameters:
        ndigits (int): number of digits after comma, precision
        strict (bool): cut off by rounding if input is too long,
            remove precision if True and necessary

        Returns:
        str: binary string representation of number
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
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

        # print(f"fracpart is {fracpart}")
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
            # print(f"result is {result}")
            # rounding can shorten it drastically, 0.1111 => 1
            return Binary.fill_to(result, ndigits, strict)

    def to_simple_exponential(self):
        """Convert to exponential representation without fraction.

        A method athat changes the string representation of a number.
        Examples: '1.1' ==> '11e-1',  '-0.01e-2' ==> '-1e-4'
        The result has no decimal point.

        Parameters:
        none

        Returns:
        Binary: binary string representation of number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        value = self._value
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.clean(value)
        else:
            li = value.split(_EXP)
            intfracpart = Binary.clean(li[0])
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

    def test_to_simple_exponential(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(
            tc,
            Binary("1.1").to_simple_exponential().compare_representation("11e-1"),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary("-0.01e-2").to_simple_exponential().compare_representation("-1e-4"),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def to_sci_exponential(self):
        """Convert to exp. representation with single binary digit before comma.

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
        value = self._value
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.clean(value)
        else:
            li = value.split(_EXP)
            intfracpart = Binary.clean(li[0])
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

    def test_to_sci_exponential(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(
            tc,
            Binary("101e2").to_sci_exponential().compare_representation("1.01e4"),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.1").to_sci_exponential().compare_representation("1.1e0"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary("-0.01e-2").to_sci_exponential().compare_representation("-1e-4"),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def get_components(value) -> tuple:
        """Return sign, intpart (without sign), fracpart, exp.

        Example: -11.01e2 ==> (1, '11', '01', 2)

        Parameters:
        value (str): respresentation of a binary

        Returns:
        tuple: tuple of sign, intpart (without sign), fracpart, exp
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        sign = 1 if value[0] == "-" else 0
        if sign:
            value = value[1:]  # remove sign from intpart
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.clean(value)
        else:
            li = value.split(_EXP)
            intfracpart = Binary.clean(li[0])
            exp = int(li[1])

        li = intfracpart.split(".")
        intpart = li[0]
        if len(li) == 1:
            fracpart = ""
        else:
            fracpart = li[1]
        return (sign, intpart, fracpart, exp)

    def get_twoscomplement_components(value, strict=False) -> tuple:
        """Return sign, intpart (indicates sign in first bit), fracpart, exp.

        strict==False: cleanup, remove unnecessary digits, do cleanup
        strict==True: produce exact twos-complement, no cleanup or simplifications

        Examples for strict:
        Example: 3.25*4, input '11.01e2' returns (1, '11', '01', 2).
        Example: 0, input '0' returns (0, '0', '', 0).
        Example: -1, input '1' returns (1, '1', '', 0).
        Example: 1, input '01' returns (0, '01', '', 0).
        Example: -0.5, input 1.1 returns (1, '1', '1', 0).
        Example: neg. number, input 101.010e-4 returns (1, '101', '010', -4).
        Example: pos number, input 0101.010e-2 returns (0, '0101', '010', -4).
        Examples for not strict:
        Example: 3.25*4, input '11.01e2' returns (1, '11', '01', 2).
        Example: 0, input '0' returns (0, '0', '', 0).
        Example: -1, input '1' returns (1, '1', '', 0).
        Example: 1, input '01' returns (0, '01', '', 0).
        Example: -0.5, input 1.1 returns (1, '1', '1', 0).
        Example: neg. number, input 111101.0100e-4 returns (1, '101', '01', -4).
        Example: pos number, input 0000101.0100e-2 returns (0, '0101', '01', -4).

        Parameters:
        value (str): respresentation of a twos-complement string
        strict (bool): if False simplify output by removing unnecessary digits

        Returns:
        tuple: tuple of sign, intpart, fracpart, exp
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")

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
                (E(?P<exp>[-+]?\d+))?    # followed by an optional exponent, or...
            )
            \s*
            \Z
        """,
            re.VERBOSE | re.IGNORECASE,
        ).match

        m = _parser(value)
        if m is None:
            raise ValueError(
                f"Invalid literal for str: {value}."
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

    def components(self) -> tuple:
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

    def isinfinity(self):
        """Determine if object is Infinity.

        Parameters:
        none

        Returns:
        bool: is or is not any kind of infinity or negative infinity
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return "Inf" in self._value

    def isint(self) -> bool:
        """Determines if binary fraction is an integer.

        This is a utility function.

        Returns:
        bool: True if int, False otherwise (Fraction, float)
        """
        return self._fraction == int(self._fraction)

    def istwoscomplement(value: str):
        """Determine if string is a valid twos-complement syntax.

        Parameters:
        none

        Returns:
        bool: is or is not valid twos-complement
        """
        try:
            Binary.get_twoscomplement_components(value)
            # don't catch TypeError
        except ValueError:
            return False
        return True

    def test_istwoscomplement(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary.istwoscomplement("1"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        # TODO: just to tell you: the next line is NOT valid Python Syntax!!!
        # pa, fa, tc = (pa + 1), fa, (tc + 1) if re else pa, (fa + 1), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("0"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("1.1"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("0.1"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("1.1e9"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("0.1e8"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("1110.1e-19"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("00001.1e-18"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("1.1e9"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("8"), False)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.istwoscomplement("Hello"), False)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.istwoscomplement(1975)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def adjusted(self):
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

    def _cmp(self, other):
        """Compare two objects.

        Compare the two non-NaN decimal instances self and other.
        Returns -1 if self < other, 0 if self == other and 1
        if self > other.  This routine is for internal use only.
        Returns integer.

        Parameters:
        other (str, Binary): object to compare to

        Returns:
        int: -1 s<o, 0 equal, 1 s>o
        """
        if not isinstance(other, Binary):
            other = Binary(other)

        # Compare(NaN, NaN) = NaN
        if self._is_special or other._is_special:
            self_inf = self.isinfinity()
            other_inf = other.isinfinity()
            if self_inf == other_inf:
                return 0
            elif self_inf < other_inf:
                return -1
            else:
                return 1

        if self._fraction == other._fraction:
            result = 0
        elif self._fraction < other._fraction:
            result = -1
        else:
            result = 1
        return result

        # TODO: this does string comparison, no longer needed
        # TODO: cleanup, save this code as string comparisons
        # TODO: Bug for 0b101e-18 0b0.000000000000000101 ?
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
        self_adjusted = self_se.adjusted()
        other_adjusted = other_se.adjusted()
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

    # Note: The Decimal standard doesn't cover rich comparisons for
    # Decimals.  In particular, the specification is silent on the
    # subject of what should happen for a comparison involving a NaN.
    # We take the following approach:
    #
    #   == comparisons involving a quiet NaN always return False
    #   != comparisons involving a quiet NaN always return True
    #   == or != comparisons involving a signaling NaN signal
    #      InvalidOperation, and return False or True as above if the
    #      InvalidOperation is not trapped.
    #   <, >, <= and >= comparisons involving a (quiet or signaling)
    #      NaN signal InvalidOperation, and return False if the
    #      InvalidOperation is not trapped.
    #
    # This behavior is designed to conform as closely as possible to
    # that specified by IEEE 754.

    def __eq__(self, other):
        """Implement ==. See _cmp() for details."""
        return self._cmp(other) == 0

    def test___eq__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary("-0.01e-2") == Binary("-1e-4"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("-0.01e-2") == "102"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("-0.01e-2") == complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def compare(self, other):
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

    def fraction_to_string(
        number: [int, float, Fraction], ndigits=_BINARY_PRECISION, strict=False
    ) -> str:
        """Convert number representation (int, float, or Fraction) to string.

        utility function

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
        return "".join(result) if strict else Binary.clean("".join(result))

    def test_fraction_to_string(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary.fraction_to_string(0), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(1), "1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(2), "10")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(13), "1101")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-0), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-1), "-1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-2), "-10")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-13), "-1101")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(0.0), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(1.0), "1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(2.0), "10")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(13.0), "1101")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-0.0), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-1.0), "-1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-2.0), "-10")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(-13.0), "-1101")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(0.0)), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(1.0)), "1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(2.0)), "10")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(13.0)), "1101")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(-0.0)), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(-1.0)), "-1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(-2.0)), "-10")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.fraction_to_string(Fraction(-13.0)), "-1101")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.fraction_to_string(Fraction(2 ** 100 + 2 ** 0)),
            "1" + "0" * 99 + "1",
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.fraction_to_string(Fraction(-(2 ** 100) - 2 ** 0)),
            "-1" + "0" * 99 + "1",
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.fraction_to_string(Fraction(2 ** 100 + 2 ** 0, 2 ** 101)),
            "0.1" + "0" * 99 + "1",
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.fraction_to_string(Fraction(2 ** 100 + 2 ** 0, -1 * 2 ** 101)),
            "-0.1" + "0" * 99 + "1",
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.fraction_to_string(
                Fraction(2 ** 1000 + 2 ** 0, -1 * 2 ** 1001), ndigits=10000
            ),
            "-0.1" + "0" * 999 + "1",
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.fraction_to_string(
                Fraction(2 ** 1000 + 2 ** 0, -1 * 2 ** 1001), ndigits=10
            ),
            "-0.1",
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.fraction_to_string(
                Fraction(2 ** 1000 + 2 ** 0, -1 * 2 ** 1001), ndigits=10, strict=True
            ),
            "-0.1" + "0" * 9,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.fraction_to_string(Binary(1))  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    # TODO:add member variable such as is_exact to indicate if lossless or not

    def string_to_fraction(value: str) -> Fraction:
        """Convert string representation to Fraction.

        utility function.

        Parameters:
        value (str): binary number in string representation

        Returns:
        Fraction: binary number in Fraction representation
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

    def test_string_to_fraction(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary.fraction_to_string(0), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("0"), Fraction(0))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("1"), Fraction(1))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("-0"), Fraction(0))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("-1"), Fraction(-1))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("11"), Fraction(3))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("-0.0"), Fraction(0))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("1.0"), Fraction(1))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("1.1"), Fraction(3, 2))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("-1.1"), Fraction(3, -2))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.string_to_fraction("-0.111"), Fraction(-0.875))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.string_to_fraction("1.1" + "0" * 2 + "1"),
            Fraction(3 * 2 ** 3 + 1, 2 ** 4),
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.string_to_fraction("1.1" + "0" * 100 + "1"),
            Fraction(3 * 2 ** 101 + 1, 2 ** 102),
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary.string_to_fraction("1.1" + "0" * 1000 + "1"),
            Fraction(3 * 2 ** 1001 + 1, 2 ** 1002),
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.string_to_fraction("102")  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.fraction_to_string(Binary(1))  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def invert(value: str, strict=True) -> str:
        """Inverts (bitwise negates) string that is in twos-complement format.

        This is a utility function.
        It negates (flips) every bit in the string.
        Input must be of format: twos-complement format.

        The twos-complement format is as follows.
            first bit: sign, 0 for +, 1 for -
            1 or more integer bits
            optional decimal point
            0 or more fractional bits
            optional exponent (e.g. e-12)

            [0,1][0,1]+.[0,1]*e[-][0-9]+
            sign (required)
                 integer bits (at least 1 bit required)
                       decimal point (optional, one or none)
                        fractional bits (optional, zero or more)
                            exponent (optional, possible with sign -)


        Examples inputs are:
            0...not valid, missing sign, or missing digits
            1...not valid, missing sign, or missing digits
            01...1, 010...2, 011...3
            10..-0, 111110..-0
            11...-1, 111...-1, 111111111...-1
            110...-2, 1110...-2,
            1101...-3, 111101...-3
            01.1...1.5, 010.11...2.75,
            111.1...-0.5, 111.11...-0.25
            01.1e-4...1.5e-4, 010.11e-4...2.75e-4,
            111.1e3...-0.5e3, 111.11e3...-0.25e3

            invert('0') raises exception
            invert('1') raises exception
            invert('1..1') raises exception
            invert('34') raises exception
            invert('1ee2') raises exception
            invert('1e') raises exception
            invert('01') returns '10'
            invert('10') returns '01'
            invert('101010') returns '010101'
            invert('0101010') returns '1010101'
            invert('0101010e-34') returns '1010101e-34'
            invert('101010e34') returns '0101010e34'
            invert(invert('0101010e-34')) returns '0101010e-34'
            invert(invert('101010e34')) returns '101010e34'

            invert(invert(n)) == for all valid n

        Returns:
        str: bitwise negated string, a twos-complement formated string
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")

        result = ""
        intpart = ""
        fracpart = ""
        for i in value:
            try:
                if int(i):
                    result += "0"
                else:
                    result += "1"
            except ValueError:
                intpart = result
                result = ""
        if len(intpart) > 0:
            fracpart = result
        else:
            intpart = result
            fracpart = "0"

        if not strict:
            leader = intpart[0]
            intpart = (
                leader + intpart.lstrip(leader)
                if int(intpart) != int(leader)  # TODO: strange code, why no then part?
                else leader
            )
            fracpart = fracpart.rstrip("0") if int(fracpart) != 0 else "0"
        # TODO: next if looks wrong: are you respecting strict in this if?
        if int(fracpart) == 0:
            result = intpart
        else:
            result = intpart + "." + fracpart
        # TODO: do you handle exp part?
        return result

    def test_invert(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary.invert("0001000"), "1110111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.invert("0001000", strict=False), "10111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.invert("1110110", strict=False), "01001")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.invert("0.1101", strict=True), "1.0010")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.invert("0.1101", strict=False), "1.001")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.invert("11.1101", strict=False), "0.001")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.invert("00.1101", strict=False), "1.001")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.invert(1975)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    # TODO: fill=1  ??? bool?
    def to_twos_complement(self, fill=1) -> str:
        """Computes the representation as a string in twos-complement.

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
        None

        Returns:
        str: binary string representation in twos-complement
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self._fraction >= 0:
            # TODO, BUG: we changed our mind, now '0' is a valid binary fraction
            # TODO: BUG: as well as a valid twos-complement representation
            # TODO, BUG: in short '0' or int 0 should return twos-complement '0'
            return "0" + self._value

        if _EXP in self._value:
            return "0" + self._value

        sign, intpart, fracpart, exp = self.components()
        intpart = abs(int(intpart, 2))
        intpart = bin(intpart)[2:]
        intpart = Binary.invert(intpart)
        new_intpart = bin(
            int(intpart.lstrip("0") if len(intpart) > 1 else intpart, 2) + 1
        )[2:]
        intpart = (len(intpart) - len(new_intpart)) * "0" + new_intpart
        intpart = (fill - len(intpart)) * "1" + intpart

        if fracpart != "" and int(fracpart) != 0:
            fracpart = fracpart.rstrip("0")
            fracl = len(fracpart)
            fracpart = bin(2 ** fracl - int(fracpart, 2))[2:]
            fracpart = "." + (fracl - len(fracpart)) * "0" + fracpart
        else:
            fracpart = ""
        # TODO, BUG: we changed our mind, now 1 or 10 are valid twos-complement strings
        return "1" + intpart + fracpart

    def test_to_twos_complement(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary("10").to_twos_complement(), Binary("10"))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1010").to_twos_complement(), Binary("1010"))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-1").to_twos_complement(fill=12), "1" * 13)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary(-1975).to_twos_complement(fill=12), "1100001001001"
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-1.0").to_twos_complement(fill=12), "1" * 13)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-1.0010").to_twos_complement(), "11.111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-0.0010").to_twos_complement(), "110.111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-0.111").to_twos_complement(), "110.001")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-0.10").to_twos_complement(), "110.1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("11"), "-1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def from_twos_complement(value: str, strict=False) -> str:
        """The opposite of to_twos_complement() function:

        This is a utility function.

        Converts '1101' to '-11' (-3)
        convert '1101.1e-2' to '-11.1e-2'  (-3.5/4)
        strict True, leaves it as much as unchanged as possivle
        strict False simplifies representation

        input "value" is string.
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")

        sign, intpart, fracpart, exp = Binary.get_twoscomplement_components(
            value, strict=strict
        )
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

    def test_from_twos_complement(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary.from_twos_complement("11.111"), "-1.001")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("110.111"), "-10.001")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("110.001"), "-10.111")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("110"), "-10")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("00"), "0")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("01"), "1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("00.11"), "0.11")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.from_twos_complement("00.11111111111110"), "0.1111111111111"
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary.from_twos_complement("00.11e-5"), "0.11e-5")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.from_twos_complement("00.11111111111110"), "0.1111111111111"
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary.from_twos_complement("00.00", strict=True), "00.00"
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.from_twos_complement("102")  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.from_twos_complement(Binary(1))  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def compare_representation(self, other):
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

    def test_compare_representation(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(
            tc,
            Binary(10.10).compare_representation(
                "1010.0001100110011001100110011001100110011001100110011"
            ),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("10.111").compare_representation("10.111"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(5).compare_representation("101"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary(8.3).compare_representation(
                "1000.010011001100110011001100110011001100110011001101"
            ),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0.0).compare_representation("0"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(1.0).compare_representation("1"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(3.5).compare_representation("11.1"), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary(-13.75).compare_representation("-1101.11"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary(13.0 + 2 ** -10).compare_representation("1101.0000000001"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary(13.0 + 2 ** -20).compare_representation("1101.00000000000000000001"),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary(13.0 + 2 ** -30).compare_representation(
                "1101.000000000000000000000000000001"
            ),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            Binary(13.0 + 2 ** -40).compare_representation(
                "1101.0000000000000000000000000000000000000001"
            ),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary(13.0 + 2 ** -50).compare_representation("1101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary(13.0 + 2 ** -60).compare_representation("1101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
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
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.1").round(1).compare_representation("1.1"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.10").round(1).compare_representation("1.1"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.101").round(1).compare_representation("1.1"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.11").round(1).compare_representation("1.1"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.110").round(1).compare_representation("1.1"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.1101").round(1).compare_representation("10"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, Binary("1.1111").round(1).compare_representation("10"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.compare_representation(1, "1")  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __repr__(self):
        """Represent self."""
        return (
            f"{self.__class__.__name__}"
            + f"({self._value}, {self._sign}, {self._is_special})"
        )

    def no_prefix(value):
        """Remove prefix '0b' from string representation.

        A utility function.
        Return format is e.g. -101.101e-23.

        Parameters:
        value (str): string from where to remove prefix

        Returns:
        str: without prefix
        """
        return value.replace(_PREFIX, "")

    def np(self):  # no prefix
        """Return string representation with prefix '0b' removed.

        Method implements the string conversion without prefix.
        Return format is e.g. -101.101e-23.
        Note that there is no '0b' prefix.

        Parameters:
        none

        Returns:
        str: without prefix
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return str(self._value)

    def test_np(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(-3.5).np(), "-11.1")
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary.np("1")  # should fail, 1 arg too much
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __str__(self) -> str:
        """Stringify self.

        Method that implements the string conversion.
        Return format is e.g. -0b101.101e-23.
        Note the prefix of '0b'.

        Parameters:
        none

        Returns:
        str: string representation with prefix '0b'
        """
        if self._sign:
            return "-" + _PREFIX + self._value[1:]
        else:
            return _PREFIX + self._value

    def __add__(self, other):
        """Add operation.

        Method that implements the * operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        Binary: addittion of the two numbers
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return Binary(self._fraction + other._fraction)

    def test___add__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(1) + Binary("1"), 2)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(-1) + Binary("1"), 0)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0.5) + Binary(0.5), 1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-1.1") + Binary("0.1"), -1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("102") + "103"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) + complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __sub__(self, other):
        """Subtract operation.

        Method that implements the - operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        Binary: subtraction of the two numbers
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return Binary(self._fraction - other._fraction)

    def test___sub__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(
            tc, Binary(Fraction(1, 3)) - Binary(Fraction(2, 3)), Fraction(-1, 3)
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(1) - Binary(1), 0)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0) - Binary(1), -1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0.1) - Binary(0.2), -0.1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(1) - Binary(0.5), 0.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("102") - "103"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) - complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __mul__(self, other):
        """Multiply operation.

        Method that implements the * operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        Binary: multiplication of the two numbers
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return Binary(self._fraction * other._fraction)

    def test___mul__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(0) * Binary(1), 0)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(1) * Binary(1), 1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(100) * Binary(Fraction(1, 10)), 10)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("102") * "103"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) * complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __truediv__(self, other):
        """True division operation

        Method that implements the / operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        Binary: true division of the two numbers
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return Binary(self._fraction / other._fraction)

    def test___truediv__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(100) / Binary(Fraction(1, 10)), 1000)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0) / Binary(10), 0)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(1) / Binary(2), 0.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("102") / "103"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) / complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __floordiv__(self, other):
        """Floor division operation

        Method that implements the // operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        Binary: floor division of the two numbers
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return Binary(self._fraction // other._fraction)

    def test___floordiv__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(10) // Binary(3), 3)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(7) // Binary(2), 3)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(8) // Binary(3), 2)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("102") // "103"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) // complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __mod__(self, other):
        """Compute modular operation

        Method that implements module, i.e. it returns the integer remainder.
        Method that implements the % operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        Binary: modulation of the two numbers
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return Binary(self._fraction % other._fraction)

    def test___mod__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(5) % Binary(3), 2)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(7) % Binary(4), 3)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("111") % Binary("11"), 1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(5.0) % Binary(1.5), 0.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("-101.0") % Binary("-1.1"), -0.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("102") % "103"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) % complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __abs__(self):
        """Compute absolute value.

        Method that implements absolute value, i.e. the positive value.

        Parameters:
        self (Binary): binary number

        Returns:
        Binary: Absolute of the number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return Binary(abs(self._fraction))

    def test___abs__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, abs(Binary(5)), 5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, abs(Binary(-7)), 7)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, abs(Binary("111")), 7)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, abs(Binary(-1.5)), 1.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, abs(Binary("-101.1")), 5.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __ceil__(self):
        """Perform math ceiling operation.

        Method that implements ceiling. Method for "ceil".
        For example, '1.11' will return '10'.

        Parameters:
        self (Binary): binary number

        Returns:
        Binary: ceiling of the number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return Binary(math.ceil(self._fraction))

    def test___ceil__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, math.ceil(Binary(5)), math.ceil(5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.ceil(Binary(-7)), math.ceil(-7))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.ceil(Binary("111")), math.ceil(7))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.ceil(Binary(-1.5)), math.ceil(-1.5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.ceil(Binary("-101.1")), math.ceil(-5.5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __floor__(self):
        """Perform math floor operation.

        Method that implements floor.
        For example, '1.11' will return '1'.

        Parameters:
        self (Binary): binary number

        Returns:
        Binary: floor of the number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return Binary(math.floor(self._fraction))

    def test___floor__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, math.floor(Binary(5)), math.floor(5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.floor(Binary(-7)), math.floor(-7))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.floor(Binary("111")), math.floor(7))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.floor(Binary(-1.5)), math.floor(-1.5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, math.floor(Binary("-101.1")), math.floor(-5.5))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __lt__(self, other):
        """Less than operation.

        Method that implements "<" operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        bool: condition result
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return self._fraction < other._fraction

    def __gt__(self, other):
        """Greater than operation.

        Method that implements ">" operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        bool: condition result
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return self._fraction > other._fraction

    def __le__(self, other):
        """Less or equal operation.

        Method that implements "<=" operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        bool: condition result
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return self._fraction <= other._fraction

    def __ge__(self, other):
        """Greater or equal operation.

        Method that implements ">=" operand.

        Parameters:
        self (Binary): binary number
        other (Binary): binary number

        Returns:
        bool: condition result
        """
        if not isinstance(other, Binary) or not isinstance(self, Binary):
            raise TypeError(f"Argument {other} and {self} must be of type Binary.")
        return self._fraction >= other._fraction

    def __bool__(self):
        """Boolean transformation. Used for not operand.

        Method that implements boolian operation "not".

        Parameters:
        self (Binary): binary number

        Returns:
        bool: boolean transformation of the number
        """
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return bool(self._fraction)

    def __and__(self, other):
        """Return the bitwise and of self and other.

        Method that implements the & operand.

        For example, '11.1' ^ '10.1' will return '10.1'

        Parameters:
        self (Binary): number
        other (Binary): number

        Returns:
        Binary: bitwise and of the two numbers
        """
        return Binary.and_or(
            self, other, "and"
        )  # TODO , do you really need the and_or function?

    def test___and__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(1) & Binary(1), Binary(1))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0) & Binary(1), Binary(0))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1000") & Binary("0"), Binary(0))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1010") & Binary("10"), Binary("10"))
        try:
            Binary("102") & "103"  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) & complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __or__(self, other):
        """Return the bitwise or of self and other.

        Method that implements the | operand.

        For example, '11.1' ^ '10.1' will return '11.1'

        Parameters:
        self (Binary): number
        other (Binary): number

        Returns:
        Binary: bitwise or of the two numbers
        """
        return Binary._or(self, other)  # TODO

    def _or(self, other):
        return  # TODO

    def __xor__(self, other):
        """Return the bitwise or of self and other.

        Method that implements the ^ operand.

        For example, '11.1' ^ '10.1' will return '11.1'

        Parameters:
        self (Binary): number
        other (Binary): number

        Returns:
        Binary: bitwise exclusive or of the two numbers
        """
        return Binary.xor(self, other)  # TODO

    def __not__(self) -> bool:
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
        # for integers it is defined as -(x+1). So ~9 is -10.
        return not self._fraction

    def test___not__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, not Binary(9), False)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, not Binary(-10.5), False)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, not Binary(0), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, not Binary(0.0), True)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            not Binary(complex(1, 1))  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __invert__(self):
        """Return the 'bitwise not' of self.

        Method that implements the ~ operand.
        This is also called the 'invert' operand, or the 'bitwise not' operand.

        It is only defined for integers. If self is not an integer it
        will raise an exception. For integers ~ is defined as
        ~n = -(n+1). For example, ~9 will return -10. ~-10 will return 9.
        For more information, see also the invert() function.

        Parameters:
        self (Binary): number

        Returns:
        Binary: 'bitwise not' of integer number
        """
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
            # string. This avoids to computation of a number representation (float) of
            # an inverted (~) float.

            raise ValueError(
                f"Invalid literal for Binary: {self._value}. "
                "~ operand only allowed on integers or fractions. "
                "To perform ~ on Binary, convert it to two's complement string"
                "and then perform invert() on that string. In short, do this: "
                "Binary.invert(Binary.to_twos_complement(value))."
            )

    def test___invert__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, ~Binary(9), Binary(-10))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, ~Binary(-10), Binary(9))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, ~~Binary(-109), Binary(-109))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, ~~Binary(9), Binary(9))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            ~Binary("-10.5")  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            ~Binary(complex(1, 1))  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __rshift__(self, ndigits: int):
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
            raise ValueError(f"negative shift count")

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
            shifted = Binary.clean(shifted_intpart + shifted_fracpart)
        return Binary(shifted)

    def test___rshift__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(1) >> 1, 0.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(2) >> 3, 0.25)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0.25) >> 1, Fraction(1, 8))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1e1") >> 1, 1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") >> 2, 5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") >> 3, Fraction(5, 2 ** 1))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") >> 3, Binary(Fraction(5, 2 ** 1)))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") >> 4, Binary(Fraction(5, 2 ** 2)))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") >> 4, Binary("101e-2"))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") >> 20, Binary("101e-18"))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") >> 20, Binary(Fraction(5, 2 ** 18)))
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101e2") >> 20).compare_representation("101e-18"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101e2") >> 2).compare_representation("101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101e-2") >> 2).compare_representation("101e-4"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101e2") >> 20).compare_representation("101e-18"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101") >> 2).compare_representation("1.01"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            (Binary("101") >> 20).compare_representation("0." + "0" * 17 + "101"),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01e2") >> 0).compare_representation("101.01e2"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01e2") >> 1).compare_representation("101.01e1"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01e2") >> 20).compare_representation("101.01e-18"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01") >> 2).compare_representation("1.0101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01") >> 1).compare_representation("10.101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01") >> 3).compare_representation("0.10101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            (Binary("101.01") >> 20).compare_representation("0." + "0" * 17 + "10101"),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("10") >> -3  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) >> complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    def __lshift__(self, ndigits: int):
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
            raise ValueError(f"negative shift count")
        if "e" in self._value:
            sign, intpart, fracpart, exp = Binary.get_components(self._value)
            shifted = (
                sign * "-"
                + intpart
                + "."
                + (fracpart if len(fracpart) > 0 else "0")
                + "e"
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
            shifted = Binary.clean(shifted_intpart + shifted_fracpart)
        return Binary(shifted)

    def test___lshift__(tc: int) -> tuple:
        """Unit test a specific function or method.

        Parameters:
        tc (int): first test case id to be used

        Returns the next available, unused test case id.
        If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
        6 is the next available test case id (= last used testcase id + 1).

        Returns:
        tuple (int, int, int):
            (number of tests passed,number of tests failed,
            last used testcase id)
        """
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        re = Binary.testcase(tc, Binary(1) << 1, 2)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(2) << 3, 16)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0.25) << 1, 0.5)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary(0.125) << 3, 1)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("1e1") << 2, 8)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") << 2, 5 * 2 ** 4)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(tc, Binary("101e2") << 20, 5 * 2 ** 22)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101e-2") << 2).compare_representation("101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101e2") << 2).compare_representation("101e4"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101e2") << 20).compare_representation("101e22"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101") << 2).compare_representation("10100"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101") << 20).compare_representation("101" + "0" * 20), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01e2") << 2).compare_representation("101.01e4"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01e2") << 20).compare_representation("101.01e22"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01") << 2).compare_representation("10101"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01") << 1).compare_representation("1010.1"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc, (Binary("101.01") << 3).compare_representation("101010"), True
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        re = Binary.testcase(
            tc,
            (Binary("101.01") << 20).compare_representation("10101" + "0" * 18),
            True,
        )
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary("10") << -3  # should fail
        except ValueError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        try:
            Binary(1) << complex(1, 1)  # should fail
        except TypeError:
            txt = "Expected exception occurred"
            re = Binary.testcase(tc, txt, txt)
        else:
            txt = "Exception was expected, but it did not occur."
            re = Binary.testcase(tc, "No exception", txt)
        pa, fa, tc = ((pa + 1) if re else pa), (fa if re else (fa + 1)), (tc + 1)
        return (pa, fa, tc)

    # is this necessary? can't we just call the corresponding function from Fractions?
    # can't we just call binary operands on Fractions and not implement anything?
    def and_or(this, other, which):  # TODO is this function still used? Still needed?
        """Shifts number to the left n times # TODO

        This is a function, not a method.

        Parameters:
        self (Binary): number to be shifted  # TODO
        ndigits (int): numner times to be shifted # TODO

        Returns:
        Binary: shifted number # TODO
        """
        # TODO: make this work with negative numbers
        if not isinstance(this, Binary) or not isinstance(other, Binary):
            raise TypeError(
                f"Arguments {this} {other} must be of type Binary and Binary."
            )
        sign1, intpart1, fracpart1, exp1 = this.components()
        sign2, intpart2, fracpart2, exp2 = other.components()
        print("Fracpart: ", fracpart1, fracpart2)

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

        else:
            result = 0
        return Binary(Binary.clean(result))

    def __LINE__():
        try:
            raise ValueError("")
        except ValueError:
            return sys.exc_info()[2].tb_frame.f_back.f_back.f_lineno

    def __FUNCTION__():
        try:
            raise ValueError("")
        except ValueError:
            return sys.exc_info()[2].tb_frame.f_back.f_back.f_code.co_name

    def testcase(id, input, expected_result):
        """Test a single test case. Compares input to expected result.

        Parameters:
        id (str): name of test case
        input: result of testcase
        expected_result: expected result

        Returns:
        bool: True if test passes, False if test fails
        """
        print(f"Test case {id} ", end="")
        info = ""
        if input == expected_result:
            result = "passed ✅"
            ret = True
        else:
            result = f"in line {Binary.__LINE__()} failed ❌"
            info = (
                f" : unit test: {Binary.__FUNCTION__()}; "
                + f"output: {input}; expected: {expected_result}"
            )
            ret = False
        print(f"{result}{info}")
        return ret

    def selftest():
        """Perform self test by running various test cases.

        Parameters:
        none

        Returns:
        bool: True if all tests pass, False if any single test fails
        """
        tc = 1000  # tc ... test case
        pa = 0  # pa ... number of tests passed
        fa = 0  # fa ... number of tests failed
        tp = 0  # tp ... accumulative total of tests passed
        tf = 0  # tf ... accumulative total of tests failed

        pa, fa, tc = Binary.test___new__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_version(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_binary_string_to_fraction(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_fraction_to_string(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_string_to_fraction(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_np(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_fill(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___float__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___int__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_compare_representation(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_istwoscomplement(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_invert(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___invert__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___eq__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___not__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___add__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___sub__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___mul__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___truediv__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___floordiv__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___mod__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___abs__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___ceil__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___floor__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___rshift__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___lshift__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test___and__(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_to_sci_exponential(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_to_simple_exponential(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_to_twos_complement(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9
        pa, fa, tc = Binary.test_from_twos_complement(tc)
        tp, tf, tc = tp + pa, tf + fa, tc + 9

        if tf == 0:
            result = f"Self-Test: 😃 All {tp} test cases passed ✅"
            ret = True
        else:
            plural = "" if tp == 1 else "s"
            result = f"Self-Test: {tp} test case{plural} passed ✅"
            plural = "" if tf == 1 else "s"
            result += f"Self-Test: {tf} test case{plural} failed ❌"
            ret = False
        print(f"{result}")
        return ret


# Useful Constants (internal use only)

""" Reusable defaults """
_Infinity = Binary("Inf")
_NegativeInfinity = Binary("-Inf")
_NaN = Binary("NaN")
_Zero = Binary(0)
_One = Binary(1)
_NegativeOne = Binary(-1)

# End of class
