from typing import override, Self, TYPE_CHECKING
from visitor.base_room import BaseRoom

if TYPE_CHECKING:
    from base_visitor import RoomVisitor

class SingleRoom(BaseRoom):
    _price = 10

    @override
    def accept(self: Self, visitor: RoomVisitor) -> None:
        return visitor.visit(self)
    
class DoubleRoom(BaseRoom):
    _price = 20

    @override
    def accept(self: Self, visitor: RoomVisitor) -> None:
        return visitor.visit(self)

class DeluxeRoom(BaseRoom):
    _price = 30

    @override
    def accept(self: Self, visitor: RoomVisitor) -> None:
        return visitor.visit(self)

