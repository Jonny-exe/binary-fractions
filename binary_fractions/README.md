# Table of Contents

* [binary](#binary)
  * [TwosComplement](#binary.TwosComplement)
    * [\_\_new\_\_](#binary.TwosComplement.__new__)
    * [istwoscomplement](#binary.TwosComplement.istwoscomplement)
    * [components](#binary.TwosComplement.components)
    * [simplify](#binary.TwosComplement.simplify)
    * [to\_fraction](#binary.TwosComplement.to_fraction)
    * [to\_float](#binary.TwosComplement.to_float)
    * [to\_no\_mantissa](#binary.TwosComplement.to_no_mantissa)
    * [to\_not\_exponential](#binary.TwosComplement.to_not_exponential)
    * [invert](#binary.TwosComplement.invert)
  * [Binary](#binary.Binary)
    * [\_\_new\_\_](#binary.Binary.__new__)
    * [to\_float](#binary.Binary.to_float)
    * [from\_float](#binary.Binary.from_float)
    * [to\_not\_exponential](#binary.Binary.to_not_exponential)
    * [to\_simple\_exponential](#binary.Binary.to_simple_exponential)
    * [to\_sci\_exponential](#binary.Binary.to_sci_exponential)
    * [to\_eng\_exponential](#binary.Binary.to_eng_exponential)
    * [to\_fraction](#binary.Binary.to_fraction)
    * [to\_fraction\_alternative\_implementation](#binary.Binary.to_fraction_alternative_implementation)
    * [to\_twoscomplement](#binary.Binary.to_twoscomplement)
    * [from\_twoscomplement](#binary.Binary.from_twoscomplement)
    * [\_\_float\_\_](#binary.Binary.__float__)
    * [\_\_int\_\_](#binary.Binary.__int__)
    * [\_\_str\_\_](#binary.Binary.__str__)
    * [compare\_representation](#binary.Binary.compare_representation)
    * [\_\_repr\_\_](#binary.Binary.__repr__)
    * [no\_prefix](#binary.Binary.no_prefix)
    * [np](#binary.Binary.np)
    * [version](#binary.Binary.version)
    * [simplify](#binary.Binary.simplify)
    * [\_\_round\_\_](#binary.Binary.__round__)
    * [round](#binary.Binary.round)
    * [round\_to](#binary.Binary.round_to)
    * [fill](#binary.Binary.fill)
    * [fill\_to](#binary.Binary.fill_to)
    * [get\_components](#binary.Binary.get_components)
    * [components](#binary.Binary.components)
    * [isinfinity](#binary.Binary.isinfinity)
    * [isnegativeinfinity](#binary.Binary.isnegativeinfinity)
    * [ispositiveinfinity](#binary.Binary.ispositiveinfinity)
    * [isnan](#binary.Binary.isnan)
    * [isint](#binary.Binary.isint)
    * [fraction](#binary.Binary.fraction)
    * [value](#binary.Binary.value)
    * [fraction\_to\_string](#binary.Binary.fraction_to_string)
    * [isclose](#binary.Binary.isclose)
    * [compare](#binary.Binary.compare)
    * [\_\_eq\_\_](#binary.Binary.__eq__)
    * [\_\_lt\_\_](#binary.Binary.__lt__)
    * [\_\_gt\_\_](#binary.Binary.__gt__)
    * [\_\_le\_\_](#binary.Binary.__le__)
    * [\_\_ge\_\_](#binary.Binary.__ge__)
    * [\_\_add\_\_](#binary.Binary.__add__)
    * [\_\_sub\_\_](#binary.Binary.__sub__)
    * [\_\_mul\_\_](#binary.Binary.__mul__)
    * [\_\_truediv\_\_](#binary.Binary.__truediv__)
    * [\_\_floordiv\_\_](#binary.Binary.__floordiv__)
    * [\_\_mod\_\_](#binary.Binary.__mod__)
    * [\_\_pow\_\_](#binary.Binary.__pow__)
    * [\_\_abs\_\_](#binary.Binary.__abs__)
    * [\_\_ceil\_\_](#binary.Binary.__ceil__)
    * [\_\_floor\_\_](#binary.Binary.__floor__)
    * [\_\_rshift\_\_](#binary.Binary.__rshift__)
    * [\_\_lshift\_\_](#binary.Binary.__lshift__)
    * [\_\_bool\_\_](#binary.Binary.__bool__)
    * [\_\_not\_\_](#binary.Binary.__not__)
    * [\_\_and\_\_](#binary.Binary.__and__)
    * [\_\_or\_\_](#binary.Binary.__or__)
    * [\_\_xor\_\_](#binary.Binary.__xor__)
    * [\_\_invert\_\_](#binary.Binary.__invert__)
  * [TestTwosComplement](#binary.TestTwosComplement)
    * [selftest](#binary.TestTwosComplement.selftest)
    * [test\_\_\_new\_\_](#binary.TestTwosComplement.test___new__)
    * [test\_\_int2twoscomp](#binary.TestTwosComplement.test__int2twoscomp)
    * [test\_\_frac2twoscomp](#binary.TestTwosComplement.test__frac2twoscomp)
    * [test\_\_float2twoscomp](#binary.TestTwosComplement.test__float2twoscomp)
    * [test\_\_fraction2twoscomp](#binary.TestTwosComplement.test__fraction2twoscomp)
    * [test\_\_str2twoscomp](#binary.TestTwosComplement.test__str2twoscomp)
    * [test\_istwoscomplement](#binary.TestTwosComplement.test_istwoscomplement)
    * [test\_components](#binary.TestTwosComplement.test_components)
    * [test\_simplify](#binary.TestTwosComplement.test_simplify)
    * [test\_to\_fraction](#binary.TestTwosComplement.test_to_fraction)
    * [test\_to\_float](#binary.TestTwosComplement.test_to_float)
    * [test\_to\_no\_mantissa](#binary.TestTwosComplement.test_to_no_mantissa)
    * [test\_to\_not\_exponential](#binary.TestTwosComplement.test_to_not_exponential)
    * [test\_invert](#binary.TestTwosComplement.test_invert)
  * [TestBinary](#binary.TestBinary)
    * [selftest](#binary.TestBinary.selftest)
    * [test\_\_\_new\_\_](#binary.TestBinary.test___new__)
    * [test\_version](#binary.TestBinary.test_version)
    * [test\_to\_float](#binary.TestBinary.test_to_float)
    * [test\_from\_float](#binary.TestBinary.test_from_float)
    * [test\_to\_not\_exponential](#binary.TestBinary.test_to_not_exponential)
    * [test\_\_\_float\_\_](#binary.TestBinary.test___float__)
    * [test\_\_\_int\_\_](#binary.TestBinary.test___int__)
    * [test\_\_\_str\_\_](#binary.TestBinary.test___str__)
    * [test\_compare\_representation](#binary.TestBinary.test_compare_representation)
    * [test\_no\_prefix](#binary.TestBinary.test_no_prefix)
    * [test\_np](#binary.TestBinary.test_np)
    * [test\_simplify](#binary.TestBinary.test_simplify)
    * [test\_to\_fraction](#binary.TestBinary.test_to_fraction)
    * [test\_\_\_round\_\_](#binary.TestBinary.test___round__)
    * [test\_round](#binary.TestBinary.test_round)
    * [test\_round\_to](#binary.TestBinary.test_round_to)
    * [test\_fill](#binary.TestBinary.test_fill)
    * [test\_fill\_to](#binary.TestBinary.test_fill_to)
    * [test\_to\_simple\_exponential](#binary.TestBinary.test_to_simple_exponential)
    * [test\_to\_sci\_exponential](#binary.TestBinary.test_to_sci_exponential)
    * [test\_to\_eng\_exponential](#binary.TestBinary.test_to_eng_exponential)
    * [test\_get\_components](#binary.TestBinary.test_get_components)
    * [test\_components](#binary.TestBinary.test_components)
    * [test\_isinfinity](#binary.TestBinary.test_isinfinity)
    * [test\_isnegativeinfinity](#binary.TestBinary.test_isnegativeinfinity)
    * [test\_ispositiveinfinity](#binary.TestBinary.test_ispositiveinfinity)
    * [test\_isnan](#binary.TestBinary.test_isnan)
    * [test\_isint](#binary.TestBinary.test_isint)
    * [test\_fraction](#binary.TestBinary.test_fraction)
    * [test\_value](#binary.TestBinary.test_value)
    * [test\_fraction\_to\_string](#binary.TestBinary.test_fraction_to_string)
    * [test\_isclose](#binary.TestBinary.test_isclose)
    * [test\_\_\_eq\_\_](#binary.TestBinary.test___eq__)
    * [test\_\_\_lt\_\_](#binary.TestBinary.test___lt__)
    * [test\_\_\_gt\_\_](#binary.TestBinary.test___gt__)
    * [test\_\_\_le\_\_](#binary.TestBinary.test___le__)
    * [test\_\_\_ge\_\_](#binary.TestBinary.test___ge__)
    * [test\_\_\_add\_\_](#binary.TestBinary.test___add__)
    * [test\_\_\_sub\_\_](#binary.TestBinary.test___sub__)
    * [test\_\_\_mul\_\_](#binary.TestBinary.test___mul__)
    * [test\_\_\_truediv\_\_](#binary.TestBinary.test___truediv__)
    * [test\_\_\_floordiv\_\_](#binary.TestBinary.test___floordiv__)
    * [test\_\_\_mod\_\_](#binary.TestBinary.test___mod__)
    * [test\_\_\_pow\_\_](#binary.TestBinary.test___pow__)
    * [test\_\_\_abs\_\_](#binary.TestBinary.test___abs__)
    * [test\_\_\_ceil\_\_](#binary.TestBinary.test___ceil__)
    * [test\_\_\_floor\_\_](#binary.TestBinary.test___floor__)
    * [test\_\_\_rshift\_\_](#binary.TestBinary.test___rshift__)
    * [test\_\_\_lshift\_\_](#binary.TestBinary.test___lshift__)
    * [test\_\_\_bool\_\_](#binary.TestBinary.test___bool__)
    * [test\_\_\_not\_\_](#binary.TestBinary.test___not__)
    * [test\_\_\_and\_\_](#binary.TestBinary.test___and__)
    * [test\_\_\_or\_\_](#binary.TestBinary.test___or__)
    * [test\_\_\_xor\_\_](#binary.TestBinary.test___xor__)
    * [test\_\_\_invert\_\_](#binary.TestBinary.test___invert__)
    * [test\_to\_twoscomplement](#binary.TestBinary.test_to_twoscomplement)
    * [test\_from\_twoscomplement](#binary.TestBinary.test_from_twoscomplement)

<a name="binary"></a>
# binary

__Floating-point Binary Fractions: Do math in base 2!__


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
print(f"ceil({bf1}) = {ceil(bf1)}, or Binary(ceil({bf1})) = {Binary(ceil(bf1))}")
print(f"floor({bf1}) = {floor(bf1)}, or Binary(ceil({bf1})) = {Binary(floor(bf1))}")
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
print(f"Binary('{bf3}').to_not_exponential() = {bf3.to_not_exponential()}")
print(f"Binary('{bf3}').to_simple_exponential() = {bf3.to_simple_exponential()}")
# scientific notation
print(f"Binary('{bf3}').to_sci_exponential() = {bf3.to_sci_exponential()}")
# engineering notation
print(f"Binary('{bf3}').to_eng_exponential() = {bf3.to_eng_exponential()}")
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
ceil(-0b1.01) = -1, or Binary(ceil(-0b1.01)) = -0b1
floor(-0b1.01) = -2, or Binary(ceil(-0b1.01)) = -0b10
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
Binary('0b10.1e-3').to_not_exponential() = 0b0.0101
Binary('0b10.1e-3').to_simple_exponential() = 0b101e-4
Binary('0b10.1e-3').to_sci_exponential() = 0b1.01e-2
Binary('0b10.1e-3').to_eng_exponential() = 0b101000000e-10
Binary('-0b1.01').to_twos_complement() = 10.11
Binary(TwosComplement('10.1')) = -1.1
Binary(TwosComplement('100001001000.1')) = -11110110111.1
Binary(TwosComplement(-1975.5)) = -11110110111.1
TwosComplement(-1975.5) = 100001001000.1
And there are more operands, more methods, more functions, ...
For more information read the documentation at:
https://raw.githubusercontent.com/Jonny-exe/binary-fractions
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

<a name="binary.TwosComplement"></a>
## TwosComplement Objects

```python
class TwosComplement(str)
```

Floating point class for representing twos-complement.

<a name="binary.TwosComplement.__new__"></a>
#### \_\_new\_\_

```python
 | __new__(cls, value: Union[int, float, Fraction, str] = 0, length: int = -1, rel_tol: float = _BINARY_RELATIVE_TOLERANCE, simplify: bool = True, warn_on_float: bool = False) -> TwosComplement
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
  float to TwosComplement.
  If False, print no warning to stdout.


**Returns**:

- `TwosComplement` - created immutable instance

<a name="binary.TwosComplement.istwoscomplement"></a>
#### istwoscomplement

```python
 | istwoscomplement(value: str) -> bool
```

Determine if string is a valid twos-complement syntax.

**Arguments**:

- `self` _str_ - string to check


**Returns**:

- `bool` - is or is not valid twos-complement

<a name="binary.TwosComplement.components"></a>
#### components

```python
 | components(self_value: Union[str, TwosComplement], strict: bool = False) -> tuple
```

Return sign, intpart (indicates sign in first bit), fracpart, exp.

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

**Arguments**:

- `self_value` _str_ - respresentation of a twos-complement string,
  string to extract components from
- `strict` _bool_ - if False simplify output by removing unnecessary digits
- `strict==False` - cleanup, remove unnecessary digits, do cleanup
- `strict==True` - produce exact twos-complement, no cleanup or simplifications


**Returns**:

- `tuple` - tuple of sign, intpart, fracpart, exp

<a name="binary.TwosComplement.simplify"></a>
#### simplify

```python
 | simplify(self_value: Union[str, TwosComplement]) -> Union[str, TwosComplement]
```

Simplifies twos-complement.

Remove duplicate 1s on left.
Remove duplicate 0s after decimal point.
Remove unnecessary exponent.

<a name="binary.TwosComplement.to_fraction"></a>
#### to\_fraction

```python
 | to_fraction(self_value: Union[str, TwosComplement]) -> Fraction
```

Converts twos-complement to Fraction.

This is a utility function as well as a method.

Do NOT use it on negative binary fractions strings!

<a name="binary.TwosComplement.to_float"></a>
#### to\_float

```python
 | to_float(self_value: Union[str, TwosComplement]) -> float
```

Converts twos-complement to float.

<a name="binary.TwosComplement.to_no_mantissa"></a>
#### to\_no\_mantissa

```python
 | to_no_mantissa(self_value: Union[str, TwosComplement], length: int = -1) -> Union[str, TwosComplement]
```

Adjust exponent such that there is no fractional part, no mantissa.

This is a utility function as well as a method.

<a name="binary.TwosComplement.to_not_exponential"></a>
#### to\_not\_exponential

```python
 | to_not_exponential(self_value: Union[str, TwosComplement], length: int = -1, strict: bool = False) -> Union[str, TwosComplement]
```

Remove exponent part from twos-complement string.

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

**Arguments**:

- `value` _str_ - binary string representation of number
- `length` _int_ - the length of the returned number.
  -1 is the minimum amount of digits required.
  0 and negatives numbers, except -1, are not allowed.
  Length includes the possible decimal point.
  Example of length 3 is: '1.1'


**Returns**:

- `str` - binary string representation of number

<a name="binary.TwosComplement.invert"></a>
#### invert

```python
 | invert(self_value: Union[str, TwosComplement], strict: bool = False) -> Union[str, TwosComplement]
```

Inverts (bitwise negates) string that is in twos-complement format.

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

**Arguments**:

- `value` _str_ - string representation of twos-complement
- `strict` _bool_ - if True try to change the string as little as
  possible in format
  if False, returned string will also be simplified
  by removing unnecessary digits.


**Returns**:

- `str` - bitwise negated string, a twos-complement formated string

<a name="binary.Binary"></a>
## Binary Objects

```python
class Binary(object)
```

Floating point class for binary fractions and arithmetic.

<a name="binary.Binary.__new__"></a>
#### \_\_new\_\_

```python
 | __new__(cls, value: Union[int, float, str, Fraction, TwosComplement] = "0", simplify: bool = True, warn_on_float: bool = False) -> Binary
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

<a name="binary.Binary.to_float"></a>
#### to\_float

```python
 | to_float(value: str) -> Union[float, int]
```

Convert from Binary string to float or integer.

This is a utility function that converts
a Binary string to a float or integer
(Binary string --> float or integer).

**Arguments**:

- `value` _str_ - binary string representation of number


**Returns**:

  float or integer: number as float or integer

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

<a name="binary.Binary.to_not_exponential"></a>
#### to\_not\_exponential

```python
 | to_not_exponential(self_value: Union[Binary, str], length: int = -1, strict: bool = False, add_prefix: bool = False) -> Union[Binary, str]
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

  Union[Binary, str]: binary string representation of number
  If self_value was of class Binary, it returns a Binary instance.
  If self_value was of class str, it returns a str instance.

<a name="binary.Binary.to_simple_exponential"></a>
#### to\_simple\_exponential

```python
 | to_simple_exponential() -> Binary
```

Convert to exponential representation without fraction.

A method that changes the string representation of a number
so that the resulting string has no decimal point.
Examples: '1.1' ==> '11e-1',  '-0.01e-2' ==> '-1e-4'

**Arguments**:

  none


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.to_sci_exponential"></a>
#### to\_sci\_exponential

```python
 | to_sci_exponential() -> Binary
```

Convert to exp. representation in scientific notation.

Scientific notation is an exponent representation with a single
binary digit before decimal point.

Method that changes string representation of number.
Examples are: '1.1' ==> '1.1e0',  '-0.01e-2' ==> '-1e-4', '1'
The result has only 1 digit before decimal point.

**Arguments**:

  none


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.to_eng_exponential"></a>
#### to\_eng\_exponential

```python
 | to_eng_exponential() -> Binary
```

Convert to exponential representation in engineering notation.

See https://www.purplemath.com/modules/exponent4.htm.
See https://www.thinkcalculator.com/numbers/decimal-to-engineering.php
See https://en.wikipedia.org/wiki/Engineering_notation.
See https://en.wikipedia.org/wiki/Engineering_notation#Binary_engineering_notation

Engineering notation is an exponent representation with the exponent
modulo 10 being 0, and where there are 1 through 9 digit before the
decimal point.
The integer part must not be 0 unless the number is 0.
The integer part is from 1 to 1023, or written in binary fraction
from 0b1 to 0b111111111.

Method that changes string representation of number.

Examples are:
'1.1' ==> '1.1'
'1.1111' ==> '1.1111'
'100.1111' ==> '100.1111'
'1.1111' ==> '1.1111'
'10.1111' ==> '10.1111'
'100.1111' ==> '100.1111'
'1000.1111' ==> '1000.1111'
1023 ==> '1111111111' => '1111111111'
1024 ==> '10000000000' => '1e10'
1025 ==> '10000000001' => '1.0000000001e10'
3072 ==> '110000000000' ==> 1.1e10
1024 ** 2 ==> '1000000000000000000000000000000' => '1e20'
'0.1' => '100000000e-10'
'0.11' => '110000000e-10'
'0.01' => '10000000e-10'
'0.0000000001' => '1e-10'
'0.000000001' => '10e-10'
'0.00000000111' => '11.1e-10'
'.11111e1' ==> '1.1111'
'.011111e2' ==> '1.1111'
'.0011111e3' ==> '1.1111'
'-0.01e-2' ==> '-1e-3' => '-1000000e-10'
'-0.0001e-4' == -0.00000001 ==> '-100e-10',
'-0.0001111e-4' == -0.00000001111 ==> '-111.1e-10',

**Arguments**:

  none


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.to_fraction"></a>
#### to\_fraction

```python
 | to_fraction(self_value: Union[str, Binary]) -> Fraction
```

Convert string representation of Binary to Fraction.

This is a utility function.

**Arguments**:

- `self_value` _str, Binary_ - binary number as string


**Returns**:

- `Fraction` - self_value as fraction

<a name="binary.Binary.to_fraction_alternative_implementation"></a>
#### to\_fraction\_alternative\_implementation

```python
 | to_fraction_alternative_implementation(value: str) -> Fraction
```

Convert string representation of Binary to Fraction.

This is a utility function.

**Arguments**:

- `value` _str_ - binary number as string


**Returns**:

- `Fraction` - value as fraction

<a name="binary.Binary.to_twoscomplement"></a>
#### to\_twoscomplement

```python
 | to_twoscomplement(length: int = -1) -> TwosComplement
```

Computes the representation as a string in twos-complement.

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

- `length` _int_ - this increases the length of the returned string
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


**Returns**:

- `str` - binary string representation in twos-complement

<a name="binary.Binary.from_twoscomplement"></a>
#### from\_twoscomplement

```python
 | from_twoscomplement(value: TwosComplement, strict: bool = False) -> str
```

The opposite of to_twoscomplement() function.

This is a utility function that converts from twos-complement format
to binary fraction format.

See to_twoscomplement() function description for more details
on twos-complement format.

Converts '1101' to '-11' (-3)
convert '1101.1e-2' to '-11.1e-2'  (-3.5/4)

**Arguments**:

- `value` _str_ - string in twos-complement format
  strict (bool):
  If strict is True, leaves it as much as unchanged as possible.
  If strict is False simplifies returned binary string representation.


**Returns**:

- `str` - string in binary fraction format

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

  None


**Returns**:

- `str` - string representation with prefix '0b'

<a name="binary.Binary.compare_representation"></a>
#### compare\_representation

```python
 | compare_representation(other: Union[str, Binary]) -> int
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
 | __repr__() -> str
```

Represent self.

<a name="binary.Binary.no_prefix"></a>
#### no\_prefix

```python
 | no_prefix(self_value: Union[str, Binary]) -> str
```

Remove prefix '0b' from string representation.

A method as well as a utility function.
Return format is e.g. -101.101e-23.

**Arguments**:

- `value` _str, Binary_ - string from where to remove prefix


**Returns**:

- `str` - without prefix

<a name="binary.Binary.np"></a>
#### np

```python
 | np(self_value: Union[str, Binary]) -> str
```

Remove prefix '0b' from string representation.

Same as no_prefix().

**Arguments**:

- `value` _str, Binary_ - string from where to remove prefix


**Returns**:

- `str` - without prefix

<a name="binary.Binary.version"></a>
#### version

```python
 | version() -> str
```

Give version number.

Is a utility function.

**Returns**:

- `str` - version number as date in format "YYMMDD-HHMMSS", e.g. "20210622-103815"

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

<a name="binary.Binary.__round__"></a>
#### \_\_round\_\_

```python
 | __round__(ndigits: int = 0) -> Binary
```

Normalize and round number to n digits after decimal point.

A method. Same as function round(). See also utility function round_to().

**Arguments**:

- `ndigits` _int_ - number of digits after decimal point, precision


**Returns**:

- `Binary` - binary string representation of number
  Other classes like Fractions have the simplicity of returning class int.
  The return class here must be Binary and it cannot be int because round()
  needs to be able to support ndigits (precision).

<a name="binary.Binary.round"></a>
#### round

```python
 | round(ndigits: int = 0) -> Binary
```

Normalize and round number to n digits after decimal point.

A method. Same as __round__() (round()). See also function round_to().

**Arguments**:

- `ndigits` _int_ - number of digits after decimal point, precision


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.round_to"></a>
#### round\_to

```python
 | round_to(value: str, ndigits: int = 0) -> str
```

Normalize and round number to n digits after decimal point.

This is a utility function.
Example: converts '11.01e-2' to '0.11' with ndigits==2.
Converts '0.1' to '0' with ndigits==0.
Converts '0.10000001' to '1' with ndigits==0.

**Arguments**:

- `value` _str_ - binary string representation of number
- `ndigits` _int_ - number of digits after decimal point, precision


**Returns**:

- `str` - binary string representation of number

<a name="binary.Binary.fill"></a>
#### fill

```python
 | fill(ndigits: int = 0, strict: bool = False)
```

Normalize and fill number to n digits after decimal point.

This is a method. See also function fill_to().

**Arguments**:

- `ndigits` _int_ - number of digits after decimal point, precision
- `strict` _bool_ - cut off by rounding if input is too long,
  remove precision if True and necessary


**Returns**:

- `Binary` - binary string representation of number

<a name="binary.Binary.fill_to"></a>
#### fill\_to

```python
 | fill_to(value: str, ndigits: int = 0, strict: bool = False) -> str
```

Normalize and fill number to n digits after decimal point.

This is a utility function.
If strict==False then if value is longer, don't touch, don't shorten it.
If strict==True then if value is longer, then shorten to strictly ndigits.

**Arguments**:

- `ndigits` _int_ - number of digits after decimal point, precision
- `strict` _bool_ - cut off by rounding if input is too long,
  remove precision if True and necessary


**Returns**:

- `str` - binary string representation of number

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
 | isinfinity() -> bool
```

Determine if object is positive or negative Infinity.

**Arguments**:

  none


**Returns**:

- `bool` - is or is not any kind of infinity or negative infinity

<a name="binary.Binary.isnegativeinfinity"></a>
#### isnegativeinfinity

```python
 | isnegativeinfinity() -> bool
```

Determine if object is Negative Infinity.

**Arguments**:

  none


**Returns**:

- `bool` - is or is not negative infinity

<a name="binary.Binary.ispositiveinfinity"></a>
#### ispositiveinfinity

```python
 | ispositiveinfinity() -> bool
```

Determine if object is Positive Infinity.

**Arguments**:

  none


**Returns**:

- `bool` - is or is not positive infinity

<a name="binary.Binary.isnan"></a>
#### isnan

```python
 | isnan() -> bool
```

Determine if object is not-a-number (NaN).

**Arguments**:

  none


**Returns**:

- `bool` - is or is not a NaN (division by zero)

<a name="binary.Binary.isint"></a>
#### isint

```python
 | isint() -> bool
```

Determines if binary fraction is an integer.

This is a utility function.

**Returns**:

- `bool` - True if int, False otherwise (Fraction, float)

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

<a name="binary.Binary.value"></a>
#### value

```python
 | value() -> str
```

Extract string representation from Binary instance.

A method to get the Binary as a Fraction.

**Arguments**:

  None


**Returns**:

- `Fraction` - binary number in string representation

<a name="binary.Binary.fraction_to_string"></a>
#### fraction\_to\_string

```python
 | fraction_to_string(number: Union[int, float, Fraction], ndigits: int = _BINARY_PRECISION, strict: bool = False) -> str
```

Convert number representation (int, float, or Fraction) to string.

This is a utility function.

**Arguments**:

- `number` _int,float,Fraction_ - binary number in number representation
- `strict` _bool_ - cut off by rounding if input is too long,
  remove precision if True and necessary


**Returns**:

- `str` - binary number in string representation

<a name="binary.Binary.isclose"></a>
#### isclose

```python
 | isclose(other: Any, rel_tol: float = _BINARY_RELATIVE_TOLERANCE) -> bool
```

Compare two objects to see if they are mathematically close.

This is a utility function. Useful for floats that have been converted
to binary fractions. A substitute for == for binary fractions
created from floats with precision errors.

**Arguments**:

- `other` _Any, int, float, Fraction, Binary_ - value of number
- `rel_tol` _float_ - relative tolerance as epsilon-value
  to decide if two numbers are close relative to each other


**Returns**:

- `bool` - True if two numbers are close, False otherwise

<a name="binary.Binary.compare"></a>
#### compare

```python
 | compare(other: Any) -> Binary
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

<a name="binary.Binary.__eq__"></a>
#### \_\_eq\_\_

```python
 | __eq__(other: Any) -> bool
```

Implements equal, implements operand ==.

See _cmp() for details.

Method that implements "==" operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `bool` - result

<a name="binary.Binary.__lt__"></a>
#### \_\_lt\_\_

```python
 | __lt__(other: Any) -> bool
```

Less than operation.

Method that implements "<" operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `bool` - result

<a name="binary.Binary.__gt__"></a>
#### \_\_gt\_\_

```python
 | __gt__(other: Any) -> bool
```

Greater than operation.

Method that implements ">" operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `bool` - result

<a name="binary.Binary.__le__"></a>
#### \_\_le\_\_

```python
 | __le__(other: Any) -> bool
```

Less or equal operation.

Method that implements "<=" operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `bool` - result

<a name="binary.Binary.__ge__"></a>
#### \_\_ge\_\_

```python
 | __ge__(other: Any) -> bool
```

Greater or equal operation.

Method that implements ">=" operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `bool` - result

<a name="binary.Binary.__add__"></a>
#### \_\_add\_\_

```python
 | __add__(other: Any) -> Binary
```

Add operation.

Method that implements the + operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `Binary` - addittion of the two numbers

<a name="binary.Binary.__sub__"></a>
#### \_\_sub\_\_

```python
 | __sub__(other: Any) -> Binary
```

Subtraction operation.

Method that implements the - operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `Binary` - addittion of the two numbers

<a name="binary.Binary.__mul__"></a>
#### \_\_mul\_\_

```python
 | __mul__(other: Any) -> Binary
```

Multiply operation.

Method that implements the * operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - number


**Returns**:

- `Binary` - multiplication of the two numbers

<a name="binary.Binary.__truediv__"></a>
#### \_\_truediv\_\_

```python
 | __truediv__(other: Any) -> Binary
```

True division operation.

Method that implements the / operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - number


**Returns**:

- `Binary` - true division of the two numbers

<a name="binary.Binary.__floordiv__"></a>
#### \_\_floordiv\_\_

```python
 | __floordiv__(other: Any) -> Binary
```

Floor division operation.

Method that implements the // operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `Binary` - floor division of the two numbers

<a name="binary.Binary.__mod__"></a>
#### \_\_mod\_\_

```python
 | __mod__(other: Any) -> Binary
```

Compute modulo operation.

Method that implements modulo, i.e. it returns the integer remainder.
Method that implements the % operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - binary number


**Returns**:

- `Binary` - modulation of the two numbers

<a name="binary.Binary.__pow__"></a>
#### \_\_pow\_\_

```python
 | __pow__(other: Any) -> Binary
```

Power of operation.

Method that implements the ** operand.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - number


**Returns**:

- `Binary` - power of the two numbers

<a name="binary.Binary.__abs__"></a>
#### \_\_abs\_\_

```python
 | __abs__() -> Binary
```

Compute absolute value.

Method that implements absolute value, i.e. the positive value.

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `Binary` - Absolute of the number

<a name="binary.Binary.__ceil__"></a>
#### \_\_ceil\_\_

```python
 | __ceil__() -> int
```

Perform math ceiling operation.

Method that implements ceiling. Method for "ceil".
For example, '1.11' will return '10'.
Note, that math.ceil() will return an int.

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `int` - ceiling of the number
  Other classes like Fractions return class int.
  Following their lead, we do the same and return class int
  instead of class Binary. Use Binary(ceil(n)) to get result in Binary.

<a name="binary.Binary.__floor__"></a>
#### \_\_floor\_\_

```python
 | __floor__() -> int
```

Perform math floor operation.

Method that implements floor.
For example, '1.11' will return '1'.
Note, that math.floor() will return an int.

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `int` - floor of the number
  Other classes like Fractions return class int.
  Following their lead, we do the same and return class int
  instead of class Binary. Use Binary(floor(n)) to get result in Binary.

<a name="binary.Binary.__rshift__"></a>
#### \_\_rshift\_\_

```python
 | __rshift__(ndigits: int) -> Binary
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

<a name="binary.Binary.__lshift__"></a>
#### \_\_lshift\_\_

```python
 | __lshift__(ndigits: int) -> Binary
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

<a name="binary.Binary.__bool__"></a>
#### \_\_bool\_\_

```python
 | __bool__() -> bool
```

Boolean transformation. Used for bool() and not operand.

Method that implements transformation to boolean. This
boolian transformation is then used by operations like "not".

**Arguments**:

- `self` _Binary_ - binary number


**Returns**:

- `bool` - boolean transformation of the number

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

<a name="binary.Binary.__and__"></a>
#### \_\_and\_\_

```python
 | __and__(other: Any) -> Binary
```

Return the bitwise 'and' of self and other.

Method that implements the & operand.

For example, '11.1' & '10.1' will return '10.1'
'-0.1' & '+1' will return '-1' because twos-complement of
'-0.1' is 1.1; and 1.1 & 01.0 results in twos-complement 1.0;
and 1.0 in twos-complement is '-1' in binary fraction.
In short, any negative number will be converted into twos-complement
representation, than bitwise-and will be done, then the resulting
number will be converted back from twos-complement to
binary string format.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - number


**Returns**:

- `Binary` - bitwise 'and' of the two numbers in binary fraction format

<a name="binary.Binary.__or__"></a>
#### \_\_or\_\_

```python
 | __or__(other: Any) -> Binary
```

Return the bitwise 'or' of self and other.

Method that implements the | operand.

For example, '11.1' | '10.1' will return '11.1'
'-0.1' | '+1' will return '-0.1' because twos-complement of
'-0.1' is 1.1; and 1.1 | 01.0 results in twos-complement 1.1;
and 1.1 in twos-complement is '-0.1' in binary fraction.
In short, any negative number will be converted into twos-complement
representation, than bitwise-or will be done, then the resulting
number will be converted back from twos-complement to
binary string format.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - number


**Returns**:

- `Binary` - bitwise 'or' of the two numbers in binary fraction format

<a name="binary.Binary.__xor__"></a>
#### \_\_xor\_\_

```python
 | __xor__(other: Any) -> Binary
```

Return the bitwise 'xor' of self and other.

Method that implements the ^ operand.

For example, '11.1' ^ '10.1' will return '1'.
'-0.1' ^ '+1' will return '-1.1' because twos-complement of
'-0.1' is 1.1; and 1.1 ^ 01.0 results in twos-complement 10.1;
and 10.1 in twos-complement is '-1.1' in binary fraction.
In short, any negative number will be converted into twos-complement
representation, than bitwise-or will be done, then the resulting
number will be converted back from twos-complement to
binary string format.

**Arguments**:

- `self` _Binary_ - binary number
- `other` _Any_ - number


**Returns**:

- `Binary` - bitwise 'xor' (bitwise exclusive or) of the
  two numbers in binary fraction format

<a name="binary.Binary.__invert__"></a>
#### \_\_invert\_\_

```python
 | __invert__() -> Binary
```

Returns the 'bitwise not' of self.

Method that implements the ~ operand.
This is also called the 'invert' operand, or the 'bitwise not' operand.
Do not confuse it with the 'boolean not' operand implemented
via the 'not' operand and the __not__() method.

It is only defined for integers. If self is not an integer it
will raise an exception. For integers ~ is defined as
~n = -(n+1). For example, ~9 will return -10. ~-10 will return 9.
For more information, see also the invert() function.

**Arguments**:

- `self` _Binary_ - number


**Returns**:

- `Binary` - 'bitwise not' of integer number

<a name="binary.TestTwosComplement"></a>
## TestTwosComplement Objects

```python
class TestTwosComplement(unittest.TestCase)
```

Unit testing of class TwosComplement.

<a name="binary.TestTwosComplement.selftest"></a>
#### selftest

```python
 | selftest() -> bool
```

Perform self test by running various test cases.

Binary uses module unittest for unit testing.
See https://docs.python.org/3/library/unittest.html for details.

**Arguments**:

  none


**Returns**:

- `bool` - True if all tests pass, False if any single test fails

<a name="binary.TestTwosComplement.test___new__"></a>
#### test\_\_\_new\_\_

```python
 | test___new__()
```

Testing the constructor.

<a name="binary.TestTwosComplement.test__int2twoscomp"></a>
#### test\_\_int2twoscomp

```python
 | test__int2twoscomp()
```

Test function/method.

<a name="binary.TestTwosComplement.test__frac2twoscomp"></a>
#### test\_\_frac2twoscomp

```python
 | test__frac2twoscomp()
```

Test function/method.

<a name="binary.TestTwosComplement.test__float2twoscomp"></a>
#### test\_\_float2twoscomp

```python
 | test__float2twoscomp()
```

Test function/method.

<a name="binary.TestTwosComplement.test__fraction2twoscomp"></a>
#### test\_\_fraction2twoscomp

```python
 | test__fraction2twoscomp()
```

Test function/method.

<a name="binary.TestTwosComplement.test__str2twoscomp"></a>
#### test\_\_str2twoscomp

```python
 | test__str2twoscomp()
```

Test function/method.

<a name="binary.TestTwosComplement.test_istwoscomplement"></a>
#### test\_istwoscomplement

```python
 | test_istwoscomplement()
```

Test function/method.

<a name="binary.TestTwosComplement.test_components"></a>
#### test\_components

```python
 | test_components()
```

Test function/method.

<a name="binary.TestTwosComplement.test_simplify"></a>
#### test\_simplify

```python
 | test_simplify()
```

Test function/method.

<a name="binary.TestTwosComplement.test_to_fraction"></a>
#### test\_to\_fraction

```python
 | test_to_fraction()
```

Test function/method.

<a name="binary.TestTwosComplement.test_to_float"></a>
#### test\_to\_float

```python
 | test_to_float()
```

Test function/method.

<a name="binary.TestTwosComplement.test_to_no_mantissa"></a>
#### test\_to\_no\_mantissa

```python
 | test_to_no_mantissa()
```

Test function/method.

<a name="binary.TestTwosComplement.test_to_not_exponential"></a>
#### test\_to\_not\_exponential

```python
 | test_to_not_exponential()
```

Test function/method.

<a name="binary.TestTwosComplement.test_invert"></a>
#### test\_invert

```python
 | test_invert()
```

Test function/method.

<a name="binary.TestBinary"></a>
## TestBinary Objects

```python
class TestBinary(unittest.TestCase)
```

Unit testing of class Binary.

<a name="binary.TestBinary.selftest"></a>
#### selftest

```python
 | selftest() -> bool
```

Perform self test by running various test cases.

Binary uses module unittest for unit testing.
See https://docs.python.org/3/library/unittest.html for details.

**Arguments**:

  none


**Returns**:

- `bool` - True if all tests pass, False if any single test fails

<a name="binary.TestBinary.test___new__"></a>
#### test\_\_\_new\_\_

```python
 | test___new__()
```

Testing the constructor.

<a name="binary.TestBinary.test_version"></a>
#### test\_version

```python
 | test_version()
```

Testing the version method.

<a name="binary.TestBinary.test_to_float"></a>
#### test\_to\_float

```python
 | test_to_float()
```

Test to_float() function.

<a name="binary.TestBinary.test_from_float"></a>
#### test\_from\_float

```python
 | test_from_float()
```

Testing from_float() function.

<a name="binary.TestBinary.test_to_not_exponential"></a>
#### test\_to\_not\_exponential

```python
 | test_to_not_exponential()
```

Test function/method.

<a name="binary.TestBinary.test___float__"></a>
#### test\_\_\_float\_\_

```python
 | test___float__()
```

Test __float__() method.

<a name="binary.TestBinary.test___int__"></a>
#### test\_\_\_int\_\_

```python
 | test___int__()
```

Test __int__() method.

<a name="binary.TestBinary.test___str__"></a>
#### test\_\_\_str\_\_

```python
 | test___str__()
```

Test __str__() method.

<a name="binary.TestBinary.test_compare_representation"></a>
#### test\_compare\_representation

```python
 | test_compare_representation()
```

Test function/method.

<a name="binary.TestBinary.test_no_prefix"></a>
#### test\_no\_prefix

```python
 | test_no_prefix()
```

Test function/method.

<a name="binary.TestBinary.test_np"></a>
#### test\_np

```python
 | test_np()
```

Test function/method.

<a name="binary.TestBinary.test_simplify"></a>
#### test\_simplify

```python
 | test_simplify()
```

Test function simplify().

<a name="binary.TestBinary.test_to_fraction"></a>
#### test\_to\_fraction

```python
 | test_to_fraction()
```

Test function/method.

<a name="binary.TestBinary.test___round__"></a>
#### test\_\_\_round\_\_

```python
 | test___round__()
```

Test function/method for rounding.

<a name="binary.TestBinary.test_round"></a>
#### test\_round

```python
 | test_round()
```

Test function/method for rounding.

<a name="binary.TestBinary.test_round_to"></a>
#### test\_round\_to

```python
 | test_round_to()
```

Test function/method for rounding.

<a name="binary.TestBinary.test_fill"></a>
#### test\_fill

```python
 | test_fill()
```

Test function/method.

<a name="binary.TestBinary.test_fill_to"></a>
#### test\_fill\_to

```python
 | test_fill_to()
```

Test function/method.

<a name="binary.TestBinary.test_to_simple_exponential"></a>
#### test\_to\_simple\_exponential

```python
 | test_to_simple_exponential()
```

Test function/method.

<a name="binary.TestBinary.test_to_sci_exponential"></a>
#### test\_to\_sci\_exponential

```python
 | test_to_sci_exponential()
```

Test function/method.

<a name="binary.TestBinary.test_to_eng_exponential"></a>
#### test\_to\_eng\_exponential

```python
 | test_to_eng_exponential()
```

Test function/method.

<a name="binary.TestBinary.test_get_components"></a>
#### test\_get\_components

```python
 | test_get_components()
```

Test function/method.

<a name="binary.TestBinary.test_components"></a>
#### test\_components

```python
 | test_components()
```

Test function/method.

<a name="binary.TestBinary.test_isinfinity"></a>
#### test\_isinfinity

```python
 | test_isinfinity()
```

Test function/method.

<a name="binary.TestBinary.test_isnegativeinfinity"></a>
#### test\_isnegativeinfinity

```python
 | test_isnegativeinfinity()
```

Test function/method.

<a name="binary.TestBinary.test_ispositiveinfinity"></a>
#### test\_ispositiveinfinity

```python
 | test_ispositiveinfinity()
```

Test function/method.

<a name="binary.TestBinary.test_isnan"></a>
#### test\_isnan

```python
 | test_isnan()
```

Test function/method.

<a name="binary.TestBinary.test_isint"></a>
#### test\_isint

```python
 | test_isint()
```

Test function/method.

<a name="binary.TestBinary.test_fraction"></a>
#### test\_fraction

```python
 | test_fraction()
```

Test function/method.

<a name="binary.TestBinary.test_value"></a>
#### test\_value

```python
 | test_value()
```

Test function/method.

<a name="binary.TestBinary.test_fraction_to_string"></a>
#### test\_fraction\_to\_string

```python
 | test_fraction_to_string()
```

Test function/method.

<a name="binary.TestBinary.test_isclose"></a>
#### test\_isclose

```python
 | test_isclose()
```

Test function/method.

<a name="binary.TestBinary.test___eq__"></a>
#### test\_\_\_eq\_\_

```python
 | test___eq__()
```

Test function/method.

<a name="binary.TestBinary.test___lt__"></a>
#### test\_\_\_lt\_\_

```python
 | test___lt__()
```

Test function/method.

<a name="binary.TestBinary.test___gt__"></a>
#### test\_\_\_gt\_\_

```python
 | test___gt__()
```

Test function/method.

<a name="binary.TestBinary.test___le__"></a>
#### test\_\_\_le\_\_

```python
 | test___le__()
```

Test function/method.

<a name="binary.TestBinary.test___ge__"></a>
#### test\_\_\_ge\_\_

```python
 | test___ge__()
```

Test function/method.

<a name="binary.TestBinary.test___add__"></a>
#### test\_\_\_add\_\_

```python
 | test___add__()
```

Test function/method.

<a name="binary.TestBinary.test___sub__"></a>
#### test\_\_\_sub\_\_

```python
 | test___sub__()
```

Test function/method.

<a name="binary.TestBinary.test___mul__"></a>
#### test\_\_\_mul\_\_

```python
 | test___mul__()
```

Test function/method.

<a name="binary.TestBinary.test___truediv__"></a>
#### test\_\_\_truediv\_\_

```python
 | test___truediv__()
```

Test function/method.

<a name="binary.TestBinary.test___floordiv__"></a>
#### test\_\_\_floordiv\_\_

```python
 | test___floordiv__()
```

Test function/method.

<a name="binary.TestBinary.test___mod__"></a>
#### test\_\_\_mod\_\_

```python
 | test___mod__()
```

Test function/method.

<a name="binary.TestBinary.test___pow__"></a>
#### test\_\_\_pow\_\_

```python
 | test___pow__()
```

Test function/method.

<a name="binary.TestBinary.test___abs__"></a>
#### test\_\_\_abs\_\_

```python
 | test___abs__()
```

Test function/method.

<a name="binary.TestBinary.test___ceil__"></a>
#### test\_\_\_ceil\_\_

```python
 | test___ceil__()
```

Test function/method.

<a name="binary.TestBinary.test___floor__"></a>
#### test\_\_\_floor\_\_

```python
 | test___floor__()
```

Test function/method.

<a name="binary.TestBinary.test___rshift__"></a>
#### test\_\_\_rshift\_\_

```python
 | test___rshift__()
```

Test function/method.

<a name="binary.TestBinary.test___lshift__"></a>
#### test\_\_\_lshift\_\_

```python
 | test___lshift__()
```

Test function/method.

<a name="binary.TestBinary.test___bool__"></a>
#### test\_\_\_bool\_\_

```python
 | test___bool__()
```

Test function/method.

<a name="binary.TestBinary.test___not__"></a>
#### test\_\_\_not\_\_

```python
 | test___not__()
```

Test function/method.

<a name="binary.TestBinary.test___and__"></a>
#### test\_\_\_and\_\_

```python
 | test___and__()
```

Test function/method.

<a name="binary.TestBinary.test___or__"></a>
#### test\_\_\_or\_\_

```python
 | test___or__()
```

Test function/method.

<a name="binary.TestBinary.test___xor__"></a>
#### test\_\_\_xor\_\_

```python
 | test___xor__()
```

Test function/method.

<a name="binary.TestBinary.test___invert__"></a>
#### test\_\_\_invert\_\_

```python
 | test___invert__()
```

Test function/method.

<a name="binary.TestBinary.test_to_twoscomplement"></a>
#### test\_to\_twoscomplement

```python
 | test_to_twoscomplement()
```

Test function/method.

<a name="binary.TestBinary.test_from_twoscomplement"></a>
#### test\_from\_twoscomplement

```python
 | test_from_twoscomplement()
```

Test function/method.

