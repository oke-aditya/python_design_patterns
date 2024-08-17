from bridge.shape import Circle
from bridge.drawing_api import DrawAPIV1, DrawAPIV2

if __name__ == "__main__":
    circle1 = Circle(5.0, 10.0, 7.0, DrawAPIV1())
    circle1.draw()

    circle2 = Circle(15.0, 20.0, 10.0, DrawAPIV2())
    circle2.draw()
