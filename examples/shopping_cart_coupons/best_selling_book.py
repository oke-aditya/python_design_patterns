from examples.shopping_cart_coupons.product_type_enum import ProductTypeEnum
from shopping_cart_coupons.base_product import BaseProduct
from typing import Self, override

class BestSellingBook(BaseProduct):
    def __init__(self: Self, name: str, product_type: ProductTypeEnum, original_price: float) -> None:
        super().__init__(name, product_type, original_price)

    @override
    def get_price(self: Self) -> float:
        return self.original_price
