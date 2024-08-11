from abc import ABC, abstractmethod
from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
    from visitor.base_visitor import RoomVisitor

class BaseRoom(ABC):
    @abstractmethod
    def accept(self: Self, visitor: RoomVisitor) -> None:
        pass

    def set_price(self: Self, price: int):
        self.price = price
