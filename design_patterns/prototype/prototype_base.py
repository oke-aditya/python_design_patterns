from abc import ABC
from typing import Self

class BasePrototype(ABC):
    def clone() -> Self:
        pass
