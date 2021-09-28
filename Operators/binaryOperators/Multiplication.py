from ..IBinaryOperator import IBinaryOperator


class Multiplication(IBinaryOperator):
    strength = 2
    symbol = "*"

    def calculate(self, first_number: int, second_number: int) -> int:
        return first_number * second_number
