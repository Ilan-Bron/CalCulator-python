from Operators.IBinaryOperator import IBinaryOperator


class Addition(IBinaryOperator):
    strength = 1
    symbol = "+"

    def calculate(self, first_number: int, second_number: int) -> int:
        return first_number + second_number
