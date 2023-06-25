from decorator.base_pizza import BasePizza

class VegDelightPizza(BasePizza):
    def cost(self) -> float:
        return 400

