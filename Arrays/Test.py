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
        self.data = {}

    def credit(self, acntId, timestamp, amount):
        if acntId not in self.data:
            self.data[acntId] = []
        self.data[acntId].append({"timestamp": timestamp, "amount": amount})


    def debit(self, acntId, timestamp, amount):
        x = {}
        if acntId not in self.data:
            self.data[acntId] = []
        self.data[acntId].append({"timestamp": timestamp, "amount": -1*amount})

    def current(self, acntId):
        amount=0
        if acntId in self.data:
            for item in self.data[acntId]:
                amount += item["amount"]
        return amount

    def balanceChange(self,acntId, start, end):
        acnt = self.data[acntId]
        amnt = 0
        for item in acnt:
            if item["timestamp"]>=start and item["timestamp"]<=end:
                amnt += item["amount"]
        return amnt


b = Bank()
b.credit(1, 5, 10)
b.credit(1,6,1)
b.credit(1,7,2)
b.debit(1,8,4)
b.credit(1,15,5)

print(b.current(1))
print(b.balanceChange(1,0,10))





