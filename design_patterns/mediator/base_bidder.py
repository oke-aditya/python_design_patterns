from collections.abc import ABC

class BaseBidder(ABC):
    def place_bid(self, bid_amount: int) -> None:
        pass

    def notify(self, bid_amount: int) -> None:
        pass
    
    def get_name() -> str:
        pass
