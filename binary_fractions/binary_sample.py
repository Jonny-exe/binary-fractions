#!/usr/bin/python3

"""Sample program using the Binary class and module."""

from binary import TwosComplement
from binary import Binary
import math

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
print(f"round({bf1}) = {round(bf1)}")
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
print(f"type({tc1}) = {type(tc1)}")
print(f"Binary('{bf3}').to_not_exponential() = {bf3.to_not_exponential()}")
print(f"Binary('{bf3}').to_simple_exponential() = {bf3.to_simple_exponential()}")
print(
    f"Binary('{bf3}').to_sci_exponential() = {bf3.to_sci_exponential()}"
)  # scientific
print(f"Binary('{bf1}').to_twos_complement() = {bf1.to_twoscomplement()}")
print(f"Binary.from_twos_complement('{tc1}') = {Binary.from_twoscomplement(tc1)}")
print(f"Binary.from_twos_complement('{tc2}') = {Binary.from_twoscomplement(tc2)}")
print(f"Binary({fl1}) = {Binary(fl1)}")
print(f"TwosComplement({fl2}) = {TwosComplement(fl2)}")
print("And there are more operands, more methods, more functions, ...")
print(
    "Read the documentation at "
    "https://raw.githubusercontent.com/Jonny-exe/binary-fractions"
    " for more information."
)

# End of file
