from command.ac import AirConditioner
from command.remote import RemoteControl
from command.ac_on_command import TurnOnAC

if __name__ == "__main__":
    air_conditioner = AirConditioner()
    remote_controller = RemoteControl()

    remote_controller.set_command(TurnOnAC(air_conditioner))
    remote_controller.press_button()

    remote_controller.undo()
