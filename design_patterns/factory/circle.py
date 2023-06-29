from shape import Shape


class Circle(Shape):
    def __init__(self, r=7) -> None:
        super().__init__()
        self.r = r

    def draw(self):
        return "Drawing a Circle"

    def area(self):
        return 3.14 * self.r * self.r


if __name__ == "__main__":
    c = Circle(7)
    print(c.draw())
    print(c.area())
