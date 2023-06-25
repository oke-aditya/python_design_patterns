# Decorator Pattern

Decorator is a structural design pattern that lets you attach 
new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

E.g. of decorator pattern

```python
from decorator.farmhouse_pizza import FarmHousePizza
from decorator.cheese_topping import CheeseTopping
topped_pizza = CheeseTopping(FarmHousePizza())
topped_pizza.cost()
```

Wrapping each object by other class adds the functionality of wrapper.

This design is also called wrapper pattern.


Use the Decorator pattern when you need to be able to assign extra behaviors 
to objects at runtime without breaking the code that uses these objects.

Use this when we have multiple permutations and combinations, we would otherwise need to create class for
every permutation and combination.

Use this to Prevent Class Explosion, everytime we don't need to inherit and create new type of Pizza.

Decorator has 2 relationships, it **is a** base class also **has a** class object.


# Use cases

1. Designing Pizza Order System.

2. Designing Coffee Machine


# Example

```python


```

