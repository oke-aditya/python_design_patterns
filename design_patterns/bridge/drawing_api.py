from abc import ABC, abstractmethod


class BaseDrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        pass

class DrawAPIV1(BaseDrawingAPI):
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"Drawing circle with x = {x}, y = {y} and radius = {radius}. With API V1")

class DrawAPIV2(BaseDrawingAPI):
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"Drawing circle with x = {x}, y = {y} and radius = {radius}. With API V2")

