from Operators.IBinaryOperator import IBinaryOperator
from OperationBorderFinder import find_operation_border

from .IOperationCalculator import IOperationCalculator


class BinaryOperationCalculator(IOperationCalculator):

    def __init__(self, operator: IBinaryOperator):
        self.operator = operator

    def calculate(self, equation: str, operator_index: int) -> int:
        given_symbol: str = equation[operator_index]

        if given_symbol != self.operator.symbol:
            raise IndexError(
                f"given operator symbol doesn't match. expected : {self.operator.symbol} got instead : {given_symbol}")

        starting_index, end_index = find_operation_border(equation, operator_index)

        first_operand_string = equation[starting_index:operator_index]
        if first_operand_string == "":
            first_operand = 0
        else:
            first_operand = int(first_operand_string)

        second_operand_string = equation[operator_index + 1: end_index + 1]
        if second_operand_string == "":
            second_operand = 0
        else:
            second_operand = int(second_operand_string)

        result = self.operator.calculate(first_operand, second_operand)

        return result
