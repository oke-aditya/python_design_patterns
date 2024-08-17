from abc import ABC, abstractmethod
from typing import override

from bridge.drawing_api import BaseDrawingAPI


class Shape(ABC):
    def __init__(self, draw_api: BaseDrawingAPI) -> None:
        self.draw_api = draw_api

    @abstractmethod
    def draw(self) -> None:
        pass

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float, draw_api: BaseDrawingAPI) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(draw_api)

    @override
    def draw(self) -> None:
        self.draw_api.draw_circle(x=self.x, y=self.y, radius=self.radius)
