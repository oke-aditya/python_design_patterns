from abc import ABC, abstractmethod


class BaseWeightMachineAdapter(ABC):
    @abstractmethod
    def get_weight_machine_in_kgs(self) -> float:
        pass
