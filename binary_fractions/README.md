# Table of Contents

* [binary](#binary)
  * [Binary](#binary.Binary)
    * [\_\_new\_\_](#binary.Binary.__new__)
    * [test\_\_\_new\_\_](#binary.Binary.test___new__)
    * [version](#binary.Binary.version)
    * [test\_version](#binary.Binary.test_version)
    * [from\_float](#binary.Binary.from_float)
    * [test\_from\_float](#binary.Binary.test_from_float)
    * [to\_float](#binary.Binary.to_float)
    * [test\_to\_float](#binary.Binary.test_to_float)
    * [\_\_float\_\_](#binary.Binary.__float__)
    * [test\_\_\_float\_\_](#binary.Binary.test___float__)
    * [\_\_int\_\_](#binary.Binary.__int__)
    * [test\_\_\_int\_\_](#binary.Binary.test___int__)
    * [simplify](#binary.Binary.simplify)
    * [test\_simplify](#binary.Binary.test_simplify)
    * [to\_not\_exponential](#binary.Binary.to_not_exponential)
    * [test\_to\_not\_exponential](#binary.Binary.test_to_not_exponential)
    * [twos\_complement\_to\_not\_exponential](#binary.Binary.twos_complement_to_not_exponential)
    * [test\_twos\_complement\_to\_not\_exponential](#binary.Binary.test_twos_complement_to_not_exponential)
    * [binary\_string\_to\_fraction](#binary.Binary.binary_string_to_fraction)
    * [test\_binary\_string\_to\_fraction](#binary.Binary.test_binary_string_to_fraction)
    * [\_\_round\_\_](#binary.Binary.__round__)
    * [round](#binary.Binary.round)
    * [round\_to](#binary.Binary.round_to)
    * [fill](#binary.Binary.fill)
    * [test\_fill](#binary.Binary.test_fill)
    * [fill\_to](#binary.Binary.fill_to)
    * [to\_simple\_exponential](#binary.Binary.to_simple_exponential)
    * [test\_to\_simple\_exponential](#binary.Binary.test_to_simple_exponential)
    * [to\_sci\_exponential](#binary.Binary.to_sci_exponential)
    * [test\_to\_sci\_exponential](#binary.Binary.test_to_sci_exponential)
    * [get\_components](#binary.Binary.get_components)
    * [get\_twoscomplement\_components](#binary.Binary.get_twoscomplement_components)
    * [components](#binary.Binary.components)
    * [isinfinity](#binary.Binary.isinfinity)
    * [isnegativeinfinity](#binary.Binary.isnegativeinfinity)
    * [ispositiveinfinity](#binary.Binary.ispositiveinfinity)
    * [isnan](#binary.Binary.isnan)
    * [test\_isnan](#binary.Binary.test_isnan)
    * [isint](#binary.Binary.isint)
    * [istwoscomplement](#binary.Binary.istwoscomplement)
    * [test\_istwoscomplement](#binary.Binary.test_istwoscomplement)
    * [adjusted](#binary.Binary.adjusted)
    * [\_\_eq\_\_](#binary.Binary.__eq__)
    * [test\_\_\_eq\_\_](#binary.Binary.test___eq__)
    * [compare](#binary.Binary.compare)
    * [fraction\_to\_string](#binary.Binary.fraction_to_string)
    * [test\_fraction\_to\_string](#binary.Binary.test_fraction_to_string)
    * [fraction](#binary.Binary.fraction)
    * [string\_to\_fraction](#binary.Binary.string_to_fraction)
    * [test\_string\_to\_fraction](#binary.Binary.test_string_to_fraction)
    * [invert](#binary.Binary.invert)
    * [test\_invert](#binary.Binary.test_invert)
    * [to\_twos\_complement](#binary.Binary.to_twos_complement)
    * [test\_to\_twos\_complement](#binary.Binary.test_to_twos_complement)
    * [from\_twos\_complement](#binary.Binary.from_twos_complement)
    * [test\_from\_twos\_complement](#binary.Binary.test_from_twos_complement)
    * [compare\_representation](#binary.Binary.compare_representation)
    * [test\_compare\_representation](#binary.Binary.test_compare_representation)
    * [\_\_repr\_\_](#binary.Binary.__repr__)
    * [no\_prefix](#binary.Binary.no_prefix)
    * [np](#binary.Binary.np)
    * [test\_np](#binary.Binary.test_np)
    * [\_\_str\_\_](#binary.Binary.__str__)
    * [\_\_add\_\_](#binary.Binary.__add__)
    * [test\_\_\_add\_\_](#binary.Binary.test___add__)
    * [\_\_sub\_\_](#binary.Binary.__sub__)
    * [test\_\_\_sub\_\_](#binary.Binary.test___sub__)
    * [\_\_mul\_\_](#binary.Binary.__mul__)
    * [test\_\_\_mul\_\_](#binary.Binary.test___mul__)
    * [\_\_truediv\_\_](#binary.Binary.__truediv__)
    * [test\_\_\_truediv\_\_](#binary.Binary.test___truediv__)
    * [\_\_floordiv\_\_](#binary.Binary.__floordiv__)
    * [test\_\_\_floordiv\_\_](#binary.Binary.test___floordiv__)
    * [\_\_mod\_\_](#binary.Binary.__mod__)
    * [test\_\_\_mod\_\_](#binary.Binary.test___mod__)
    * [\_\_pow\_\_](#binary.Binary.__pow__)
    * [\_\_abs\_\_](#binary.Binary.__abs__)
    * [test\_\_\_abs\_\_](#binary.Binary.test___abs__)
    * [\_\_ceil\_\_](#binary.Binary.__ceil__)
    * [test\_\_\_ceil\_\_](#binary.Binary.test___ceil__)
    * [\_\_floor\_\_](#binary.Binary.__floor__)
    * [test\_\_\_floor\_\_](#binary.Binary.test___floor__)
    * [\_\_lt\_\_](#binary.Binary.__lt__)
    * [\_\_gt\_\_](#binary.Binary.__gt__)
    * [\_\_le\_\_](#binary.Binary.__le__)
    * [\_\_ge\_\_](#binary.Binary.__ge__)
    * [\_\_bool\_\_](#binary.Binary.__bool__)
    * [\_\_and\_\_](#binary.Binary.__and__)
    * [test\_\_\_and\_\_](#binary.Binary.test___and__)
    * [\_\_or\_\_](#binary.Binary.__or__)
    * [\_\_xor\_\_](#binary.Binary.__xor__)
    * [\_\_not\_\_](#binary.Binary.__not__)
    * [test\_\_\_not\_\_](#binary.Binary.test___not__)
    * [\_\_invert\_\_](#binary.Binary.__invert__)
    * [test\_\_\_invert\_\_](#binary.Binary.test___invert__)
    * [\_\_rshift\_\_](#binary.Binary.__rshift__)
    * [test\_\_\_rshift\_\_](#binary.Binary.test___rshift__)
    * [\_\_lshift\_\_](#binary.Binary.__lshift__)
    * [test\_\_\_lshift\_\_](#binary.Binary.test___lshift__)
    * [and\_or](#binary.Binary.and_or)
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
 | __new__(cls, value: [int, float, str, Fraction] = "0", simplify: bool = True, warn_on_float: bool = False)
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
- `warn_on_float` _bool_ - if True print a warning statement to stdout to
  warn about possible loss in precision in case of conversion from
  float to Binary.
  If False, print no warning to stdout.


**Returns**:

- `Binary` - created immutable instance

<a name="binary.Binary.test___new__"></a>
#### test\_\_\_new\_\_

```python
 | test___new__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.version"></a>
#### version

```python
 | version() -> str
```

Give version number.

Is a utility function.

**Returns**:

- `str` - version number as date in format "YYMMDD-HHMMSS", e.g. "20210622-103815"

<a name="binary.Binary.test_version"></a>
#### test\_version

```python
 | test_version(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.from_float"></a>
#### from\_float

```python
 | from_float(value: float, rel_tol: float = _BINARY_RELATIVE_TOLERANCE) -> str
```

Convert from float to Binary string of type string.

This is a utility function. It converts from
float to Binary (float --> Binary).

**Arguments**:

- `value` _float_ - value of number
- `rel_tol` _float_ - relative tolerance to know when to stop converting
  relates to precision


**Returns**:

- `str` - string representation of Binary string

<a name="binary.Binary.test_from_float"></a>
#### test\_from\_float

```python
 | test_from_float(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.to_float"></a>
#### to\_float

```python
 | to_float(value: str) -> [float, int]
```

Convert from Binary string to float or integer.

This is a utility function that converts
a Binary string to a float or integer
(Binary string --> float or integer).

**Arguments**:

- `value` _str_ - binary string representation of number


**Returns**:

  float or integer: number as float or integer

<a name="binary.Binary.test_to_float"></a>
#### test\_to\_float

```python
 | test_to_float(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__float__"></a>
#### \_\_float\_\_

```python
 | __float__() -> [float, int]
```

Convert from Binary to float.

This is a method that convert Binary to float (or if possible to
integer). (Binary --> float or integer)

**Returns**:

- `float` - number as float or integer

<a name="binary.Binary.test___float__"></a>
#### test\_\_\_float\_\_

```python
 | test___float__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

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

<a name="binary.Binary.test___int__"></a>
#### test\_\_\_int\_\_

```python
 | test___int__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.simplify"></a>
#### simplify

```python
 | simplify(value: str, add_prefix: bool = False) -> str
```

Simplify string representation.

This is a utility function.
Do NOT use it on Twos-complement strings!
This function does not validate the input string.
Input string is assumed to be a syntactically valid binary fraction string.
Invalid strings can lead to undefined results.
Example: converts '11.0' to '11' or '0011.0e-0' to '11'.

**Arguments**:

- `value` _str_ - binary string representation of number
- `add_prefix` _bool_ - if True add 0b prefix to returned output,
  if False then do not add prefix to returned output


**Returns**:

- `str` - simplified binary string representation of number

<a name="binary.Binary.test_simplify"></a>
#### test\_simplify

```python
 | test_simplify(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.to_not_exponential"></a>
#### to\_not\_exponential

```python
 | to_not_exponential(self_value, add_prefix: bool = False) -> str
```

Normalize string representation. Remove exponent part.

This is both a method as well as a utility function.
Do NOT use it on Twos-complement strings!
This function does not validate the input string.
Input string is assumed to be a syntactically valid binary fraction string.
Invalid strings can lead to undefined results.

It removes the exponent, and returns a fully "decimal" binary string.
Example: converts '11.01e-2' to '0.1101'

**Arguments**:

- `self_value` _Binary, str_ - a Binary instance or
  a binary string representation of number
  add_prefix (bool):
  if self_value is a string:
  if True add 0b prefix to returned output,
  if False then do not add prefix to returned output
  if self_value is a Binary instance:
  always forces to True, will always show prefix 0b


**Returns**:

- `str` - binary string representation of number

<a name="binary.Binary.test_to_not_exponential"></a>
#### test\_to\_not\_exponential

```python
 | test_to_not_exponential(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.twos_complement_to_not_exponential"></a>
#### twos\_complement\_to\_not\_exponential

```python
 | twos_complement_to_not_exponential(value: str) -> str
```

Remove exponent part from twos-complement string.

This is a utility function.
Do NOT use it on binary fractions strings!
This function does not validate the input string.
Input string is assumed to be a syntactically valid twos-complement string.
Invalid input strings can lead to undefined results.

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

**Arguments**:

- `value` _str_ - binary string representation of number


**Returns**:

- `str` - binary string representation of number

<a name="binary.Binary.test_twos_complement_to_not_exponential"></a>
#### test\_twos\_complement\_to\_not\_exponential

```python
 | test_twos_complement_to_not_exponential(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.binary_string_to_fraction"></a>
#### binary\_string\_to\_fraction

```python
 | binary_string_to_fraction(value: str) -> Fraction
```

Convert string representation of binary to Fraction.

utility function

**Arguments**:

- `value` _str_ - binary number as string


**Returns**:

- `Fraction` - value as fraction

<a name="binary.Binary.test_binary_string_to_fraction"></a>
#### test\_binary\_string\_to\_fraction

```python
 | test_binary_string_to_fraction(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

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

This is a method. See also function fill_to().

**Arguments**:

- `ndigits` _int_ - number of digits after comma, precision
- `strict` _bool_ - cut off by rounding if input is too long,
  remove precision if True and necessary


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.test_fill"></a>
#### test\_fill

```python
 | test_fill(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.fill_to"></a>
#### fill\_to

```python
 | fill_to(value, ndigits=0, strict=False)
```

Normalize and fill number to n digits after comma.

This is a utility function.
If strict==False then if value is longer, don't touch, don't shorten it.
If strict==True then if value is longer, then shorten to strictly ndigits.

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

A method athat changes the string representation of a number.
Examples: '1.1' ==> '11e-1',  '-0.01e-2' ==> '-1e-4'
The result has no decimal point.

**Arguments**:

  none


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.test_to_simple_exponential"></a>
#### test\_to\_simple\_exponential

```python
 | test_to_simple_exponential(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.to_sci_exponential"></a>
#### to\_sci\_exponential

```python
 | to_sci_exponential()
```

Convert to exp. representation with single binary digit before comma.

Method that changes string representation of number.
Examples are: '1.1' ==> '1.1e0',  '-0.01e-2' ==> '-1e-4', '1'
The result has only 1 digit before decimal point.

**Arguments**:

  none


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.test_to_sci_exponential"></a>
#### test\_to\_sci\_exponential

```python
 | test_to_sci_exponential(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.get_components"></a>
#### get\_components

```python
 | get_components(value: str) -> tuple
```

Return sign, intpart (without sign), fracpart, exp.

Example: -11.01e2 ==> (1, '11', '01', 2)

**Arguments**:

- `value` _str_ - respresentation of a binary


**Returns**:

- `tuple` - tuple of sign, intpart (without sign), fracpart, exp

<a name="binary.Binary.get_twoscomplement_components"></a>
#### get\_twoscomplement\_components

```python
 | get_twoscomplement_components(value, strict=False) -> tuple
```

Return sign, intpart (indicates sign in first bit), fracpart, exp.

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

**Arguments**:

- `value` _str_ - respresentation of a twos-complement string
- `strict` _bool_ - if False simplify output by removing unnecessary digits


**Returns**:

- `tuple` - tuple of sign, intpart, fracpart, exp

<a name="binary.Binary.components"></a>
#### components

```python
 | components() -> tuple
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

Determine if object is positive or negative Infinity.

**Arguments**:

  none


**Returns**:

- `bool` - is or is not any kind of infinity or negative infinity

<a name="binary.Binary.isnegativeinfinity"></a>
#### isnegativeinfinity

```python
 | isnegativeinfinity()
```

Determine if object is Negative Infinity.

**Arguments**:

  none


**Returns**:

- `bool` - is or is not negative infinity

<a name="binary.Binary.ispositiveinfinity"></a>
#### ispositiveinfinity

```python
 | ispositiveinfinity()
```

Determine if object is Positive Infinity.

**Arguments**:

  none


**Returns**:

- `bool` - is or is not positive infinity

<a name="binary.Binary.isnan"></a>
#### isnan

```python
 | isnan()
```

Determine if object is not-a-number (NaN).

**Arguments**:

  none


**Returns**:

- `bool` - is or is not a NaN (division by zero)

<a name="binary.Binary.test_isnan"></a>
#### test\_isnan

```python
 | test_isnan(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.isint"></a>
#### isint

```python
 | isint() -> bool
```

Determines if binary fraction is an integer.

This is a utility function.

**Returns**:

- `bool` - True if int, False otherwise (Fraction, float)

<a name="binary.Binary.istwoscomplement"></a>
#### istwoscomplement

```python
 | istwoscomplement(value: str)
```

Determine if string is a valid twos-complement syntax.

**Arguments**:

  none


**Returns**:

- `bool` - is or is not valid twos-complement

<a name="binary.Binary.test_istwoscomplement"></a>
#### test\_istwoscomplement

```python
 | test_istwoscomplement(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

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

<a name="binary.Binary.test___eq__"></a>
#### test\_\_\_eq\_\_

```python
 | test___eq__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

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

<a name="binary.Binary.test_fraction_to_string"></a>
#### test\_fraction\_to\_string

```python
 | test_fraction_to_string(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.fraction"></a>
#### fraction

```python
 | fraction() -> Fraction
```

Extract Fractional representation from Binary instance.

A method to get the Binary as a Fraction.

**Arguments**:

  None


**Returns**:

- `Fraction` - binary number in Fraction representation

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

<a name="binary.Binary.test_string_to_fraction"></a>
#### test\_string\_to\_fraction

```python
 | test_string_to_fraction(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.invert"></a>
#### invert

```python
 | invert(value: str, strict=True) -> str
```

Inverts (bitwise negates) string that is in twos-complement format.

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

**Returns**:

- `str` - bitwise negated string, a twos-complement formated string

<a name="binary.Binary.test_invert"></a>
#### test\_invert

```python
 | test_invert(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.to_twos_complement"></a>
#### to\_twos\_complement

```python
 | to_twos_complement(fill=1) -> str
```

Computes the representation as a string in twos-complement.

This is a method returning a string.

**Examples**:

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


**Arguments**:

  None


**Returns**:

- `str` - binary string representation in twos-complement

<a name="binary.Binary.test_to_twos_complement"></a>
#### test\_to\_twos\_complement

```python
 | test_to_twos_complement(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.from_twos_complement"></a>
#### from\_twos\_complement

```python
 | from_twos_complement(value: str, strict=False) -> str
```

The opposite of to_twos_complement() function:

This is a utility function.

Converts '1101' to '-11' (-3)
convert '1101.1e-2' to '-11.1e-2'  (-3.5/4)
strict True, leaves it as much as unchanged as possivle
strict False simplifies representation

input "value" is string.

<a name="binary.Binary.test_from_twos_complement"></a>
#### test\_from\_twos\_complement

```python
 | test_from_twos_complement(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

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

<a name="binary.Binary.test_compare_representation"></a>
#### test\_compare\_representation

```python
 | test_compare_representation(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

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

A utility function.
Return format is e.g. -101.101e-23.

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

Method implements the string conversion without prefix.
Return format is e.g. -101.101e-23.
Note that there is no '0b' prefix.

**Arguments**:

  none


**Returns**:

- `str` - without prefix

<a name="binary.Binary.test_np"></a>
#### test\_np

```python
 | test_np(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__str__"></a>
#### \_\_str\_\_

```python
 | __str__() -> str
```

Stringify self.

Method that implements the string conversion.
Return format is e.g. -0b101.101e-23.
Note the prefix of '0b'.

**Arguments**:

  none


**Returns**:

- `str` - string representation with prefix '0b'

<a name="binary.Binary.__add__"></a>
#### \_\_add\_\_

```python
 | __add__(other)
```

Add operation.

Method that implements the * operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number


**Returns**:

- `Binary` - addittion of the two numbers

<a name="binary.Binary.test___add__"></a>
#### test\_\_\_add\_\_

```python
 | test___add__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__sub__"></a>
#### \_\_sub\_\_

```python
 | __sub__(other)
```

Subtract operation.

Method that implements the - operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number


**Returns**:

- `Binary` - subtraction of the two numbers

<a name="binary.Binary.test___sub__"></a>
#### test\_\_\_sub\_\_

```python
 | test___sub__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__mul__"></a>
#### \_\_mul\_\_

```python
 | __mul__(other)
```

Multiply operation.

Method that implements the * operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number


**Returns**:

- `Binary` - multiplication of the two numbers

<a name="binary.Binary.test___mul__"></a>
#### test\_\_\_mul\_\_

```python
 | test___mul__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__truediv__"></a>
#### \_\_truediv\_\_

```python
 | __truediv__(other)
```

True division operation

Method that implements the / operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number


**Returns**:

- `Binary` - true division of the two numbers

<a name="binary.Binary.test___truediv__"></a>
#### test\_\_\_truediv\_\_

```python
 | test___truediv__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__floordiv__"></a>
#### \_\_floordiv\_\_

```python
 | __floordiv__(other)
```

Floor division operation

Method that implements the // operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number


**Returns**:

- `Binary` - floor division of the two numbers

<a name="binary.Binary.test___floordiv__"></a>
#### test\_\_\_floordiv\_\_

```python
 | test___floordiv__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__mod__"></a>
#### \_\_mod\_\_

```python
 | __mod__(other)
```

Compute modular operation

Method that implements module, i.e. it returns the integer remainder.
Method that implements the % operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number


**Returns**:

- `Binary` - modulation of the two numbers

<a name="binary.Binary.test___mod__"></a>
#### test\_\_\_mod\_\_

```python
 | test___mod__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__pow__"></a>
#### \_\_pow\_\_

```python
 | __pow__(other)
```

Powwer of operation.

Method that implements the ** operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Binary_ - binary number


**Returns**:

- `Binary` - powwer of the two numbers

<a name="binary.Binary.__abs__"></a>
#### \_\_abs\_\_

```python
 | __abs__()
```

Compute absolute value.

Method that implements absolute value, i.e. the positive value.

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `Binary` - Absolute of the number

<a name="binary.Binary.test___abs__"></a>
#### test\_\_\_abs\_\_

```python
 | test___abs__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__ceil__"></a>
#### \_\_ceil\_\_

```python
 | __ceil__()
```

Perform math ceiling operation.

Method that implements ceiling. Method for "ceil".
For example, '1.11' will return '10'.

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `Binary` - ceiling of the number

<a name="binary.Binary.test___ceil__"></a>
#### test\_\_\_ceil\_\_

```python
 | test___ceil__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__floor__"></a>
#### \_\_floor\_\_

```python
 | __floor__()
```

Perform math floor operation.

Method that implements floor.
For example, '1.11' will return '1'.

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `Binary` - floor of the number

<a name="binary.Binary.test___floor__"></a>
#### test\_\_\_floor\_\_

```python
 | test___floor__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__lt__"></a>
#### \_\_lt\_\_

```python
 | __lt__(other)
```

Less than operation.

Method that implements "<" operand.

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

Greater than operation.

Method that implements ">" operand.

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

Less or equal operation.

Method that implements "<=" operand.

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

Greater or equal operation.

Method that implements ">=" operand.

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

Boolean transformation. Used for not operand.

Method that implements boolian operation "not".

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `bool` - boolean transformation of the number

<a name="binary.Binary.__and__"></a>
#### \_\_and\_\_

```python
 | __and__(other)
```

Return the bitwise and of self and other.

Method that implements the & operand.

For example, '11.1' ^ '10.1' will return '10.1'

**Arguments**:

- `self` _Binary_ - number
- `other` _Binary_ - number


**Returns**:

- `Binary` - bitwise and of the two numbers

<a name="binary.Binary.test___and__"></a>
#### test\_\_\_and\_\_

```python
 | test___and__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__or__"></a>
#### \_\_or\_\_

```python
 | __or__(other)
```

Return the bitwise or of self and other.

Method that implements the | operand.

For example, '11.1' ^ '10.1' will return '11.1'

**Arguments**:

- `self` _Binary_ - number
- `other` _Binary_ - number


**Returns**:

- `Binary` - bitwise or of the two numbers

<a name="binary.Binary.__xor__"></a>
#### \_\_xor\_\_

```python
 | __xor__(other)
```

Return the bitwise or of self and other.

Method that implements the ^ operand.

For example, '11.1' ^ '10.1' will return '11.1'

**Arguments**:

- `self` _Binary_ - number
- `other` _Binary_ - number


**Returns**:

- `Binary` - bitwise exclusive or of the two numbers

<a name="binary.Binary.__not__"></a>
#### \_\_not\_\_

```python
 | __not__() -> bool
```

Return the 'boolean not' of self.

Method that implements the 'not' operand.
Do not confuse it with the 'bitwise not' operand ~.

If self is 0, then method returns True.
For all other values it returns False.

For example: not Binary(0) returns True.
For example: not Binary(3.5) returns False.

**Arguments**:

- `self` _Binary_ - number


**Returns**:

- `Binary` - 'boolean not' of number

<a name="binary.Binary.test___not__"></a>
#### test\_\_\_not\_\_

```python
 | test___not__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__invert__"></a>
#### \_\_invert\_\_

```python
 | __invert__()
```

Return the 'bitwise not' of self.

Method that implements the ~ operand.
This is also called the 'invert' operand, or the 'bitwise not' operand.

It is only defined for integers. If self is not an integer it
will raise an exception. For integers ~ is defined as
~n = -(n+1). For example, ~9 will return -10. ~-10 will return 9.
For more information, see also the invert() function.

**Arguments**:

- `self` _Binary_ - number


**Returns**:

- `Binary` - 'bitwise not' of integer number

<a name="binary.Binary.test___invert__"></a>
#### test\_\_\_invert\_\_

```python
 | test___invert__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__rshift__"></a>
#### \_\_rshift\_\_

```python
 | __rshift__(ndigits: int)
```

Shifts number n digits (bits) to the right.

Method that implementes >> operand.

As example, shifting right by 1, divides the number by 2.
The string representation will be changed as little as possible.
If the string representation is in exponential form it will remain in
exponential form. If the string representation is in non-exponential form,
it will remain in non-exponential form, i.e. only the decimal point will be
moved to the left.

**Arguments**:

- `self` _Binary_ - number to be shifted
- `ndigits` _int_ - number of digits to be shifted right


**Returns**:

- `Binary` - right shifted number

<a name="binary.Binary.test___rshift__"></a>
#### test\_\_\_rshift\_\_

```python
 | test___rshift__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.__lshift__"></a>
#### \_\_lshift\_\_

```python
 | __lshift__(ndigits: int)
```

Shifts number n digits (bits) to the left.

Method that implementes << operand.

As example, shifting left by 1, multiplies the number by 2.
The string representation will be changed as little as possible.
If the string representation is in exponential form it will remain in
exponential form. If the string representation is in non-exponential form,
it will remain in non-exponential form, i.e. only the decimal point will be
moved to the right.

**Arguments**:

- `self` _Binary_ - number to be shifted
- `ndigits` _int_ - number of digits to be shifted left


**Returns**:

- `Binary` - left shifted number

<a name="binary.Binary.test___lshift__"></a>
#### test\_\_\_lshift\_\_

```python
 | test___lshift__(tc: int) -> tuple
```

Unit test a specific function or method.

**Arguments**:

- `tc` _int_ - first test case id to be used

  Returns the next available, unused test case id.
  If input tc was 3 and test 3, 4 and 5, were done, then 6 will be returned.
  6 is the next available test case id (= last used testcase id + 1).


**Returns**:

  tuple (int, int, int):
  (number of tests passed,number of tests failed,
  last used testcase id)

<a name="binary.Binary.and_or"></a>
#### and\_or

```python
 | and_or(this, other, which)
```

Shifts number to the left n times # TODO

This is a function, not a method.

**Arguments**:

- `self` _Binary_ - number to be shifted  # TODO
- `ndigits` _int_ - numner times to be shifted # TODO


**Returns**:

- `Binary` - shifted number # TODO

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

