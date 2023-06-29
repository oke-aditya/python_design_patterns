from state.vending_states import VendingState
from state.dispense_product_state import DispenseProductState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state.vending_machine import VendingMachine


class ProductSelectState(VendingState):
    def choose_product(
        self, vending_machine: "VendingMachine", product_code: str
    ) -> None:
        inventory = vending_machine.get_inventory()
        price = inventory.get(product_code, None)
        user_price = sum(vending_machine.get_coins())

        # Less money paid
        if user_price < price:
            self.refund_money(vending_machine)
            raise ValueError(
                f"Given money = {user_price} is less than price of product = {price} "
            )

        else:
            change = user_price - price
            # Simplifying the logic a bit here
            vending_machine.set_coins([change])
            vending_machine.set_vending_machine_state(
                DispenseProductState(vending_machine)
            )

    def refund_money(self, vending_machine: "VendingMachine") -> list[int]:
        coins_refund = vending_machine.get_coins()

        from state.idle_state import IdleState

        vending_machine.set_vending_machine_state(IdleState())
        return coins_refund
