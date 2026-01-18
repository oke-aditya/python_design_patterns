# Time-Based Key-Value Store" or "Cache with TTL."

It tests your ability to manage temporal data. Unlike a standard hash map where key=value overwrites the old value, here you often need to remember what the value was at which time.
Archetype 3: The Time-Based KV Store

The Core Conflict:

## Level 1 & 2 ask for "Current State" (Standard Hash Map).

## Level 3 asks for "Historical State" (What was the value 5 minutes ago?).

The Trap: If you overwrite data in Level 1, you cannot solve Level 3. You must store logs of changes, not just the final result.

## Level 1: Basic Set & Get

Goal: Implement set(key, value, timestamp) and get(key, timestamp).

    Twist: For Level 1, get usually just asks for the latest value.

The "Fellows Grade" Architecture: Do not use self.store = {key: value}. Instead, map each key to a List of Records. self.store = { key: [ (timestamp, value), ... ] }

## Level 2: Time-To-Live (TTL)

Goal: set(key, value, timestamp, ttl). The value is only valid for ttl seconds. If you get it after timestamp + ttl, it should return "" (or null).

The Logic Change: We need to store the expiry_time in our record tuple.

Old Tuple: (timestamp, value)

New Tuple: (timestamp, value, expiry_time)

## Level 3: The "Time Travel" Query

Goal: get_at_time(key, target_time).

Retrieve the value of key exactly as it was at target_time.

This is the "Hard" part. You have a list of updates, e.g., [(Time 10, "A"), (Time 20, "B"), (Time 30, "C")].

If I ask for get_at_time(25), you must return "B".
