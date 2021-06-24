


    def isint(self) -> bool:
        """Determines if binary fraction is an integer.

        This is a utility function.

        Returns:
        bool: True if int, False otherwise (Fraction, float)
        """
        result = #TODO
        return result



    def invert(value:str) -> str:
        """Inverts string that is in 2s-complement format.

        This is a utility function.
        It negates (flips) every bit in the string.
        Input must be of format:
            first bit: sign, 0 for +, 1 for -
            1 or more integer bits
            optional decimal point
            0 or more fractional bits
            optional exponent (e.g. e-12)

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
        str: bitwise negated string
        """
        result = #TODO
        return result


    def __not__(self):
        if isint(self):
            #TODO: use n = - (n+1) formula
        else:
            #TODO: raise exception telling user that invert on float it not defined.
            #TODO: And that the user should use Binary.invert(Binary.to_twos_complement(self)) instead.
        return #TODO


    def to_twos_complement(value) -> str:
        """Computes the representation as a string in 2s-complement.

        This is a utility function.
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
        str: binary string representation in 2s-complement
        """
        if not isinstance(value, str):
            raise TypeError(f"Argument {value} must be of type str.")
        # # TODO:
        if self.value >= 0:
            return self._value
        else:
            #TODO: convert -1.5e3 into 11.1e3 etc
            return # TODO

    def from_twos_complement(value) -> str:
        """The opposite of to_twos_complement(value) -> str:

        Converts '1101' to '-11' (-3)
        convert '1101.1e-2' to '-11.1e-2'  (-3.5/4)
        """
        #TODO
