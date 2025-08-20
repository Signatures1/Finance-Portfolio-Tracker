import csv
from stocks import Stock
from portfolio import Portfolio

class Portfolio_io:
    @staticmethod
    def save_portfolio(portfolio, filename="stocks.csv"):
        with open(filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Symbol', 'Quantity','Buy_Price', 'Current_Price'])
            for stock in portfolio.portfolio:
                csv_writer.writerow([stock.symbol, stock.quantity, stock.buy_price, stock.current_price])
    
    @staticmethod
    def load_portfolio(filename="stocks.csv"):
        portfolio = Portfolio()
        try:
            with open(filename, mode='r',encoding='utf8') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    if not row:
                        continue
                    symbol, quantity, buy_price, current_price = row
                    quantity = int(quantity)
                    buy_price = float(buy_price)
                    current_price = float(current_price)
                    stock = Stock(symbol, quantity, buy_price)
                    stock.current_price = current_price
                    portfolio.add_stock(stock)
        except FileNotFoundError:
            pass
        return portfolio