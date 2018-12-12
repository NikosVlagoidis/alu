from unsigned import Unsigned


class ALU:

    def operate(self, *args, op_code: str) -> Unsigned:
        """
        Operation method for ALU
        :param args: the input values for the operation
        :param op_code:(string) operation code
        :return: Unsigned
        """
        return self.opcodes[op_code](*args)

    def add(self, first: Unsigned, second: Unsigned) -> Unsigned:
        """
        Add operation for ALU
        :param first: (Unsigned) First Unsigned for addition
        :param second: (Unsigned) Second Unsigned for addition
        :return: Unsigned
        """
        return first + second

    def sub(self, first: Unsigned, second: Unsigned) -> Unsigned:
        """
        Subtract operation for ALU
        :param first: (Unsigned) First Unsigned for addition
        :param second: (Unsigned) Second Unsigned for addition
        :return: Unsigned
        """
        return first - second

    def decrement(self, number: Unsigned) -> Unsigned:
        """
        Decrement operation for ALU
        :param number: (Unsigned) Unsigned number to decrement
        :return: Unsigned
        """
        try:
            return number - Unsigned(1)
        except OverflowError:
            raise OverflowError(f"Cannot decrease bellow 0")

    def increment(self, number: Unsigned) -> Unsigned:
        """
        Increment operation for ALU
        :param number: (Unsigned) Unsigned number to increment
        :return: Unsigned
        """
        try:
            return number + Unsigned(1)
        except OverflowError:
            raise OverflowError(f"Cannot increase above 7")

    def complement(self, number: Unsigned) -> Unsigned:
        """
        Complement operation for ALu
        :param number: (Unsigned) Unsigned number to complement
        :return: Unsigned
        """
        return ~number

    def bit_wise_and(self, first: Unsigned, second: Unsigned) -> Unsigned:
        """
        Bit wise AND operation for ALU
        :param first: (Unsigned) First Unsigned for AND operation
        :param second: (Unsigned) Second Unsigned for AND operation
        :return: Unsigned
        """
        return first & second

    def bit_wise_or(self, first: Unsigned, second: Unsigned) -> Unsigned:
        """
        Bit wise OR operation for ALU
        :param first: (Unsigned) First Unsigned for OR operation
        :param second: (Unsigned) Second Unsigned for OR operation
        :return: Unsigned
        """
        return first | second

    def bit_wise_xor(self, first: Unsigned, second: Unsigned) -> Unsigned:
        """
        Bit wise XOR operation for ALU
        :param first: (Unsigned) First Unsigned for XOR operation
        :param second: (Unsigned) Second Unsigned for XOR operation
        :return: Unsigned
        """
        return first ^ second

    @property
    def opcodes(self):
        """
        Opcodes for the ALU operations
        :return: dict
        """
        return {
            "000": self.add,
            "001": self.sub,
            "010": self.decrement,
            "011": self.increment,
            "100": self.complement,
            "101": self.bit_wise_and,
            "110": self.bit_wise_or,
            "111": self.bit_wise_xor

        }


if __name__ == "__main__":
    unsigned_a = Unsigned(3)
    unsigned_b = Unsigned(2)
    alu = ALU()

    print(alu.operate(unsigned_a, unsigned_b, op_code="000"))
    print(alu.operate(unsigned_a, op_code="100"))
    print(alu.operate(unsigned_b, unsigned_b, op_code="101"))
    

    
