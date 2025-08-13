from abstract_factory.abstract_vehicle_factory import AbstractVehicleFactory
from abstract_factory.normal_vehicle_factory import NormalVehicleFactory
from abstract_factory.luxury_vehicle_factory import LuxuryVehicleFactory

## This follow abstract factory pattern, this returns is a factory of factories.


class VehicleFactory:
    @staticmethod
    def get_vehicle_factory(vehicle_factory_name: str) -> AbstractVehicleFactory:
        match vehicle_factory_name:
            case "normal":
                return NormalVehicleFactory
            case "luxury":
                return LuxuryVehicleFactory
