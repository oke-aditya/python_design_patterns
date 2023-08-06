from command.base_command import BaseCommand

class RemoteControl:
    _command_history : list[BaseCommand] = []
    _command: BaseCommand = None

    def set_command(self, command: BaseCommand) -> None:
        self._command = command
    
    def press_button(self) -> None:
        self._command.execute()
        self._command_history.append(self._command)
    
    def undo(self) -> None:
        if len(self._command_history) != 0:
            last_command: BaseCommand = self._command_history.pop()
            last_command.undo()

