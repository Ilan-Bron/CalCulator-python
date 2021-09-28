from typing import Protocol
from abc import abstractmethod

from .IOperator import IOperator


class IOnarOperation(IOperator, Protocol):
    is_operand_before_operation : bool

    @abstractmethod
    def calculate(self, first_number: int) -> int:
        raise NotImplementedError
