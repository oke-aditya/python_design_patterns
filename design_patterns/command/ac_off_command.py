from command.base_command import BaseCommand
from command.ac import AirConditioner


class TurnOfAc(BaseCommand):
    def __init__(self, ac: AirConditioner) -> None:
        self.ac = ac
    def execute(self) -> None:
        self.ac.turn_off()

    def undo(self) -> None:
        self.ac.turn_on()
