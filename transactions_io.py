import csv
from transactions import Transaction
from finance_tracker import FinanceTracker

class Transactions_io:
    @staticmethod
    def save_transactions(finance_tracker, filename="transactions.csv"):
        with open(filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Date', 'Amount','Category', 'Description'])
            for finance in finance_tracker.transactions:
                csv_writer.writerow([finance.date, finance.amount, finance.category, finance.description])
    
    @staticmethod
    def load_transactions(filename="transactions.csv"):
        finance_tracker = FinanceTracker()
        try:
            with open(filename, mode='r',encoding='utf8') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    if not row:
                        continue
                    date, amount, category, description = row
                    amount = float(amount)
                    transaction = Transaction(date, amount, category, description)
                    finance_tracker.add_transaction(transaction)
        except FileNotFoundError:
            pass
        return finance_tracker