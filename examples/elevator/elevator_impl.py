from elevator.elevator_enums import DirectionEnum
from elevator.elevator_states import IdleState
from collections import deque

class Elevator:
    def __init__(self, elevator_id, allowed_floors=None) -> None:
        self.elevator_id = elevator_id
        self.current_floor = 0
        self.allowed_floors = allowed_floors or range(1, 10)
        self.state = IdleState()
        self.direction = DirectionEnum.IDLE
        self.up_queue = deque()
        self.down_queue = deque()


    def change_state(self, new_state):
        self.state = new_state
    
    def request_floor(self, floor):
        if floor not in self.allowed_floors or floor == self.current_floor:
            return
        
        if floor > self.current_floor:
            if floor not in self.up_queue:
                self.up_queue.append(floor)
                self.up_queue = deque(sorted(self.up_queue))


        else:
            if floor not in self.down_queue:
                self.down_queue.append(floor)
                self.down_queue = deque(sorted(self.down_queue))

        self.update_direction()
    

    def update_direction(self):
        if self.direction == DirectionEnum.IDLE:
            if self.up_queue:
                self.direction = DirectionEnum.UP
            elif self.down_queue:
                self.direction = DirectionEnum.DOWN

    def get_next_destination(self):
        if self.direction == DirectionEnum.UP and self.up_queue:
            return self.up_queue[0]
        elif self.direction == DirectionEnum.DOWN and self.down_queue:
            return self.down_queue[0]
        return None

    def remove_current_floor(self):
        if self.direction == DirectionEnum.UP and self.up_queue and self.up_queue[0] == self.current_floor:
            self.up_queue.popleft()
        elif self.direction == DirectionEnum.DOWN and self.down_queue and self.down_queue[0] == self.current_floor:
            self.down_queue.popleft()

    def is_idle(self):
        return not self.up_queue and not self.down_queue

    def step(self, floor):
        self.state.step(self)

