from math import sqrt

from ..IOnarOperation import IOnarOperation


class SquareRoot(IOnarOperation):
    strength = 3
    symbol = "v"

    is_operand_before_operation = False

    def calculate(self, first_number: int) -> int:
        return int(sqrt(first_number))
