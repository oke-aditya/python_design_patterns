from parking_lot.common_enums import StatusEnum

class ParkingSpot:
    def __init__(self, slot, vehicle_type, status, floor) -> None:
        self.slot = slot
        self.vehicle_type = vehicle_type
        self.status = status
        self.floor = floor
    
    def book_slot(self):
        self.status = StatusEnum.OCCUPIED

    def release_slot(self):
        self.status = StatusEnum.AVAILABLE
