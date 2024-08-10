# Mediator pattern

Allows loose coupling between pattern. 

Avoids referring objects calling each other explicity. 


## Examples

- Online Auction system. 
E.g. In auctions people refer through a person via bids.

- Flight management system.

Two planes never talk to each other, but mediator.

```python

from mediator.auction import Auction
from mediator.concrete_bidder import Bidder

if __name__ == "__main__":
    auction = Auction()
    bidder_a = Bidder("A", auction)
    bidder_b = Bidder("B", auction)
    bidder_c = Bidder("C", auction)

    bidder_a.place_bid(10)
    bidder_b.place_bid(20)
    bidder_c.place_bid(30)
    
```
