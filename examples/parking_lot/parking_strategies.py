from .base_parking_strategy import BaseParkingStrategy
from .common_enums import StatusEnum

class BestFirstParkingStrategy(BaseParkingStrategy):
    def __init__(self, parking_slots: list[dict]) -> None:
        super().__init__(parking_slots)

    # Given the slot put the vehicle
    def park(self, slot: dict[str, str]) -> None:
        pass


    def unpark(self, slot: dict[str, str]) -> None:
        pass

    def find_parking_spot(self, vehicle) -> dict[str, str]:
        for slot in self.parking_slots:
            if slot["status"] == StatusEnum.AVAILABLE and slot["vehicle_type"] == vehicle.vehicle_type:
                return slot
        
        return {}
