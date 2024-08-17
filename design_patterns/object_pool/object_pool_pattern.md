# Object Pool design Pattern

Manage pool of objects. 

Borrow from the pool -> use it and return back to the pool.

## Advantages

Reduces overhead of creating objects, making connections faster.

Reduces latency.

Limits the use of resources.

## Disadvantages

Resource leakage can happen.

Required more memory due to additional overhead.

Needs thread safety, which is complex overhead.
