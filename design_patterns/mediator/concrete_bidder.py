from mediator.base_bidder import BaseBidder
from mediator.base_mediator import BaseMediator
from typing import override

class Bidder(BaseBidder):
    def __init__(self, name: str, mediator: BaseMediator) -> None:
        self.name = name
        self.mediator = mediator
        self.mediator.add_bidder(self)
    
    @override
    def get_name(self) -> str:
        return self.name

    @override
    def place_bid(self, bid_amount: int) -> None:
        self.mediator.place_bid(bid_amount)
    
    @override
    def notify(self, bid_amount: int) -> None:
        print(f"Bidder {self.name} has bidded for amount = {bid_amount}")
