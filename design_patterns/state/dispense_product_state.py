from state.vending_states import VendingState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state.vending_machine import VendingMachine


class DispenseProductState(VendingState):
    def dispense_product(self, vending_machine: 'VendingMachine', product_code: str) -> None:
        # Remove that product from vending machine
        product_popped = vending_machine.inventory.pop(product_code)

        from state.idle_state import IdleState
        vending_machine.set_vending_machine_state(IdleState(vending_machine))

