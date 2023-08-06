# Command Design Pattern

Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. 

This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

Command pattern separates the logic of
1. Receiver
2. Invoker
3. Command



# Use Case

1. Support Undo Redo Operations.
2. Queue operations, schedule their execution, or execute them remotely.

# Examples

1. Design Text Editor with Cut Copy Paste / Undo Redo Functionality.
2. Design AC Remote / TV Remote.

```python

from command.ac import AirConditioner
from command.remote import RemoteControl
from command.ac_on_command import TurnOnAC


air_conditioner = AirConditioner()
remote_controller = RemoteControl()

remote_controller.set_command(TurnOnAC(air_conditioner))
remote_controller.press_button()
remote_controller.undo()

```

