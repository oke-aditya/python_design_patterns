from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw() -> str:
        pass
    
    @abstractmethod
    def area() -> float:
        pass
