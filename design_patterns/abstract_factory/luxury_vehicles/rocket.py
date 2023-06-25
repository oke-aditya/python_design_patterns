from abstract_factory.base_vehicle import BaseVehicle

class Rocket(BaseVehicle):
    def speed(self) -> int:
        return 80
