from typing import Protocol
from abc import abstractmethod

from .IOperator import IOperator


class IBinaryOperator(IOperator, Protocol):

    @abstractmethod
    def calculate(self, first_number: int, second_number: int) -> int:
        raise NotImplementedError
