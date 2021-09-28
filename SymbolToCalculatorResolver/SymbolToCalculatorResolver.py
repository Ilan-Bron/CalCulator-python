from typing import Dict

from .ISymbolToCalculatorResolver import ISymbolToCalculatorResolver
from OperationCalculators.IOperationCalculator import IOperationCalculator


class SymbolToCalculatorResolver(ISymbolToCalculatorResolver):

    def __init__(self, symbol_to_calculator_dictionary: Dict[str, IOperationCalculator]):
        self.symbol_to_calculator_dictionary = symbol_to_calculator_dictionary

    def resolve(self, symbol: str) -> IOperationCalculator:
        return self.symbol_to_calculator_dictionary[symbol]
