from enum import Enum, auto 

class VehicleType(Enum):
    CAR = auto()
    BIKE = auto()
    BUS = auto()


class ParkingGate(Enum):
    ENTRY = auto()
    EXIT = auto()

class StatusEnum(Enum):
    OCCUPIED = auto()
    AVAILABLE = auto()
    

