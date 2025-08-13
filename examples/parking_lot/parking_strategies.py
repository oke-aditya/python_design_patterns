from parking_lot.parking_spot import ParkingSpot
from parking_lot.base_parking_strategy import BaseParkingStrategy
from parking_lot.common_enums import StatusEnum
from typing import Optional

class BestFirstParkingStrategy(BaseParkingStrategy):
    def __init__(self, parking_spot: list[ParkingSpot]) -> None:
        super().__init__(parking_spot)

    def find_parking_spot(self, vehicle) -> Optional[ParkingSpot]:
        for spot in self.parking_spots:
            if spot.status == StatusEnum.AVAILABLE and spot.vehicle_type == vehicle.vehicle_type:
                return spot
