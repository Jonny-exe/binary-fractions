#!/usr/bin/python3


"""An implementation of a Binary class and module.

It allows one to represent integers or floats as binary strings.
E.g. the integer 5 will be represented as string '0b11'.
E.g. the float -3.75 will be represented as string '-0b11.11'.
Exponential representation is also possible:
'-0b0.01111e3' or '-0b11.1e1' or '-0b1110e-2' all represent float -3.75.
various operations and transformations are offered.

License: GPL v3 or later

File Format: linted/beautified by black

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
>>> b.normalize()
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
>>> b2._cmp(b3) # same value, returns equal
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

"""

# TODO: go to stackoverflow.com, search for "binary math", "binary fractions"
# and where there are matches add comment/entry to reference this module
# in PyPi

import math  # isclose()
import re

_BINARY_WARNED_ABOUT_FLOAT = False
_BINARY_RELATIVE_TOLERANCE = 1e-10
_PREFIX = "0b"
_EXP = "e"

# see implementation of class Decimal:
# https://github.com/python/cpython/blob/3.9/Lib/_pydecimal.py
# https://docs.python.org/3/library/decimal.html
# see implementation of class Fraction:
# https://github.com/python/cpython/blob/3.9/Lib/fractions.py
# https://docs.python.org/3/library/fractions.html
# https://github.com/bradley101/fraction/blob/master/fraction/Fraction.py


class Binary(str):
    """Floating point class for binary fractions and arithmetic."""

    def __new__(cls, value="0", simplify=True):
        """Contructor.

        Use __new__ and not __init__ because it is immutable.
        Allows string, float and integer as input for constructor.

        Parameters:
        value (int, float, str): value of number
        simplify (bool): if True try to simplify string representation
            if False, try to leave the string representation as much as is

        Returns:
        Binary: created immutable instance
        """
        ##### crud for parsing strings #############################################
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
                        # version A: this normalizes to remove comma
                        intpart = str(int(intpart + fracpart))
                        exppart = str(exp - len(fracpart))
                        self._value = sign + intpart + _EXP + exppart
                        # # version B: this leaves string as much as is
                        # if fracpart == "":
                        #    self._value = sign + intpart + _EXP + str(exp)
                        # else:
                        #    self._value = sign + intpart + "." + fracpart + _EXP + str(exp)
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
            # self._value = Binary.normalize(self._value) # not strictly needed
            return self

        # From an integer
        if isinstance(value, int):
            if value >= 0:
                self._sign = 0
                sign = ""
            else:
                self._sign = 1
                sign = "-"
            self._value = sign + bin(abs(value)).replace(_PREFIX, "")
            return self

        # From another Binary
        if isinstance(value, Binary):
            self._sign = value._sign
            self._value = value._value
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
            # self._value = Binary.normalize(self._value) # not strictly needed
            return self

        # from a float
        if isinstance(value, float):
            if not _BINARY_WARNED_ABOUT_FLOAT:
                _BINARY_WARNED_ABOUT_FLOAT = True
                print("Warning: mixing floats and Binary")
            # TODO
            # better: store it as fraction (use class fraction for that)
            # fraction class allows exact math operations
            if value < 0:
                self._sign = 1
            else:
                self._sign = 0
            self._value = Binary.from_float(value)
            return self

        # any oher types
        raise TypeError("Cannot convert %r to Binary" % value)

    def from_float(value, rel_tol=_BINARY_RELATIVE_TOLERANCE):
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

    def float(self):
        """Convert from Binary to float.

        method
        Binary --> float or integer

        Returns:
        float: number as float or integer
        """
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        result = Binary.to_float(value)
        return result  # float or integer

    def to_float(value):
        """Convert from Binary to float or integer.

        utility function
        Binary --> float or integer
        could also use inverse of method float.hex()

        Parameters:
        value (str): binary string representation of number

        Returns:
        float or integer: number as float or integer
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # print(f"not normalized is {value}")
        value = Binary.normalize(value)
        # print(f"normalized is {value}")
        l = value.split(".")
        intpart = l[0]
        result = int(intpart, 2)
        if result < 0:
            sign = -1
        else:
            sign = 1
        # print(f"int result is {result}")
        if len(l) == 1:
            fracpart = ""
            return result  ## an integer
        else:
            fracpart = l[1]

        # print(f"fracpart is {fracpart}")
        l = len(fracpart)
        for i in range(l):
            if fracpart[i] == "1":
                result += (2 ** -(i + 1)) * sign
        return result  # float

    def clean(value):
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
        else:
            result = value
        if result == "-0":
            result = "0"
        return result

    def normalize(value):
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
            l = value.split(_EXP)
            intfracpart = l[0]
            exp = int(l[1])

            l = intfracpart.split(".")
            intpart = l[0]
            if len(l) == 1:
                fracpart = ""
            else:
                fracpart = l[1]
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
                    intpart = intpart[:exp]
                    result = intpart + "." + fracpart
        result = Binary.clean(result)
        # print(f"after normalize {result}")
        return result

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
        value = Binary.normalize(value)
        l = value.split(".")
        intpart = l[0]
        if len(l) == 1:
            fracpart = ""
        else:
            fracpart = l[1]

        # print(f"fracpart is {fracpart}")
        if len(fracpart) <= ndigits:
            return value
        nplusonedigit = fracpart[ndigits]
        nplusonedigits = fracpart[ndigits:]
        # print(f"nplusonedigit and nplusonedigits is {nplusonedigit} and {nplusonedigits}")
        if (len(nplusonedigits.rstrip("0")) <= 1) or (nplusonedigit == "0"):
            # '' or '1'
            return intpart + "." + fracpart[0:ndigits]
            # round down from 0.10xxx1 to 0.11000 ==> 0.1
        else:
            # round up from 0.1xxxx1 to 0.111111 ==> 1.0
            digits = intpart + fracpart[0:ndigits]
            digits = bin(int(digits, 2) + 1)[2:]  # rounded up
            # print(f'digits is {digits}')
            l = len(digits)
            result = digits[: l - ndigits] + "." + digits[l - ndigits :]
            return Binary.clean(result)

    def fill(self, ndigits=0, strict=False):
        """Normalize and fill number to n digits after comma.

        method, see fill_to()

        Parameters:
        ndigits (int): number of digits after comma, precision
        strict (bool): cut off by rounding if input is too long,
            remove precision if True and necessary

        Returns:
        Binary: binary string representation of number
        """
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return Binary.fill_to(value, ndigits, strict)

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
        # print(f"value is {value} of type {type(value)}")
        # print(f"non norm. value is {value}")
        value = Binary.normalize(value)
        # print(f"norm. value is {value}")
        l = value.split(".")
        intpart = l[0]
        if len(l) == 1:
            fracpart = ""
        else:
            fracpart = l[1]

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

        method
        examples: '1.1' ==> '11e-1',  '-0.01e-2' ==> '-1e-4'
        result has no comma

        Parameters:
        none

        Returns:
        Binary: binary string representation of number
        """
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.clean(value)
        else:
            l = value.split(_EXP)
            intfracpart = Binary.clean(l[0])
            exp = int(l[1])

        l = intfracpart.split(".")
        intpart = l[0]
        if len(l) == 1:
            fracpart = ""
        else:
            fracpart = l[1]
        lenintpart = len(intpart)
        lenfracpart = len(fracpart)
        exp -= lenfracpart
        intpart += fracpart
        return Binary(intpart + _EXP + str(exp), False)

    def to_sci_exponential(self):
        """Convert to exp. representation with single binary digit before comma.

        method
        examples: '1.1' ==> '1.1e0',  '-0.01e-2' ==> '-1e-4', '1'
        result has only 1 digit before comma

        Parameters:
        none

        Returns:
        Binary: binary string representation of number
        """
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.clean(value)
        else:
            l = value.split(_EXP)
            intfracpart = Binary.clean(l[0])
            exp = int(l[1])

        l = intfracpart.split(".")
        intpart = l[0]
        if len(l) == 1:
            fracpart = ""
        else:
            fracpart = l[1]
        if self._sign:
            intpart = intpart[1:]
            sign = "-"
        else:
            sign = ""
        lenintpart = len(intpart)
        lenfracpart = len(fracpart)

        exp += lenintpart - 1
        fracpart = intpart[1:] + fracpart
        intpart = intpart[:1]
        if fracpart == "":
            result = sign + intpart + _EXP + str(exp)
        else:
            result = sign + intpart + "." + fracpart + _EXP + str(exp)
        return Binary(result, False)

    def __bool__(self):
        """Implement the 'not' operand, operation.

        Return True if self is nonzero; otherwise return False.
        NaNs and infinities are considered nonzero.
        For "not" operand.

        Parameters:
        none

        Returns:
        Binary: binary string representation of number
        """
        return self._is_special or Binary.normalize(self._value) != "0"

    def components(self):
        """Return sign, intpart (without sign), fracpart, exp.

        Example: -11.01e2 ==> (1, '11', '01', 2)

        Parameters:
        none

        Returns:
        list: list of sign, intpart (without sign), fracpart, exp
        """
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        if self._sign:
            value = value[1:]  # remove sign from intpart
        if _EXP not in value:
            exp = 0
            intfracpart = Binary.clean(value)
        else:
            l = value.split(_EXP)
            intfracpart = Binary.clean(l[0])
            exp = int(l[1])

        l = intfracpart.split(".")
        intpart = l[0]
        if len(l) == 1:
            fracpart = ""
        else:
            fracpart = l[1]
        return (self._sign, intpart, fracpart, exp)

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
                return -(-1) ** self._sign
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
        # compare representation to another Binary
        if isinstance(other, Binary):
            return str(self._value) == str(other._value)
        if isinstance(other, str):
            return str(self._value) == other
        else:
            return str(self._value) == str(other)

    def __repr__(self):
        """Represent self."""
        return f"{self.__class__.__name__}({self._value}, {self._sign}, {self._is_special})"

    def no_prefix(value):
        """Remove prefix '0b' from string representation.

        utility function
        Return format is e.g. -101.101e-23

        Parameters:
        value (str): string from where to remove prefix

        Returns:
        str: without prefix
        """
        return value.replace(_PREFIX, "")

    def np(self):  # no prefix
        """Return string representation with prefix '0b' removed.

        method
        Return format is e.g. -101.101e-23

        Parameters:
        none

        Returns:
        str: without prefix
        """
        return str(self._value)

    def __str__(self):
        """Stringify self.

        method
        Return format is e.g. -0b101.101e-23

        Parameters:
        none

        Returns:
        str: (with) prefix
        """
        if self._sign:
            return "-" + _PREFIX + self._value[1:]
        else:
            return _PREFIX + self._value

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
        if input == expected_result:
            result = " passed ✅"
            ret = True
        else:
            result = " failed ❌"
            ret = False
        print(f"{result}")
        return ret

    def selftest():
        """Perform self test by running various test cases.

        Parameters:
        none

        Returns:
        bool: True if all tests pass, False if any single test fails
        """
        tc = 1000
        r = True
        # type should be Binary, not string
        r &= Binary.testcase(tc, "Binary" in str(type(Binary(5))), True)
        tc += 1
        try:
            Binary("102")  # should fail
        except:
            r &= Binary.testcase(
                tc, "Expected exception occurred", "Expected exception occurred"
            )
        tc += 1
        r &= Binary.testcase(tc, Binary(-3.5), "-11.1")
        tc += 1
        r &= Binary.testcase(tc, Binary(-3.5), "-0b11.1")
        tc += 1
        r &= Binary.testcase(tc, Binary(-3.5).np(), "-11.1")
        tc += 1
        r &= Binary.testcase(tc, str(Binary(-3.5)), "-0b11.1")
        tc += 1
        r &= Binary.testcase(
            tc,
            Binary(10.10).compare_representation(
                "1010.000110011001100110011001100110011001"
            ),
            True,
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("10.111").compare_representation("10.111"), True
        )
        tc += 1
        r &= Binary.testcase(tc, Binary(5).compare_representation("101"), True)
        tc += 1
        r &= Binary.testcase(
            tc,
            Binary(8.3).compare_representation(
                "1000.0100110011001100110011001100110011"
            ),
            True,
        )
        tc += 1
        r &= Binary.testcase(tc, Binary(0.0).compare_representation("0"), True)
        tc += 1
        r &= Binary.testcase(tc, Binary(1.0).compare_representation("1"), True)
        tc += 1
        r &= Binary.testcase(tc, Binary(3.5).compare_representation("11.1"), True)
        tc += 1
        r &= Binary.testcase(
            tc, Binary(-13.75).compare_representation("-1101.11"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary(13.0 + 2 ** -10).compare_representation("1101.0000000001"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc,
            Binary(13.0 + 2 ** -20).compare_representation("1101.00000000000000000001"),
            True,
        )
        tc += 1
        r &= Binary.testcase(
            tc,
            Binary(13.0 + 2 ** -30).compare_representation(
                "1101.000000000000000000000000000001"
            ),
            True,
        )
        tc += 1
        r &= Binary.testcase(
            tc,
            Binary(13.0 + 2 ** -40).compare_representation(
                "1101.0000000000000000000000000000000000000001"
            ),
            True,
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary(13.0 + 2 ** -50).compare_representation("1101"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary(13.0 + 2 ** -60).compare_representation("1101"), True
        )
        tc += 1
        r &= Binary.testcase(
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
        tc += 10
        r &= Binary.testcase(
            tc, Binary("1.1").round(1).compare_representation("1.1"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("1.10").round(1).compare_representation("1.1"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("1.101").round(1).compare_representation("1.1"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("1.11").round(1).compare_representation("1.1"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("1.110").round(1).compare_representation("1.1"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("1.1101").round(1).compare_representation("10"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("1.1111").round(1).compare_representation("10"), True
        )
        tc += 10
        r &= Binary.testcase(tc, Binary("1.1111").fill(1), "1.1111")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.1111").fill(4), "1.1111")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.1111").fill(5), "1.11110")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.1111").fill(6), "1.111100")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.1111").fill(1, True), "10.0")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.1111").fill(4, True), "1.1111")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.1111").fill(5, True), "1.11110")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.1111").fill(6, True), "1.111100")
        tc += 1
        r &= Binary.testcase(tc, Binary("1.0011").fill(1, True), "1.0")
        tc += 1
        r &= Binary.testcase(
            tc, Binary((1, (1, 0, 1, 0), -2)).compare_representation("-1010e-2"), True
        )
        tc += 10
        r &= Binary.testcase(tc, Binary("-1").float(), -1.0)
        tc += 1
        r &= Binary.testcase(tc, Binary("-1.1").float(), -1.5)
        tc += 1
        r &= Binary.testcase(tc, Binary("1.001").float(), 1.125)
        tc += 1
        r &= Binary.testcase(tc, Binary((1, (1, 0, 1, 0), -2)).float(), -2.5)
        tc += 1
        r &= Binary.testcase(tc, Binary(-13.0 - 2 ** -10).float(), -13.0009765625)
        tc += 1
        r &= Binary.testcase(tc, Binary(13.0 + 2 ** -20).float(), 13.000000953674316)
        tc += 1
        r &= Binary.testcase(tc, Binary(13.0 + 2 ** -30).float(), 13.000000000931323)
        tc += 10
        r &= Binary.testcase(
            tc,
            Binary("1.1").to_simple_exponential().compare_representation("11e-1"),
            True,
        )
        tc += 1
        r &= Binary.testcase(
            tc,
            Binary("-0.01e-2").to_simple_exponential().compare_representation("-1e-4"),
            True,
        )
        tc += 1
        r &= Binary.testcase(
            tc, Binary("1.1").to_sci_exponential().compare_representation("1.1e0"), True
        )
        tc += 1
        r &= Binary.testcase(
            tc,
            Binary("-0.01e-2").to_sci_exponential().compare_representation("-1e-4"),
            True,
        )
        tc += 1
        if r:
            result = "Self-Test: 😃 All test cases passed ✅"
            ret = True
        else:
            result = "Self-Test: Some test case failed ❌"
            ret = False
        print(f"{result}")
        return ret


##### Useful Constants (internal use only) ################################

""" Reusable defaults """
_Infinity = Binary("Inf")
_NegativeInfinity = Binary("-Inf")
_NaN = Binary("NaN")
_Zero = Binary(0)
_One = Binary(1)
_NegativeOne = Binary(-1)

# End of class
