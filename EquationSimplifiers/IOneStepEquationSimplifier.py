from typing import Protocol
from abc import abstractmethod


class IOneStepEquationSimplifier(Protocol):

    @abstractmethod
    def simplify(self, equation: str) -> str:
        raise NotImplementedError
