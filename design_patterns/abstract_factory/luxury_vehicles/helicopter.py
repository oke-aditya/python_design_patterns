from abstract_factory.base_vehicle import BaseVehicle


class Helicopter(BaseVehicle):
    def speed(self) -> int:
        return 60
