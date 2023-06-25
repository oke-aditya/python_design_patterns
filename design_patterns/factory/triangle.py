from shape import Shape


class Traingle(Shape):
    def __init__(self, b=10, h=10) -> None:
        super().__init__()
        self.b = b
        self.h = h


    def draw(self):
        return "Drawing a triangle"

    def area(self):
        return 0.5 * self.b * self.h


if __name__ == "__main__":
    traingle = Traingle(10, 10)
    #print(traingle.draw())
    print(traingle.area())

