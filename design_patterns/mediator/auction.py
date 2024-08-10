from typing import override
from design_patterns.mediator.base_bidder import BaseBidder
from mediator.base_mediator import BaseMediator


class Auction(BaseMediator):
    _bidders_list: list[BaseBidder] = []
        
    @override
    def add_bidder(self, bidder: BaseBidder) -> None:
        self._bidders_list.append(bidder)
    
    @override
    def place_bid(self, bidder: BaseBidder, bid_amount: int) -> None:
        for all_bidders in self._bidders_list:
            if bidder.get_name() != all_bidders.get_name():
                bidder.notify(bid_amount)
