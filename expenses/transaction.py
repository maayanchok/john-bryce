class Transaction:
    def __init__(self, name, symbol, amount, date, category):
        self.name = name
        self.symbol = symbol
        self.amount = amount
        self.date = date
        self.category = category


class Wallet:
    def __init__(self, balance, transaction):
        self.balance = 0



transactions = []

def new_transaction():
    "creates object based on inputs and append to transactions list"
    name = input("name")
    symbol = input("symbol")
    amount = input("amount")
    date = input("date")
    category = input("category")
    new_tran = Transaction(name, symbol, amount, date, category)
    transactions.append(new_tran)
    return transactions

response = ""
while response !="n":
    new_transaction()
    response = input("do you want to add a transaction?  y/n ")

