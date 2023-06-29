from state.has_money_state import HasMoneyState
from state.vending_states import VendingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state.vending_machine import VendingMachine


class IdleState(VendingState):
    def __init__(self, vending_machine: 'VendingMachine') -> None:
        vending_machine.set_coins(coins=[])

    def click_on_insert_coin(self, vending_machine: 'VendingMachine') -> None:
        vending_machine.set_vending_machine_state(HasMoneyState())

    # def click_on_product_select(vending_machine: 'VendingMachine'):
    #     return super().click_on_product_select()

    # def dispense_product(vending_machine: 'VendingMachine'):
    #     return super().dispense_product()
    
    # def get_change(vending_maching: 'VendingMachine'):
    #     return super().get_change()
    
    # def insert_coin(vending_machine: 'VendingMachine'):
    #     return super().insert_coin()
    
    # def refund_money(vending_machine: 'VendingMachine'):
    #     return super().refund_money()
    
