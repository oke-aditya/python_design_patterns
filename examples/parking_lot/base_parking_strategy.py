# We need someway to know which floor and which slots are for what vehicles

# Maybe we can map these or maintiain a stucture like this
# [['Slot': 'VehicleType'], [['Slot': 'VehicleType']], [['Slot': 'VehicleType']]]
# Say this comes from a JSON that can be stored and fetched

PARKING_SLOTS = [
    {
        "Slot": "",
        "VehicleType": "",
        "Status": "",
        "Floor": "",
    },

    {
        "Slot": "",
        "VehicleType": "",
        "Status": "",
        "Floor": "",
    },
    
    {
        "Slot": "",
        "VehicleType": "",
        "Status": "",
        "Floor": "",
    },    
]


from abc import ABC, abstractmethod
from .parking_spot import ParkingSpot
from typing import Optional

# For now assume we do have this grid let's implement parking floor then
class BaseParkingStrategy(ABC):
    def __init__(self, parking_spots: list[ParkingSpot]) -> None:
        self.parking_spots = parking_spots

    @abstractmethod
    # Should return relevant spot info
    def find_parking_spot(self, vehicle) -> Optional[ParkingSpot]:
        pass
    
