#Tracking all transactions
from transactions import Transaction

class FinanceTracker:
    
    def __init__(self):
        self.transactions = []                  #list for storing transactions
    
    def add_transaction(self, transaction):   #add new entry
        self.transactions.append(transaction)

    def calculate_balance(self):                 #get the current balance by totaling the amount
        total = 0
        for t in self.transactions:
            total += t.amount
        return total
    
    def summarize_by_category(self):              #putting all transactions into seperate categorys for organization
        summary = {}
        for t in self.transactions:
            if t.category in summary:
                summary[t.category] += t.amount
            else:
                summary[t.category] = t.amount
        return summary
