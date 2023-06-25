# Say now user orders farmhouse pizza with Cheese topping

from .cheese_topping import CheeseTopping
from .farmhouse_pizza import FarmHousePizza

if __name__ == "__main__":
    topped_pizza = CheeseTopping(FarmHousePizza())
    print(f"Cost of topped pizza = {topped_pizza.cost()}")
