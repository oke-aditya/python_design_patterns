from .base_vehicle import BaseVehicle
from .common_enums import VehicleType


class Car(BaseVehicle):
    def __init__(self, vehicle_number) -> None:
        super().__init__(vehicle_number, vehicle_type=VehicleType.CAR)


class Bike(BaseVehicle):
    def __init__(self, vehicle_number) -> None:
        super().__init__(vehicle_number, vehicle_type=VehicleType.BIKE)
    

class Bus(BaseVehicle):
    def __init__(self, vehicle_number) -> None:
        super().__init__(vehicle_number, vehicle_type=VehicleType.BUS)
    
