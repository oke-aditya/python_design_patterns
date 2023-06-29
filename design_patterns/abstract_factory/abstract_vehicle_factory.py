from abc import ABC
from abstract_factory.base_vehicle import BaseVehicle


class AbstractVehicleFactory(ABC):
    def get_vehicle(vehicle_name: str) -> BaseVehicle:
        pass
