from state.inventory import INVENTORY

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state.vending_states import VendingState


class VendingMachine:
    vending_state = None
    inventory = INVENTORY
    coins: list[int] = []

    def get_vending_machine_state(self) -> "VendingState":
        return self.vending_state

    def set_vending_machine_state(self, vending_state: "VendingState") -> None:
        self.vending_state = vending_state

    def set_coins(self, coins: list[int]) -> None:
        self.coins = coins

    def get_coins(self) -> list[int]:
        return self.coins

    def get_inventory(self) -> dict[str, int]:
        return self.inventory

    def set_inventory(self, inventory: dict[str, int]) -> None:
        self.inventory = inventory
