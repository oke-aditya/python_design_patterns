from shape import Shape
from circle import Circle
from triangle import Traingle

class ShapeFactory:
    @staticmethod
    def get_shape(shape: str) -> Shape:
        match shape:
            case "Circle":
                return Circle()
            
            case "Triangle":
                return Traingle()
            
            case other:
                raise ValueError("No shape found")


if __name__ == "__main__":
    shape = ShapeFactory.get_shape("Circle")
    shape.draw()

