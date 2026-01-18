# e will use a Max-Heap to track available space.

# The Problem: When you release a task, a server's available space increases. 
# You cannot easily find and update that server inside the Heap.

# The Solution: The "Lazy Update" pattern. 
# When a server's state changes, we don't fix the old entry in the heap. 
# We just push a new, correct entry and ignore the old "ghost" entry when it eventually bubbles to the top.

import heapq

class LoadBalancer:
    def __init__(self) -> None:
        # Source of Truth: { server_id: current_capacity }
        self.server_capacity = {}
        
        # Task Tracking: { task_id: (server_id, load_amount) }
        self.task_map = {}
        
        # The Ranking Engine: Max-Heap of servers
        # Format: [ (-free_space, server_id), ... ]
        # We use negative free_space because Python's heapq is a Min-Heap
        self.heap = []
    

    def add_server(self, server_id, capacity):
        if server_id in self.server_capacity:
            return False
        
        self.server_capacity[server_id] = capacity
        heapq.heappush(self.heap, (-capacity, server_id))

    
    def assign_task(self, task_id, load):
        if task_id in self.task_map:
            return False

        # We need to find the best server (Most Free Space).
        # But our heap might contain "Stale" (Ghost) entries from previous updates.

        candidate_server = None
        candidate_cap = -1

        while self.heap:
            neg_cap, server_id = heapq.heappop(self.heap)
            real_cap = -neg_cap

            # CHECK FOR GHOSTS:
            # Does the capacity in the heap match the REAL capacity in our Map?
            if server_id in self.server_capacity and self.server_capacity[server_id] == real_cap:
                if real_cap >= load:
                    candidate_server = server_id
                    candidate_cap = real_cap
                    break # found a server
                else:
                    # If the server with highest capacity cannot do it, nobody can
                    heapq.heappush(self.heap, (neg_cap, server_id))
            else:
                continue
        
        if not candidate_server:
            return False
        
        new_cap = candidate_cap - load
        self.server_capacity[candidate_server] = new_cap
        self.task_map[task_id] = (candidate_server, load)
        
        # Push the NEW state to the heap
        heapq.heappush(self.heap, (-new_cap, candidate_server))

    def release_task(self, task_id):
        if task_id not in self.task_map:
            return False
            
        server_id, load = self.task_map[task_id]
        
        # 1. Update the Source of Truth
        if server_id in self.server_capacity:
            self.server_capacity[server_id] += load
            current_cap = self.server_capacity[server_id]
            
            # 2. Push the NEW state to the heap
            # NOTE: We do NOT remove the old state (with less capacity). 
            # The old state is now a "Ghost" and will be ignored by assign_task.
            heapq.heappush(self.heap, (-current_cap, server_id))
            
        del self.task_map[task_id]
        return True



