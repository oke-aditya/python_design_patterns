from adapter.base_weight_machine_adapter import BaseWeightMachineAdapter

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from adapter.base_weight_machine import BaseWeightMachine


class WeightMachineAdapter(BaseWeightMachineAdapter):
    def __init__(self, weight_machine: BaseWeightMachine) -> None:
        self.weight_machine = weight_machine
    
    def get_weight_machine_in_kgs(self,) -> float:
        weight_kgs = self.weight_machine.get_weight_in_pounds() * 0.45
        return weight_kgs
