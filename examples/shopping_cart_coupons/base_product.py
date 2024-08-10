from abc import ABC, abstractmethod
from typing import Self
from product_type_enum import ProductTypeEnum

class BaseProduct(ABC):
    def __init__(self: Self, name: str, product_type: ProductTypeEnum, original_price: float) -> None:
        self.name = name
        self.product_type = product_type
        self.original_price = original_price

    @abstractmethod
    def get_price(self: Self) -> float:
        pass

    def get_product_type(self: Self) -> ProductTypeEnum:
        return self.product_type
