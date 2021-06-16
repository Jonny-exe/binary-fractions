# Binary fractions

This is really small package to handle binary fractions.

It has 2 functions:
  - float2bin, which converts floats to binary fractions represented in strings
  - bin2float, which converts binary fractions represented in strings to floats


```
valid binary fraction: "100111.110001"

float2bin:
  arguments: (float_number: float)
  optional_argument: (binary_places: int) # This specifies the precision of the returned bin. Default 50

bin2float:
  arguments: (bin_number: string)

```

