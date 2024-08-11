from abc import ABC

from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from rooms import SingleRoom, DoubleRoom, DeluxeRoom

class RoomVisitor(ABC):
    def visit(self: Self, room: SingleRoom) -> None:
        pass

    def visit(self: Self, room: DoubleRoom) -> None:
        pass

    def visit(self: Self, room: DeluxeRoom) -> None:
        pass    
