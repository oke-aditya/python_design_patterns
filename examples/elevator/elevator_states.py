from abc import ABC, abstractmethod
from elevator.elevator_enums import DirectionEnum


class BaseElevatorState(ABC):
    @abstractmethod
    def step(self, elevator):
        pass

    @abstractmethod
    def on_request(self, elevator, floor):
        pass


class IdleState(BaseElevatorState):
    def step(self, elevator):
        elevator.update_direction()
        if not elevator.is_idle():
            elevator.transition_to(MovingState())

    def on_request(self, elevator, floor):
        elevator.request_floor(floor)
        elevator.update_direction()
        if not elevator.is_idle():
            elevator.transition_to(MovingState())



class MovingState(BaseElevatorState):
    def step(self, elevator):
        next_floor = elevator.get_next_destination()
        if next_floor is None:
            elevator.transition_to(IdleState())
            return

        if elevator.current_floor < next_floor:
            elevator.current_floor += 1
            elevator.direction = DirectionEnum.UP
        elif elevator.current_floor > next_floor:
            elevator.current_floor -= 1
            elevator.direction = DirectionEnum.DOWN
        else:
            elevator.remove_current_floor()
            if elevator.is_idle():
                elevator.transition_to(IdleState())
            else:
                elevator.update_direction()

    def on_request(self, elevator, floor):
        elevator.destination_floors.add(floor)


class StoppedState(BaseElevatorState):
    def step(self, elevator):
        if elevator.destination_floors:
            elevator.transition_to(MovingState())
        else:
            elevator.transition_to(IdleState())
    
    def on_request(self, elevator, floor):
        elevator.destination_floors.add(floor)


