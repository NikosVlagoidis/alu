class Unsigned:
    """
    Custom implementation of an unsigned 3-bit binary number.
    """

    def __init__(self, number: int):
        """
        Constructor method of Unsigned class
        :param number (int): Integer number of the unsigned binary number
        """
        if 0 > number or number > 7:
            raise OverflowError("Byte should be between 0-7")
        self.integer = number

    def __add__(self, other):
        """
        Implementation of addition operator + for Unsigned numbers
        :param other (Unsigned): The other Unsigned number
        :return: Unsigned
        """
        try:
            return Unsigned(self.integer + other.integer)
        except OverflowError:
            raise OverflowError(f"Cannot add numbers {self} {other}")

    def __sub__(self, other):
        """
        Implementation of subtract operator - for Unsigned numbers
        :param other (Unsigned): The other Unsigned number
        :return: Unsigned
        """
        try:
            return Unsigned(self.integer - other.integer)
        except OverflowError:
            raise OverflowError(f"Cannot subtract numbers {self} {other}")

    def __invert__(self):
        """
        Implementation of invert operator ~ for Unsigned numbers
        :return: Unsigned
        """
        unsignie = f'{self.integer:03b}'.replace(
            '1', '@'
        ).replace('0', '1').replace('@', '0')

        return Unsigned(int(unsignie, 2))

    def __and__(self, other):
        """
        Implementation of and operator & for Unsigned numbers
        :param other (Unsigned): The other Unsigned number
        :return: Unsigned
        """
        return Unsigned(self.integer & other.integer)

    def __or__(self, other):
        """
        Implementation of or operator | for Unsigned numbers
        :param other: (Unsigned): The other Unsigned number
        :return: Unsigned
        """
        return Unsigned(self.integer | other.integer)

    def __xor__(self, other):
        """
        Implementation of xor operator ^ for Unsigned numbers
        :param other: (Unsigned): The other Unsigned number
        :return: Unsigned
        """
        return Unsigned(self.integer ^ other.integer)

    def __repr__(self):
        """
        Implementation of representation for Unsigned numbers
        :return: string
        """
        return f'{self.integer:b}'
