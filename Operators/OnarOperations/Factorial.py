from ..IOnarOperation import IOnarOperation


class Factorial(IOnarOperation):
    strength = 3
    symbol = "!"

    is_operand_before_operation = True

    def calculate(self, first_number: int) -> int:
        if first_number == 0:
            return 1

        return self.calculate(first_number - 1) * first_number
