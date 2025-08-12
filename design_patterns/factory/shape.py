from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass

    @abstractmethod
    def area(self) -> float:
        pass
