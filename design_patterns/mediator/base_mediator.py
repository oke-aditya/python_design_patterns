from collections.abc import ABC
from mediator.base_bidder import BaseBidder

class BaseMediator(ABC):
    def add_bidder(self, bidder: BaseBidder) -> None:
        pass
    
    def place_bid(self, bidder: BaseBidder, bid_amount: int) -> None:
        pass

