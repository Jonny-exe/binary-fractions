# Table of Contents

* [binary](#binary)
  * [Binary](#binary.Binary)
    * [\_\_new\_\_](#binary.Binary.__new__)
    * [from\_float](#binary.Binary.from_float)
    * [version](#binary.Binary.version)
    * [\_\_float\_\_](#binary.Binary.__float__)
    * [\_\_int\_\_](#binary.Binary.__int__)
    * [to\_float](#binary.Binary.to_float)
    * [clean](#binary.Binary.clean)
    * [to\_not\_exponential](#binary.Binary.to_not_exponential)
    * [binary\_string\_to\_fraction](#binary.Binary.binary_string_to_fraction)
    * [\_\_round\_\_](#binary.Binary.__round__)
    * [round](#binary.Binary.round)
    * [round\_to](#binary.Binary.round_to)
    * [fill](#binary.Binary.fill)
    * [fill\_to](#binary.Binary.fill_to)
    * [to\_simple\_exponential](#binary.Binary.to_simple_exponential)
    * [to\_sci\_exponential](#binary.Binary.to_sci_exponential)
    * [get\_components](#binary.Binary.get_components)
    * [components](#binary.Binary.components)
    * [isinfinity](#binary.Binary.isinfinity)
    * [adjusted](#binary.Binary.adjusted)
    * [\_\_eq\_\_](#binary.Binary.__eq__)
    * [compare](#binary.Binary.compare)
    * [fraction\_to\_string](#binary.Binary.fraction_to_string)
    * [string\_to\_fraction](#binary.Binary.string_to_fraction)
    * [compare\_representation](#binary.Binary.compare_representation)
    * [\_\_repr\_\_](#binary.Binary.__repr__)
    * [no\_prefix](#binary.Binary.no_prefix)
    * [np](#binary.Binary.np)
    * [\_\_str\_\_](#binary.Binary.__str__)
    * [\_\_add\_\_](#binary.Binary.__add__)
    * [\_\_sub\_\_](#binary.Binary.__sub__)
    * [\_\_mul\_\_](#binary.Binary.__mul__)
    * [\_\_truediv\_\_](#binary.Binary.__truediv__)
    * [\_\_floordiv\_\_](#binary.Binary.__floordiv__)
    * [\_\_mod\_\_](#binary.Binary.__mod__)
    * [\_\_abs\_\_](#binary.Binary.__abs__)
    * [\_\_ceil\_\_](#binary.Binary.__ceil__)
    * [\_\_floor\_\_](#binary.Binary.__floor__)
    * [\_\_lt\_\_](#binary.Binary.__lt__)
    * [\_\_gt\_\_](#binary.Binary.__gt__)
    * [\_\_le\_\_](#binary.Binary.__le__)
    * [\_\_ge\_\_](#binary.Binary.__ge__)
    * [\_\_bool\_\_](#binary.Binary.__bool__)
    * [\_\_rshift\_\_](#binary.Binary.__rshift__)
    * [\_\_lshift\_\_](#binary.Binary.__lshift__)
    * [testcase](#binary.Binary.testcase)
    * [selftest](#binary.Binary.selftest)

<a name="binary"></a>
# binary

# Floating-point Binary Fractions: Do math in base 2!

![logo](binary-fractions.svg)

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


If you are curious about floating point binary fractions, have a look at:
- https://en.wikipedia.org/wiki/Computer_number_format#Representing_fractions_in_binary
- https://www.electronics-tutorials.ws/binary/binary-fractions.html
- https://ryanstutorials.net/binary-tutorial/binary-floating-point.php
- https://planetcalc.com/862/

## License:
- GPL v3 or later

## Features:
- Python 3
- constructors for various types: int, float, Fraction, Binary, str
- supports many operators: +, -, *, /, //, %, **, not, ...
- supports many methods: lshift, rshift, <<, >>, round, floor, ceil, ...
- very high precision
- many operations are lossless, i.e. with no rounding errors or loss of precision
- supports very long binary fractions
- supports exponential representations
- well documented. Please read the documentation inside the source code
([binary.py](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/binary.py)).
Or look at the pydoc-generated documentation in
[README.md](https://github.com/Jonny-exe/binary-fractions/blob/master/binary_fractions/README.md).


## Sample usage, Example calls:


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

<a name="binary.Binary"></a>
## Binary Objects

```python
class Binary(object)
```

Floating point class for binary fractions and arithmetic.

<a name="binary.Binary.__new__"></a>
#### \_\_new\_\_

```python
 | __new__(cls, value: [int, float, str, Fraction] = "0", simplify: bool = True)
```

Constructor.

Use __new__ and not __init__ because it is immutable.
Allows string, float, integer, and Fraction as input for constructor.
If instance is contructed from a string, attention is paid to *not*
modify the string or to modify it as little as possible.
For example, if given '1e1' it will remain as '1e1', it will not change it
to '1'. Same with '1000', it will not change it to '1e4'. We try to keep then
string representation as close to the original as possible.

**Arguments**:

- `value` _int, float, str_ - value of number
- `simplify` _bool_ - if True try to simplify string representation
  if False, try to leave the string representation as much as is
  

**Returns**:

- `Binary` - created immutable instance

<a name="binary.Binary.from_float"></a>
#### from\_float

```python
 | from_float(value: float, rel_tol: float = _BINARY_RELATIVE_TOLERANCE)
```

Convert from float to Binary.

utility function
float --> Binary
could also use method float.hex()

**Arguments**:

- `value` _float_ - value of number
- `rel_tol` _float_ - relative tolerance to know when to stop converting
  relates to precision
  

**Returns**:

- `str` - string representation of Binary

<a name="binary.Binary.version"></a>
#### version

```python
 | version() -> str
```

Give version number.

Is a utility function.

**Returns**:

- `str` - version number as date in format "YYMMDD-HHMMSS", e.g. "20210622-103815"

<a name="binary.Binary.__float__"></a>
#### \_\_float\_\_

```python
 | __float__()
```

Convert from Binary to float.

method
Binary --> float or integer

**Returns**:

- `float` - number as float or integer

<a name="binary.Binary.__int__"></a>
#### \_\_int\_\_

```python
 | __int__()
```

Convert from Binary to int.

method
Binary --> float or integer

**Returns**:

- `float` - number as integer

<a name="binary.Binary.to_float"></a>
#### to\_float

```python
 | to_float(value: str)
```

Convert from Binary string to float or integer.

utility function
Binary string --> float or integer
could also use inverse of method float.hex()

**Arguments**:

- `value` _str_ - binary string representation of number
  

**Returns**:

  float or integer: number as float or integer

<a name="binary.Binary.clean"></a>
#### clean

```python
 | clean(value: str) -> str
```

Clean up string representation.

utility function
Example: convert '11.0' to '11'

**Arguments**:

- `value` _str_ - binary string representation of number
  

**Returns**:

- `str` - binary string representation of number

<a name="binary.Binary.to_not_exponential"></a>
#### to\_not\_exponential

```python
 | to_not_exponential(value: str) -> str
```

Normalize string representation. Remove exponent part.

utility function
remove exponent, fully "decimal"
Example: convert '11.01e-2' to '0.1101'

**Arguments**:

- `value` _str_ - binary string representation of number
  

**Returns**:

- `str` - binary string representation of number

<a name="binary.Binary.binary_string_to_fraction"></a>
#### binary\_string\_to\_fraction

```python
 | binary_string_to_fraction(value)
```

Convert string representation of binary to Fraction.

utility function

**Arguments**:

- `value` _str_ - binary number as string
  

**Returns**:

- `Fraction` - value as fraction

<a name="binary.Binary.__round__"></a>
#### \_\_round\_\_

```python
 | __round__()
```

Normalize and round number to n digits after comma.

method, see round_to()

**Arguments**:

- `ndigits` _int_ - number of digits after comma, precision
  

**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.round"></a>
#### round

```python
 | round(ndigits=0)
```

Normalize and round number to n digits after comma.

method, see round_to()

**Arguments**:

- `ndigits` _int_ - number of digits after comma, precision
  

**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.round_to"></a>
#### round\_to

```python
 | round_to(value, ndigits=0)
```

Normalize and round number to n digits after comma.

utility function
Example: convert '11.01e-2' to '0.11' with ndigits==2
convert '0.1' to '0' with ndigits==0
convert '0.10000001' to '1' with ndigits==0

**Arguments**:

- `value` _str_ - binary string representation of number
- `ndigits` _int_ - number of digits after comma, precision
  

**Returns**:

- `str` - binary string representation of number

<a name="binary.Binary.fill"></a>
#### fill

```python
 | fill(ndigits=0, strict=False)
```

Normalize and fill number to n digits after comma.

method, see fill_to()

**Arguments**:

- `ndigits` _int_ - number of digits after comma, precision
- `strict` _bool_ - cut off by rounding if input is too long,
  remove precision if True and necessary
  

**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.fill_to"></a>
#### fill\_to

```python
 | fill_to(value, ndigits=0, strict=False)
```

Normalize and fill number to n digits after comma.

utility function
strict==False: if value is longer, don't touch, don't shorten
strict==True: if value is longer, then shorten, strictly ndigits

**Arguments**:

- `ndigits` _int_ - number of digits after comma, precision
- `strict` _bool_ - cut off by rounding if input is too long,
  remove precision if True and necessary
  

**Returns**:

- `str` - binary string representation of number

<a name="binary.Binary.to_simple_exponential"></a>
#### to\_simple\_exponential

```python
 | to_simple_exponential()
```

Convert to exponential representation without fraction.

method
examples: '1.1' ==> '11e-1',  '-0.01e-2' ==> '-1e-4'
result has no comma

**Arguments**:

  none
  

**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.to_sci_exponential"></a>
#### to\_sci\_exponential

```python
 | to_sci_exponential()
```

Convert to exp. representation with single binary digit before comma.

method
examples: '1.1' ==> '1.1e0',  '-0.01e-2' ==> '-1e-4', '1'
result has only 1 digit before comma

**Arguments**:

  none
  

**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.get_components"></a>
#### get\_components

```python
 | get_components(value)
```

Return sign, intpart (without sign), fracpart, exp.

Example: -11.01e2 ==> (1, '11', '01', 2)

**Arguments**:

- `value` _str_ - respresentation of a binary
  

**Returns**:

- `tuple` - tuple of sign, intpart (without sign), fracpart, exp

<a name="binary.Binary.components"></a>
#### components

```python
 | components()
```

Return sign, intpart (without sign), fracpart, exp.

Example: -11.01e2 ==> (1, '11', '01', 2)
intpart does not have a sign

**Arguments**:

  none
  

**Returns**:

- `tuple` - tuple of sign, intpart (without sign), fracpart, exp

<a name="binary.Binary.isinfinity"></a>
#### isinfinity

```python
 | isinfinity()
```

Determine if object is Infinity.

**Arguments**:

  none
  

**Returns**:

- `bool` - is or is not any kind of infinity or negative infinity

<a name="binary.Binary.adjusted"></a>
#### adjusted

```python
 | adjusted()
```

Return the adjusted exponent of self.

**Arguments**:

  none
  

**Returns**:

- `int` - adjusted exponent

<a name="binary.Binary.__eq__"></a>
#### \_\_eq\_\_

```python
 | __eq__(other)
```

Implement ==. See _cmp() for details.

<a name="binary.Binary.compare"></a>
#### compare

```python
 | compare(other)
```

Compare self to other. Return a Binary value.

a or b is a NaN ==> Binary('NaN')
a < b           ==> Binary('-1')
a == b          ==> Binary('0')
a > b           ==> Binary('1')

**Arguments**:

- `other` _str, Binary_ - object to compare to
  

**Returns**:

- `Binary` - -1 s<o, 0 equal, 1 s>o

<a name="binary.Binary.fraction_to_string"></a>
#### fraction\_to\_string

```python
 | fraction_to_string(number: [int, float, Fraction], ndigits=_BINARY_PRECISION, strict=False) -> str
```

Convert number representation (int, float, or Fraction) to string.

utility function

**Arguments**:

- `number` _int,float,Fraction_ - binary number in number representation
- `strict` _bool_ - cut off by rounding if input is too long,
  remove precision if True and necessary
  

**Returns**:

- `str` - binary number in string representation

<a name="binary.Binary.string_to_fraction"></a>
#### string\_to\_fraction

```python
 | string_to_fraction(value: str) -> Fraction
```

Convert string representation to Fraction.

utility function.

**Arguments**:

- `value` _str_ - binary number in string representation
  

**Returns**:

- `Fraction` - binary number in Fraction representation

<a name="binary.Binary.compare_representation"></a>
#### compare\_representation

```python
 | compare_representation(other)
```

Compare representation of self to representation of other string.

Does NOT compare values! '1.1' does NOT equal to '11e-1' !
Only '11e-1' equals to '11e-1' !
Returns integer.

**Arguments**:

- `other` _str, Binary_ - object to compare to
  

**Returns**:

- `int` - -1 s<o, 0 equal, 1 s>o

<a name="binary.Binary.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__()
```

Represent self.

<a name="binary.Binary.no_prefix"></a>
#### no\_prefix

```python
 | no_prefix(value)
```

Remove prefix '0b' from string representation.

utility function
Return format is e.g. -101.101e-23

**Arguments**:

- `value` _str_ - string from where to remove prefix
  

**Returns**:

- `str` - without prefix

<a name="binary.Binary.np"></a>
#### np

```python
 | np()
```

Return string representation with prefix '0b' removed.

method
Return format is e.g. -101.101e-23

**Arguments**:

  none
  

**Returns**:

- `str` - without prefix

<a name="binary.Binary.__str__"></a>
#### \_\_str\_\_

```python
 | __str__()
```

Stringify self.

method
Return format is e.g. -0b101.101e-23

**Arguments**:

  none
  

**Returns**:

- `str` - (with) prefix

<a name="binary.Binary.__add__"></a>
#### \_\_add\_\_

```python
 | __add__(other)
```

Add operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `Binary` - addittion of the two numbers

<a name="binary.Binary.__sub__"></a>
#### \_\_sub\_\_

```python
 | __sub__(other)
```

Subtract operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `Binary` - subtraction of the two numbers

<a name="binary.Binary.__mul__"></a>
#### \_\_mul\_\_

```python
 | __mul__(other)
```

Multiply operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `Binary` - multiplication of the two numbers

<a name="binary.Binary.__truediv__"></a>
#### \_\_truediv\_\_

```python
 | __truediv__(other)
```

True division operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `Binary` - true division of the two numbers

<a name="binary.Binary.__floordiv__"></a>
#### \_\_floordiv\_\_

```python
 | __floordiv__(other)
```

Floor division operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `Binary` - floor division of the two numbers

<a name="binary.Binary.__mod__"></a>
#### \_\_mod\_\_

```python
 | __mod__(other)
```

modular operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `Binary` - modulation of the two numbers

<a name="binary.Binary.__abs__"></a>
#### \_\_abs\_\_

```python
 | __abs__()
```

Absolute

method

**Arguments**:

- `self` _Binary_ - binary number
  

**Returns**:

- `Binary` - Absolute of the number

<a name="binary.Binary.__ceil__"></a>
#### \_\_ceil\_\_

```python
 | __ceil__()
```

Math ceiling

method

**Arguments**:

- `self` _Binary_ - binary number
  

**Returns**:

- `Binary` - ceiling of the number

<a name="binary.Binary.__floor__"></a>
#### \_\_floor\_\_

```python
 | __floor__()
```

Math floor

method

**Arguments**:

- `self` _Binary_ - binary number
  

**Returns**:

- `Binary` - floor of the number

<a name="binary.Binary.__lt__"></a>
#### \_\_lt\_\_

```python
 | __lt__(other)
```

Less than operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `bool` - condition result

<a name="binary.Binary.__gt__"></a>
#### \_\_gt\_\_

```python
 | __gt__(other)
```

Greater than operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `bool` - condition result

<a name="binary.Binary.__le__"></a>
#### \_\_le\_\_

```python
 | __le__(other)
```

Less or equal operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `bool` - condition result

<a name="binary.Binary.__ge__"></a>
#### \_\_ge\_\_

```python
 | __ge__(other)
```

Greater or equal operation

method

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number
  

**Returns**:

- `bool` - condition result

<a name="binary.Binary.__bool__"></a>
#### \_\_bool\_\_

```python
 | __bool__()
```

Boolean transformation

method

**Arguments**:

- `self` _Binary_ - binary number
  

**Returns**:

- `bool` - boolean transformation of the number

<a name="binary.Binary.__rshift__"></a>
#### \_\_rshift\_\_

```python
 | __rshift__(ndigits: int)
```

Shifts number to the right n times

**Arguments**:

- `self` _Binary_ - number to be shifted
- `ndigits` _int_ - numner times to be shifted
  

**Returns**:

- `Binary` - shifted number

<a name="binary.Binary.__lshift__"></a>
#### \_\_lshift\_\_

```python
 | __lshift__(ndigits: int)
```

Shifts number to the left n times

**Arguments**:

- `self` _Binary_ - number to be shifted
- `ndigits` _int_ - numner times to be shifted
  

**Returns**:

- `Binary` - shifted number

<a name="binary.Binary.testcase"></a>
#### testcase

```python
 | testcase(id, input, expected_result)
```

Test a single test case. Compares input to expected result.

**Arguments**:

- `id` _str_ - name of test case
- `input` - result of testcase
- `expected_result` - expected result
  

**Returns**:

- `bool` - True if test passes, False if test fails

<a name="binary.Binary.selftest"></a>
#### selftest

```python
 | selftest()
```

Perform self test by running various test cases.

**Arguments**:

  none
  

**Returns**:

- `bool` - True if all tests pass, False if any single test fails

