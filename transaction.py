class Transaction:
    def __init__(self, name, symbol, amount, date, category):
        self.name = name
        self.symbol = symbol
        self.amount = amount
        self.date = date
        self.category = category


class Wallet:
    def __init__(self, balance):
        self.balance = 0

new_transaction = Transaction("sandwich", "+", "54", "14/03/2022", "food")
