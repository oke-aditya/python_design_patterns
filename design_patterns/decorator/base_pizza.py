from abc import ABC, abstractmethod


class BasePizza(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass
