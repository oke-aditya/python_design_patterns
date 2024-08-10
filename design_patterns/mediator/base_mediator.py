from abc import ABC, abstractmethod
from mediator.base_bidder import BaseBidder

class BaseMediator(ABC):
    @abstractmethod
    def add_bidder(self, bidder: BaseBidder) -> None:
        pass
    
    @abstractmethod
    def place_bid(self, bidder: BaseBidder, bid_amount: int) -> None:
        pass

