# credit(account_id, timestamp, amount) # Adds value to the given account, recording the timestamp. O(1)

# debit(account_id, timestamp, amount) # Subtracts value from the given account, recording the timestamp. O(1)

# current(account_id) # Returns the current balance. O(1)

# # Returns the net change in account value between the given timestamps.
# # O(log M) M being the number of transactions for the account
# balance_change(account_id, exclusive_start_timestamp, inclusive_end_timestamp)

# credit(1, 5, 10) +
# credit(1, 6, 1) +
# credit(1, 7, 2) +
# debit(1, 8, 4) +
# credit(1, 15, 5) -

# balance_change(1, 0, 10) => 9
# {acntId:currentAmount}
# [{accountId:[{"timestamp":"10","amount": "20","transactionMode":"credit"},{"timestamp":"10","amount": "20","transactionMode":"credit"},{"timestamp":"10","amount": "20","transactionMode":"credit"}]},]
class Bank:
    def __init__(self):
        self.data = []
        self.dicmap = {}

    def credit(self, acntId, timestamp, amount):
        x = {}
        if acntId not in self.data:
            x[acntId] = []
            self.dicmap[acntId] = 0
        self.dicmap[acntId] += amount
        x[acntId].append({"timestamp": timestamp, "amount": amount, "transactionMode": "credit"})


    def debit(self, acntId, timeteststamp, amount):
        x = {}
        if acntId not in self.Data:
            x[acntId] = []
            self.dicmap[acntId] = 0
        x[acntId].append({"timestamp": timestamp, "amount": amount, "transactionMode": "debit"})
        self.dicmap[acntId] -= amount

    def current(self, acntId):
        if acntId in self.dicmap:
            print(self.data)
            return self.dicmap[acntId]
        return 0

    def balanceChange(self,acntId, start, end):
        acnt = self.data[acntId]
        amnt = 0
        for item in acnt:
            if item.transactionMode == "credit":
                amnt += item.amount
            else:
                amnt -= item.amount
        return amnt


b = Bank()
b.credit(1, 5, 10)
print(b.current(1))




