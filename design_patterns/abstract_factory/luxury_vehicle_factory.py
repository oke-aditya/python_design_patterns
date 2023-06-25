from abstract_factory.base_vehicle import BaseVehicle
from abstract_factory.luxury_vehicles.helicopter import Helicopter
from abstract_factory.luxury_vehicles.rocket import Rocket
from abstract_factory.abstract_vehicle_factory import AbstractVehicleFactory

class LuxuryVehicleFactory(AbstractVehicleFactory):
    @staticmethod
    def get_vehicle(vehicle_name: str) -> BaseVehicle:
        match vehicle_name:
            case "helicopter":
                return Helicopter()
            case "rocket":
                return Rocket()

