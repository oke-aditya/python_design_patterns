from .drive_strategy import DriveStrategy

class NormalDriveStrategy(DriveStrategy):
    def drive() -> str:
        return "Normal Driving Mode"

