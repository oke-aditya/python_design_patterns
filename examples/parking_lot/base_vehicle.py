from abc import ABC, abstractmethod

class BaseVehicle(ABC):
    @abstractmethod
    def __init__(self, vehicle_number, vehicle_type) -> None:
        super().__init__()
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

