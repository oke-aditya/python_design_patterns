from abc import ABC
from .base_pizza import BasePizza

class BaseDecorator(BasePizza, ABC):
    pass
