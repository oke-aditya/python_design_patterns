from abc import ABC, abstractmethod


class BaseProcessorFlyweight(ABC):
    @abstractmethod
    def display(self, row: int, col: int) -> None:
        pass
