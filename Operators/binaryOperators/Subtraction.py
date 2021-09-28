from ..IBinaryOperator import IBinaryOperator


class Subtraction(IBinaryOperator):
    strength = 1
    symbol = "-"

    def calculate(self, first_number: int, second_number: int) -> int:
        return first_number - second_number
