import bisect

class KVStore:
    def __init__(self) -> None:
        # Map<String, List of Tuples>
        # Key -> [(timestamp, value), (timestamp, value)...]
        self.store = {}

    def set(self, key, value, timestamp, ttl):
        if key not in self.store:
            self.store[key] = []
        
        expiry = timestamp + ttl
        # Append the new value with its timestamp
        # Assumption: Timestamps in calls strictly increase (Standard Constraint)
        self.store[key].append((timestamp, value, expiry))
        return True
    
    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        
        records = self.store[key]
        
        latest_record = records[-1]

        start_time, value, expiry_time = latest_record

        if timestamp >= expiry_time:
            return ""
        
        return value
    
    def get_at_time(self, key, target_time):
        if key not in self.store:
            return ""
            
        records = self.store[key]
        # We need to find the record that started BEFORE or AT target_time
        # and hasn't expired yet.
        
        # Step 1: Binary Search to find the right insertion point
        # We search based on 'start_time' (index 0 of tuple)
        # We want the rightmost record where start_time <= target_time
        
        # Create a dummy tuple for comparison. We pick a value that ensures strict ordering.
        # This effectively searches for the first record that starts AFTER target_time
        idx = bisect.bisect_right(records, (target_time, float('inf'), float('inf')))    
        if idx == 0:
            return "" # All records start after target_time
            
        # The candidate is the one just before the insertion point
        candidate = records[idx - 1]
        start_time, value, expiry_time = candidate

        # A record is valid if:
        # 1. It started before or at target_time (Handled by Binary Search)
        # 2. It hasn't expired (TTL check)
        # 3. It wasn't overwritten by a newer record before target_time?
        #    Actually, since we picked the rightmost record <= target_time, 
        #    we naturally picked the "latest" update relative to that time.
        
        if target_time >= expiry_time:
            return "" # It expired before we queried it
            
        return value
