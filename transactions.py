#Transaction class

class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date                    #date
        self.amount = amount                #amount (positive for income, negative for expense)
        self.category = category            #category (food, subscription, bills)
        self.description = description      #description about the transaction