from abstract_factory.base_vehicle import BaseVehicle


class Car(BaseVehicle):
    def speed(self) -> int:
        return 30
