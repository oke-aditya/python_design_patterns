from adapter.weight_machine_adapter import WeightMachineAdapter
from adapter.weight_machine import WeightMachine

if __name__ == "__main__":
    wm_adapter = WeightMachineAdapter(WeightMachine())
    print(wm_adapter.get_weight_machine_in_kgs())
