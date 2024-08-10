from abc import ABC, abstractmethod

class BaseBidder(ABC):
    @abstractmethod
    def place_bid(self, bid_amount: int) -> None:
        pass

    @abstractmethod
    def notify(self, bid_amount: int) -> None:
        pass
    
    @abstractmethod
    def get_name() -> str:
        pass
