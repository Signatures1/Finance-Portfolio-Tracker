from stocks import Stock

#portfolio    
class Portfolio:
    def __init__(self):                                                 #initializer for stock list
        self.stocks = []
    
    def add_stock(self, stock):                                         #add stocks to the list                    
        self.stocks.append(stock)
    
    def calculate_total_loss(self):                                     #total loss
        loss = 0
        for stock in self.stocks:
            loss += stock.profit_loss()
        return loss

    def calculate_total_value(self):                                    #total gain
        profit = 0
        for stock in self.stocks:
            profit += stock.market_value()
        return profit
    
    def categorize_stock(self):                                         #sorting/organizing stocks
        different_stocks = {}                                           #library for org
        for stock in self.stocks:
            if stock.symbol not in different_stocks:
                different_stocks[stock.symbol] = {
                    "shares" : stock.quantity,                          #sorts by name and puts in amount of one specific stock and the total value for that stock that we own
                    "value" : stock.market_value()
                }
            else:
                different_stocks[stock.symbol]["shares"] += stock.quantity
                different_stocks[stock.symbol]["value"] += stock.market_value()
        return different_stocks