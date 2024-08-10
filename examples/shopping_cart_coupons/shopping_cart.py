from typing import Self

from shopping_cart_coupons.base_product import BaseProduct


class ShoppingCart:
    _product_list: list[BaseProduct]
    
    def __init__(self: Self) -> None:
        pass

    def add_to_cart(self: Self, product: BaseProduct) -> None:
        #product_with_discount = 
        self._product_list.append(product)


    def get_total_price(self: Self) -> float:
        total_price = 0.0
        for product in self._product_list:
            total_price += product.get_price()
        
        return total_price
