# Design Parking Lot

## Gathering Requirements

1. No of exits and end entrances

Ans: assume 1 entrance and exit, but scalable

2. Types of parking spots?

Car, vehicle, bikes?

3. Payment Charges?

Hourly, Minute?

4. Parking floors?

Nope

5. Parking spot nearest to park for entrance?

For now, choose any, later optimize

### Objects

1. Vehicle:

Vehicle No, Type

2. Entrance

Find Parking spot, Update Parking Spot.

3. Parking Spot

Id, isEmpty, valid, price

4. Ticket

Entry time, parking spot id, ticket id.

5. Exit gate

calculate charges
collect payment,
reset parking spot.

### Design patterns

Use strategy and Factory patterns where needed.

Payment Strategy, Algorithm Strategy, etc.


