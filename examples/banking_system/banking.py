import heapq

class Account:
    def __init__(self, account_id) -> None:
        self.id = account_id
        self.balance = 0

        # Keep track of incoming and outgoing
        self.total_incoming = 0
        self.total_outgoing = 0
        
        # Store history, needed in future
        self.history = []

    
class BankSystem:
    def __init__(self) -> None:
        self.accounts = {} # <Str, account>
        self.payment_counter = 1

        # Priority Queue for scheduled payments
        # Format: (due_time, payment_id, account_id, amount)
        self.scheduled_payments = []

        # Map for O(1) cancellation lookups
        # payment_id -> (due_time, account_id, amount)
        self.active_payments = {}
    
    def _process_due_payments(self, current_time):
        """
        CRITICAL: Runs at the start of EVERY public method.
        """
        
        while self.scheduled_payments:
            due_time, pay_id, acct_id, amount = self.scheduled_payments[0]

            # If the next payment is in the future, stop processing
            if due_time > current_time:
                break
                
            heapq.heappop(self.scheduled_payments)

            # Check if it was cancelled (it won't be in active_payments if cancelled)
            if pay_id not in self.active_payments:
                continue
            
            acct = self.accounts.get(acct_id)
            if acct and acct.balance >= amount:
                acct.balance -= amount
                acct.total_outgoing += amount
            
            del self.scheduled_payments[pay_id]

    def schedule_payment(self, timestamp, account_id, amount, delay):
        self._process_due_payments(timestamp)

        if account_id not in self.accounts:
            return ""
        
        pay_id = f"payment{self.payment_counter}"
        self.payment_counter += 1
        due_time = timestamp + delay

        heapq.heappush(self.scheduled_payments, (due_time, pay_id, account_id, amount))
        self.active_payments[pay_id] = (due_time, account_id, amount)
        return pay_id

    def cancel_payment(self, timestamp, account_id, payment_id):
        self._process_due_payments(timestamp)
        
        if payment_id not in self.active_payments:
            return False
            
        # Verify ownership
        if self.active_payments[payment_id][1] != account_id:
            return False
            
        # "Lazy Delete": Just remove from the map. 
        # When the PQ pops it later, it will see it's missing from map and ignore it.
        del self.active_payments[payment_id]
        return True

    def create_account(self, timestamp, account_id):
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = Account(account_id)
        return True
    
    def deposit(self, timestamp, account_id, amount):
        # We must do this on every timstamp
        self._process_due_payments(timestamp)

        if account_id not in self.accounts:
            return None
        
        acct = self.accounts[account_id]
        acct.balance += amount
        acct.total_incoming += amount

        # log into history
        acct.history.append((timestamp, "DEPOSIT", amount, None))
        return acct.balance

    
    def transfer(self, timestamp, source_id, target_id, amount):
        # We must do this on every timstamp
        self._process_due_payments(timestamp)

        if source_id == target_id:
            return False
        if source_id not in self.accounts or target_id not in self.accounts:
            return False
        
        source = self.accounts[source_id]
        target = self.accounts[target_id]

        if source.balance < amount:
            return False
        
        source.balance -= amount
        target.balance += amount

        source.total_outgoing += amount
        target.total_incoming += amount

        # Log History
        source.history.append((timestamp, "TRANSFER_OUT", amount, target_id))
        target.history.append((timestamp, "TRANSFER_IN", amount, source_id))
        
        return True

    def get_top_spenders(self, timestamp, n):
        # We need a list of accounts to sort
        # List format: (outgoing_amount, account_id)
        candidates = []

        for acct_id, acct in self.accounts.items():
            # Only consider accounts that have sent money? 
            # Usually the prompt implies all accounts, but 0 spenders are at the bottom.
            candidates.append((acct.total_outgoing, acct.id))

        # Sort Logic:
        # Primary: Amount Descending (we use -x for min-heap style or just reverse=True)
        # Secondary: ID Ascending (alphabetical)
        # Python's sort is stable. To mix Descending/Ascending, the cleanest way is a key:
        candidates.sort(key = lambda x: (-x[0], x[1]))

        return candidates



