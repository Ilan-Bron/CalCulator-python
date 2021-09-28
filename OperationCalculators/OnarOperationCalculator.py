from Operators.IOnarOperation import IOnarOperation
from OperationBorderFinder import find_operation_border

from .IOperationCalculator import IOperationCalculator


class OnarOperationCalculator(IOperationCalculator):

    def __init__(self, operator: IOnarOperation):
        self.operator = operator

    def calculate(self, equation: str, operator_index: int) -> int:
        given_symbol = equation[operator_index]

        if given_symbol != self.operator.symbol:
            raise IndexError(
                f"given operator symbol doesn't match. expected : {self.operator.symbol} got instead : {given_symbol}")

        starting_index, end_index = find_operation_border(equation, operator_index)

        if self.operator.is_operand_before_operation:
            operand = int(equation[starting_index:operator_index])
        else:
            operand = int(equation[operator_index + 1: end_index + 1])

        result = self.operator.calculate(operand)

        return result
