## Load Balancer

This archetype tests your ability to handle two conflicting requirements:

    Fast Lookup: You need to find a specific task instantly to delete it (O(1)).

    Fast Ranking: You need to always pick the "best" server (e.g., most free space) (O(logN)).

If you just use a List, finding the best server is slow (O(N)). If you just use a Map, you can't find the "max" efficiently. You need both.
The Architecture: Map + Lazy Heap

We will use a Max-Heap to track available space.

    The Problem: When you release a task, a server's available space increases. You cannot easily find and update that server inside the Heap.

    The Solution: The "Lazy Update" pattern. When a server's state changes, we don't fix the old entry in the heap. We just push a new, correct entry and ignore the old "ghost" entry when it eventually bubbles to the top.


