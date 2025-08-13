from abc import ABC, abstractmethod


class BaseWeightMachine(ABC):
    @abstractmethod
    def get_weight_in_pounds(self) -> float:
        pass
