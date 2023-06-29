from .base_decorator import BaseDecorator
from .base_pizza import BasePizza


class CheeseTopping(BaseDecorator):
    def __init__(self, pizza: BasePizza) -> None:
        self.pizza = pizza

    def cost(self) -> float:
        return self.pizza.cost() + 10
