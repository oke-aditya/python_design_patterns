from state.vending_states import VendingState
from typing import TYPE_CHECKING
from state.product_select_state import ProductSelectState

if TYPE_CHECKING:
    from state.vending_machine import VendingMachine


class HasMoneyState(VendingState):
    def click_on_product_select(self, vending_machine: 'VendingMachine') -> None:
        vending_machine.set_vending_machine_state(ProductSelectState())

    def insert_coin(self, vending_machine: 'VendingMachine', coin: int) -> None:
        print("Accepted the coin")
        vending_machine.coins.append(coin)
    
    def refund_money(self, vending_machine: 'VendingMachine') -> list[int]:
        print("Refunding Money")
        coins_refund = vending_machine.get_coins()
        
        from state.idle_state import IdleState
        vending_machine.set_vending_machine_state(IdleState(vending_machine))
        return coins_refund
