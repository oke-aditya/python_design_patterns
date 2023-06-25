from strategy.drive_strategy_modes.drive_strategy import DriveStrategy
from abc import ABC


class Vehicle(ABC):
    drive_strategy: DriveStrategy

    def __init__(self, drive_strategy: DriveStrategy) -> None:
        self.drive_strategy = drive_strategy

    def drive(self) -> str:
        self.drive_strategy.drive()
