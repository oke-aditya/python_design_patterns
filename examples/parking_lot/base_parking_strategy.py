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

# For now assume we do have this grid let's implement parking floor then
class BaseParkingStrategy(ABC):
    def __init__(self, parking_slots: list[dict]) -> None:
        self.parking_slots = parking_slots
    
    @abstractmethod
    def park(self) -> None:
        pass
    
    @abstractmethod
    def unpark(self, slot: dict[str, str]) -> None:
        pass

    @abstractmethod
    # Should return relevant spot info
    def find_parking_spot(self, vehicle) -> dict[str, str]:
        pass
    
