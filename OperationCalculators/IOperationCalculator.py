from typing import Protocol
from abc import abstractmethod


class IOperationCalculator(Protocol):

    @abstractmethod
    def calculate(self, equation: str, operator_index: int) -> int:
        raise NotImplementedError
