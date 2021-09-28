from typing import Protocol
from abc import abstractmethod

from OperationCalculators.IOperationCalculator import IOperationCalculator


class ISymbolToCalculatorResolver(Protocol):

    @abstractmethod
    def resolve(self, symbol: str) -> IOperationCalculator:
        raise NotImplementedError
