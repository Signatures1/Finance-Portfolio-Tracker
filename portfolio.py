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

#portfolio    
class Portfolio:
    def __init__(self):                                                 #initializer for stock list
        self.portfolio = []
    
    def add_stocks(self, stock):                                        #add stocks to the list                    
        self.portfolio.append(stock)
    
    def calculate_total_loss(self):                                     #total loss
        loss = 0
        for stock in self.portfolio:
            loss += stock.profit_loss()
        return loss

    def calculate_total_value(self):                                    #total gain
        profit = 0
        for stock in self.portfolio:
            profit += stock.market_value()
        return profit
    
    def categorize_stock(self):                                         #sorting/organizing stocks
        different_stocks = {}                                           #library for org
        for stock in self.portfolio:
            if stock.symbol not in different_stocks:
                different_stocks[stock.symbol] = {
                    "shares" : stock.quantity,                          #sorts by name and puts in amount of one specific stock and the total value for that stock that we own
                    "value" : stock.market_value()
                }
            else:
                different_stocks[stock.symbol]["shares"] += stock.quantity
                different_stocks[stock.symbol]["value"] += stock.market_value()
        return different_stocks