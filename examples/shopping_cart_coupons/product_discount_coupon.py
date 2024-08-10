# Discount for product level coupon

from typing import Self, override
from examples.shopping_cart_coupons.product_type_enum import ProductTypeEnum
from shopping_cart_coupons.base_product import BaseProduct

PRODUCT_TYPE_DISCOUNT = {
    ProductTypeEnum.BOOKS : 0.1,
    ProductTypeEnum.ELECTRONICS: 0.2
}


class ProductLevelCoupon(BaseProduct):
    def __init__(self: Self, product: BaseProduct, product_type: ProductTypeEnum,) -> None:
        self.product_type = product_type
        self.product = product

    @override
    def get_price(self: Self) -> float:
        base_price = self.product.get_price()
        base_price = base_price - (base_price * PRODUCT_TYPE_DISCOUNT.get(self.product_type, 0))
        return base_price
