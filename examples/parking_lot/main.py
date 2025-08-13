from parking_lot.parking_spot import ParkingSpot
from parking_lot.parking_strategies import BestFirstParkingStrategy
from parking_lot.vehicles import Car, Bus, Bike
from parking_lot.common_enums import VehicleType, StatusEnum

if __name__ == "__main__":

    # Create few spots for parking
    print("hi")
    
    # We can probably create many of these parking spots
    parking_spot1 = ParkingSpot("A", VehicleType.CAR, StatusEnum.AVAILABLE, floor=1)
    parking_spot2 = ParkingSpot("B", VehicleType.BUS, StatusEnum.AVAILABLE, floor=1)
    parking_spot3 = ParkingSpot("C", VehicleType.CAR, StatusEnum.AVAILABLE, floor=1)
    parking_spot4 = ParkingSpot("D", VehicleType.BIKE, StatusEnum.AVAILABLE, floor=1)

    all_spots = [parking_spot1, parking_spot2, parking_spot3, parking_spot4]

    bfs = BestFirstParkingStrategy(all_spots)

    car1 = Car("ABC")
    bike1 = Bike("DEF")
    bus1 = Bus("XYZ")

    spot = bfs.find_parking_spot(car1)
    print(spot.slot, spot.status, spot.vehicle_type)

