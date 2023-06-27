from abstract_factory.base_vehicle import BaseVehicle

class Bike(BaseVehicle):
    def speed(self) -> int:
        return 20
