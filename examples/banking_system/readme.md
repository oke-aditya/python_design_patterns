# The Core Concept

Unlike a normal web app where you check the system clock, in this problem, **every function call receives a timestamp integer**.  
You must **trust this input**.

Timestamps generally increase, but in **Level 3 / Level 4**, you might receive:
- Queries for past times
- Scheduled future events
---

# Level 1: The Setup

## Goal
Implement a banking system that handles account creation and money movement.

## Requirements

### `create_account(timestamp, account_id)`
- Creates a new account with a balance of `0`
- Returns:
  - `true` if the account was created
  - `false` if `account_id` already exists

---

### `deposit(timestamp, account_id, amount)`
- Adds `amount` to the account
- Returns:
  - The new balance (`int`) on success
  - `None` / `-1` if the account does not exist

---

### `transfer(timestamp, source_id, target_id, amount)`
- Moves money from `source_id` to `target_id`
- Fails if:
  - Either account does not exist
  - The source has insufficient funds
  - `source_id == target_id`
- Returns:
  - `true` on success
  - `false` on failure

---

# The Reference Architecture Strategy

## The Trap
Most candidates simply use a dictionary:

```python
balances = {"user1": 100}
```

The Solution: Create an Account class immediately. Even if Level 1 seems simple, store the data you might need.

# Level 3: The "Future" Twist (Scheduled Payments)

This is where the problem changes from a simple database to an Event Simulation.

The Prompt: Implement schedule_payment(timestamp, account_id, amount, delay).

This schedules a payment to be deducted from account_id at timestamp + delay.

Critical Constraint: You must also implement a check that runs before every single other operation to process any payments that have become "due" because the timestamp moved forward.

Return: A unique string ID for the scheduled payment (e.g., "payment1", "payment2").

## The Twist:

If the account has insufficient funds at the moment the payment is due, the payment is cancelled (not retried).

You typically need a cancel_payment(timestamp, account_id, payment_id) method as well.


## The Architecture Shift

You need a global Priority Queue (or a sorted list) of pending transactions.

Why? Because payments must be processed in chronological order.

If I schedule a payment for time=100, and then I call deposit at time=105, 
the system must first process the payment at 100 before processing the deposit at 105.




