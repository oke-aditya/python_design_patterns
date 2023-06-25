from strategy.drive_strategy_modes.drive_strategy import DriveStrategy
from strategy.drive_strategy_modes.sport_drive_strategy import SportDriveStrategy
from strategy.vehicle import Vehicle

class OffRoadVehicle(Vehicle):
    def __init__(self, drive_strategy: DriveStrategy = SportDriveStrategy) -> None:
        super().__init__(drive_strategy)

    def drive(self) -> str:
        return self.drive_strategy.drive()

