from typing import List

from .IOneStepEquationSimplifier import IOneStepEquationSimplifier
from SymbolToCalculatorResolver.ISymbolToCalculatorResolver import ISymbolToCalculatorResolver
from Operators.IOperator import IOperator
from OperationBorderFinder import find_operation_border


class StrengthBasedEquationSimplifier(IOneStepEquationSimplifier):

    def __init__(
            self,
            operator_list: List[IOperator],
            symbol_to_operator_calculator_resolver: ISymbolToCalculatorResolver):
        self.operator_list = operator_list
        self.symbol_to_operator_calculator_resolver = symbol_to_operator_calculator_resolver

    def __find_strongest_operator(self, equation: str, operator_list: List[IOperator]) -> int:

        biggest_strength = -1
        strongest_symbol_index = -1

        for current_index, symbol in enumerate(equation):

            for operator in operator_list:
                if symbol == operator.symbol:
                    if operator.strength > biggest_strength:
                        biggest_strength = operator.strength
                        strongest_symbol_index = current_index

        return strongest_symbol_index

    def __replace_operation_with_result(self, equation: str, operator_index: int, result: int) -> str:

        starting_index, end_index = find_operation_border(equation, operator_index)

        replaced_equation = equation[0:starting_index] + str(result) + equation[end_index + 1:]
        return replaced_equation

    def simplify(self, equation: str) -> str:

        strongest_symbol_index = self.__find_strongest_operator(equation, self.operator_list)

        if strongest_symbol_index == -1:
            return equation

        strongest_symbol = equation[strongest_symbol_index]

        current_calculator = self.symbol_to_operator_calculator_resolver.resolve(strongest_symbol)
        result = current_calculator.calculate(equation, strongest_symbol_index)

        simplified_equation = self.__replace_operation_with_result(equation, strongest_symbol_index, result)

        return simplified_equation
