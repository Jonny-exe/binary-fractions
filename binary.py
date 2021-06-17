#!/usr/bin/python3

import math
import sys

_BINARY_WARNED_ABOUT_FLOAT = False

# see implementation of class Decimal:
# https://github.com/python/cpython/blob/3.9/Lib/_pydecimal.py
# see implementation of class Fraction:
# https://github.com/python/cpython/blob/3.9/Lib/fractions.py

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

import re
_parser = re.compile(r"""        # A numeric string consists of:
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
""", re.VERBOSE | re.IGNORECASE).match


class Binary(str):

    def __new__(cls, value="0"):
        global _BINARY_WARNED_ABOUT_FLOAT
        self = super(Binary, cls).__new__(cls)
        # From a string
        # REs insist on real strings, so we can too.
        if isinstance(value, str):
            m = _parser(value.strip().replace("_", ""))
            if m is None:
                raise ValueError(f"Invalid literal for Binary: {value}.")

            if m.group('sign') == "-":
                sign = "-"
            else:
                sign = ""
            intpart = m.group('int')
            if intpart is not None:
                # finite number
                fracpart = m.group('frac') or ''
                fracpart = fracpart.rstrip('0')
                exp = int(m.group('exp') or '0')
                if exp != 0:
                    intpart = str(int(intpart+fracpart))
                    exppart = str(exp - len(fracpart))
                    self._value = sign+intpart+'e'+exppart
                else:
                    self._value = sign+intpart+'.'+fracpart
            else:
                diag = m.group('diag')
                if diag is not None:
                    # NaN
                    if m.group('signal'):
                        self._value = 'NaN'  # N
                    else:
                        self._value = 'NaN'  # n
                else:
                    # infinity
                    self._value = sign+'Infinity'  # F
            # self._value = Binary.normalize(self._value) # not strictly needed
            return self

        # From an integer
        if isinstance(value, int):
            if value >= 0:
                sign = ""
            else:
                sign = "-"
            self._value = sign+bin(abs(value)).replace("0b", "")
            return self

        # From another Binary
        if isinstance(value, Binary):
            self._value = value._value
            return self

        # tuple/list conversion (possibly from as_tuple())
        if isinstance(value, (list,tuple)):
            if len(value) != 3:
                raise ValueError('Invalid tuple size in creation of Decimal '
                                 'from list or tuple.  The list or tuple '
                                 'should have exactly three elements.')
            # process sign.  The isinstance test rejects floats
            if not (isinstance(value[0], int) and value[0] in (0,1)):
                raise ValueError("Invalid sign.  The first value in the tuple "
                                 "should be an integer; either 0 for a "
                                 "positive number or 1 for a negative number.")
            if value[0]:
                sign = "-"
            else:
                sign = ""
            if value[2] == 'F':
                # infinity: value[1] is ignored
                self._Value = 'Infinity'
            else:
                # process and validate the digits in value[1]
                digits = []
                for digit in value[1]:
                    if isinstance(digit, int) and 0 <= digit <= 1:
                        # skip leading zeros
                        if digits or digit != 0:
                            digits.append(digit)
                    else:
                        raise ValueError("The second value in the tuple must "
                                         "be composed of integers in the range "
                                         "0 through 1.")
                if value[2] in ('n', 'N'):
                    # NaN: digits form the diagnostic
                    self._value = 'NaN'
                elif isinstance(value[2], int):
                    # finite number: digits give the coefficient
                    integer = ''.join(map(str, digits or [0]))
                    self._value = sign + integer + 'e' + str(value[2])
                else:
                    raise ValueError("The third value in the tuple must "
                                     "be an integer, or one of the "
                                     "strings 'F', 'n', 'N'.")
            # self._value = Binary.normalize(self._value) # not strictly needed
            return self

        if isinstance(value, float):
            if not _BINARY_WARNED_ABOUT_FLOAT:
                 _BINARY_WARNED_ABOUT_FLOAT = True
                 print("Warning: mixing floats and Binary")
            # TODO
            # better: store it as fraction (use class fraction for that)
            # fraction class allows exact math operations
            self._value = Binary.from_float(value)
            return self

        raise TypeError("Cannot convert %r to Binary" % value)


    def from_float(value, rel_tol=1e-10):
        # float --> Binary
        # could also use method float.hex()
        if not isinstance(value, float):
            raise TypeError(f"Argument {value} must be of type float.")
        if value >= 0:
            sign = ""
        else:
            sign = "-"
        value=abs(value)
        integer=int(value)
        intpart = bin(integer).replace("0b", "")

        fracpart=""
        rest = 0.0
        i = 1
        fraction = value - integer
        while not (math.isclose(rest, fraction, rel_tol=rel_tol)):
            b = 2 ** -i
            if b + rest <= fraction:
                fracpart+="1"
                rest += b
            else:
                fracpart+="0"
            i += 1
        return Binary.clean(sign+intpart+"."+fracpart)


    def float(self):
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        result = Binary.to_float(value)
        return result # float


    def to_float(value):  # or integer
        # convert Binary --> float
        # could also use inverse of method float.hex()
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        value = Binary.normalize(value)
        l = value.split('.')
        intpart = l[0]
        result = int(intpart,2)
        if len(l) == 1:
            fracpart = ''
            return result ## an integer
        else:
            fracpart = l[1]

        # print(f"fracpart is {fracpart}")
        l = len(fracpart)
        for i in range(l):
            if fracpart[i] == "1":
                result += 2 ** -(i + 1)
        return result # float


    def clean(value):  # convert 11.0 to 11
        return value.rstrip('0').rstrip('.')


    def normalize(value):  # convert 11.01e-2 to 0.1101
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # print(f"before normalize {value}")
        if 'e' not in value:
            result = Binary.clean(value)
        else:
            l = value.split('e')
            intfracpart = l[0]
            expo = int(l[1])

            l = intfracpart.split('.')
            intpart = l[0]
            if len(l) == 1:
                fracpart = ''
            else:
                fracpart = l[1]
            lenintpart = len(intpart)
            lenfracpart = len(fracpart)

            if expo >= 0:
                if lenfracpart <= expo:
                    fracpart += "0"*(expo-lenfracpart)
                    result = intpart + fracpart
                else:
                    intpart += fracpart[:expo]
                    fracpart = fracpart[expo:]
                    result = intpart + '.' + fracpart
            else: # expo < 0
                if lenintpart <= abs(expo):
                    intpart = "0"*(abs(expo)-lenintpart) + intpart
                    result = '0.' + intpart + fracpart
                else:
                    fracpart = intpart[expo:] + fracpart
                    intpart = intpart[:expo]
                    result = intpart + '.' + fracpart
        result = Binary.clean(result)
        # print(f"after normalize {result}")
        return result


    def round(self, ndigits=0):
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        result = Binary.round_to(value, ndigits)
        return Binary(result)


    def round_to(value, ndigits=0):
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # print(f"value is {value} of type {type(value)}")
        value = Binary.normalize(value)
        l = value.split('.')
        intpart = l[0]
        if len(l) == 1:
            fracpart = ''
        else:
            fracpart = l[1]

        # print(f"fracpart is {fracpart}")
        if len(fracpart) <= ndigits:
            return value
        nplusonedigit=fracpart[ndigits]
        nplusonedigits=fracpart[ndigits:]
        # print(f"nplusonedigit and nplusonedigits is {nplusonedigit} and {nplusonedigits}")
        if (len(nplusonedigits.rstrip('0')) <= 1) or (nplusonedigit == '0'):
            # '' or '1'
            return intpart + '.' + fracpart[0:ndigits]
            # round down from 0.10xxx1 to 0.11000 ==> 0.1
        else:
            # round up from 0.1xxxx1 to 0.111111 ==> 1.0
            digits = intpart + fracpart[0:ndigits]
            digits = bin(int(digits,2)+1)[2:] # rounded up
            # print(f'digits is {digits}')
            l = len(digits)
            result = digits[:l-ndigits] + '.' + digits[l-ndigits:]
            return Binary.clean(result)


    def fill(self, ndigits=0, strict=False):
        value = self._value
        if not isinstance(self, Binary):
            raise TypeError(f"Argument {self} must be of type Binary.")
        return Binary.fill_to(value, ndigits, strict)


    def fill_to(value, ndigits=0, strict=False):
        # strict==False: if longer, don't touch, don't shorten
        # strict==True: if longer, then shorten, strictly ndigits
        # output is string in this case, not Binary!
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # print(f"value is {value} of type {type(value)}")
        value = Binary.normalize(value)
        l = value.split('.')
        intpart = l[0]
        if len(l) == 1:
            fracpart = ''
        else:
            fracpart = l[1]

        # print(f"fracpart is {fracpart}")
        if len(fracpart) == ndigits:
            return value
        elif len(fracpart) < ndigits:
            if fracpart == '':
                value += '.'
            return value + '0'*(ndigits-len(fracpart))
        elif not strict: # len(fracpart) > ndigits:
            return value
        else: # strict
            result = Binary.round_to(value, ndigits)
            # rounding can shorten it drastically, 0.1111 => 1
            return Binary.fill_to(result, ndigits, strict)


    def __repr__(self):
        """repr(self)"""
        return '%s(%s, %s)' % (self.__class__.__name__,self._value)


    def __str__(self):
        """str(self)"""
        return str(self._value)


    def selftest():
        """testing"""
        print(1, f"type is {type(Binary(5))}") ## should be Binary, not string
        try:
            print(2, Binary('102'))  # should fail
        except:
            print(3, f'Expected exception {sys.exc_info()[0]} occurred.')
        print(4, Binary(10.10))
        print(5, Binary('10.111'))
        print(6, Binary(5))
        print(7, Binary(8.3))
        print(8, Binary(0.0))
        print(9, Binary(1.0))
        print(10, Binary(3.5))
        print(11, Binary(-13.75))
        print(12, Binary(13.0 + 2 ** -10))
        print(13, Binary(13.0 + 2 ** -20))
        print(14, Binary(13.0 + 2 ** -30))
        print(15, Binary(13.0 + 2 ** -40))
        print(16, Binary(13.0 + 2 ** -50))
        print(17, Binary(13.0 + 2 ** -60))
        print(18, Binary(13.0 + 2 ** -10 + 2 ** -20 + 2 ** -30 + 2 ** -40 + 2 ** -50 + 2 ** -60 + 2 ** -70))
        print(21, Binary('1.1').round(1)) # 1.1
        print(22, Binary('1.10').round(1)) # 1.1
        print(23, Binary('1.101').round(1)) # 1.1
        print(24, Binary('1.11').round(1)) # 1.1
        print(25, Binary('1.110').round(1)) # 1.1
        print(26, Binary('1.1101').round(1)) # 10
        print(27, Binary('1.1111').round(1)) # 10
        print(28, Binary('1.1111').fill(1)) # 1.1111
        print(29, Binary('1.1111').fill(4)) # 1.1111
        print(110, Binary('1.1111').fill(5)) # 1.11110
        print(111, Binary('1.1111').fill(6)) # 1.111100
        print(112, Binary('1.1111').fill(1, True)) # 10.0
        print(113, Binary('1.1111').fill(4, True)) # 1.1111
        print(114, Binary('1.1111').fill(5, True)) # 1.11110
        print(115, Binary('1.1111').fill(6, True)) # 1.111100
        print(116, Binary('1.0011').fill(1, True)) # 1.0
        print(117, Binary((1, (1, 0, 1, 0 ), -2))) # -10.10
        print(118, Binary('-1').float()) # -1
        print(119, Binary('1.1').float()) # 1.5
        print(120, Binary('1.001').float()) # 1.125
        print(121, Binary((1, (1, 0, 1, 0 ), -2)).float()) # -3.5
        print(122, Binary(13.0 + 2 ** -10).float())
        print(123, Binary(13.0 + 2 ** -20).float())
        print(124, Binary(13.0 + 2 ** -30).float())
        return None

##### Useful Constants (internal use only) ################################

# Reusable defaults
_Infinity = Binary('Inf')
_NegativeInfinity = Binary('-Inf')
_NaN = Binary('NaN')
_Zero = Binary(0)
_One = Binary(1)
_NegativeOne = Binary(-1)

# this should be commented out once it is made a package
# TODO
Binary.selftest()

# End of class
