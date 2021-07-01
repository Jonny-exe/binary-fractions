#!/usr/bin/python3

"""Sample program using the Binary class and module."""

from binary import Binary
import math  # isclose()

bf1str: str = "-1.01"  # -1.25
bf2str: str = "10.1"  # 2.5
bf3str: str = "10.1e-3"  # 2.5/8
tcstr: str = "10.1"  # -1.5 in two's complement, '-0b1.1' as binary fraction
fl: float = 2.3

bf1: Binary = Binary(bf1str)
bf2: Binary = Binary(bf2str)
bf3: Binary = Binary(bf3str)

print("Sample program demonstrating binary fractions class and module:")
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
print(f"ceil({bf1}) = {math.ceil(bf1)}")
print(f"floor({bf1}) = {math.floor(bf1)}")
print(f"int({bf1}) = {int(bf1)}")
print(f"float({bf1}) = {float(bf1)}")
print(f"str({bf1}) = {str(bf1)}")
print(f"Fraction({bf1}) = {bf1._fraction} = {bf1.fraction()}")
print(f"{bf1} & {bf2} = {bf1&bf2}")
print(f"{bf1} | {bf2} = {bf1|bf2}")
print(f"{bf1} ^ {bf2} = {bf1^bf2}")
print(f"~(floor({bf2})) = {~(math.floor(bf2))}")
print(f"type({bf1}) = {type(bf1)}")
print(f"Binary('{bf3}').to_not_exponential() = {bf3.to_not_exponential()}")
print(f"Binary('{bf3}').to_simple_exponential() = {bf3.to_simple_exponential()}")
print(
    f"Binary('{bf3}').to_sci_exponential() = {bf3.to_sci_exponential()}"
)  # scientific
print(f"Binary('{bf1}').to_twos_complement() = {bf1.to_twos_complement()}")
print(f"Binary.from_twos_complement('{tcstr}') = {Binary.from_twos_complement(tcstr)}")
print(f"Binary.from_float({fl}) = {Binary.from_float(fl)}")
print("And there are more operands, more methods, more functions, ...")
print(
    "Read the documentation at "
    "https://raw.githubusercontent.com/Jonny-exe/binary-fractions"
    " for more information."
)

# End of file
