from decorator.base_pizza import BasePizza


class FarmHousePizza(BasePizza):
    def cost(self) -> float:
        return 200
