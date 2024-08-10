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
    
