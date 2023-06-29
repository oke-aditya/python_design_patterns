from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state.vending_machine import VendingMachine


class VendingState(ABC):
    def click_on_insert_coin(self, vending_machine: "VendingMachine"):
        raise NotImplementedError("Method not implemented")

    def click_on_product_select(self, vending_machine: "VendingMachine"):
        raise NotImplementedError("Method not implemented")

    def insert_coin(self, vending_machine: "VendingMachine", coin: int):
        raise NotImplementedError("Method not implemented")

    def choose_product(self, vending_machine: "VendingMachine", product_code: str):
        raise NotImplementedError("Method not implemented")

    def dispense_product(self, vending_machine: "VendingMachine", product_code: str):
        raise NotImplementedError("Method not implemented")

    def refund_money(self, vending_machine: "VendingMachine"):
        raise NotImplementedError("Method not implemented")

    def get_change(self, vending_maching: "VendingMachine"):
        raise NotImplementedError("Method not implemented")
