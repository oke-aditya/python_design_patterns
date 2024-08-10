# Apply Coupons to shopping cart.

Given a shopping cart with products and coupons.

Calculate the net price after applying coupons on products.

Coupons can be on different conditions.
1. N% off on the individual product.
2. P% off on next item
3. D% off on Nth item of Type T.

Sequentially apply all coupons and get the total Amount.


# Solution

Use decorator pattern to solve the problem.
Create base class Product, implement all products and coupons on it.
Apply discounts on Shopping cart which has products.



