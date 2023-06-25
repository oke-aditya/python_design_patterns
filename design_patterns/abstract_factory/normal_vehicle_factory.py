from abstract_factory.base_vehicle import BaseVehicle
from abstract_factory.normal_vehicles.car import Car
from abstract_factory.normal_vehicles.bike import Bike
from abstract_factory.abstract_vehicle_factory import AbstractVehicleFactory


class NormalVehicleFactory(AbstractVehicleFactory):
    @staticmethod
    def get_vehicle(vehicle_name: str) -> BaseVehicle:
        match vehicle_name:
            case "car":
                return Car()
            
            case "bike":
                return Bike()
