from typing import Protocol


class IOperator(Protocol):
    strength: int
    symbol: str
