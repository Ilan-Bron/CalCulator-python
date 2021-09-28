from Operators.IBinaryOperator import IBinaryOperator


class Maximum(IBinaryOperator):
    strength = 3
    symbol = "@"

    def calculate(self, first_number: int, second_number: int) -> int:
        return max(first_number, second_number)
