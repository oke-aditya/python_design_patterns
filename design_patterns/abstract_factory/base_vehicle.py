from abc import ABC, abstractmethod

class BaseVehicle(ABC):
    @abstractmethod
    def speed(self) -> int:
        pass
