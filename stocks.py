#Stocks
class Stock:
    def __init__(self, symbol, quantity, buy_price):                    #initializer
        self.symbol = symbol
        self.quantity = quantity
        self.buy_price = buy_price
        self.current_price = buy_price

    def market_value(self):                                             #current amount of money held in portfolio
        return self.quantity * self.current_price
    
    def profit_loss(self):                                              #how much we gained/lossed based on market
        return (self.current_price - self.buy_price) * self.quantity