from strategy.drive_strategy_modes.drive_strategy import DriveStrategy
from strategy.drive_strategy_modes.normal_drive_strategy import NormalDriveStrategy
from strategy.vehicle import Vehicle

class NormalVehicle(Vehicle):
    def __init__(self, drive_strategy: DriveStrategy = NormalDriveStrategy) -> None:
        super().__init__(drive_strategy)

    def drive(self) -> str:
        return self.drive_strategy.drive()
