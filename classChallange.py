class Order:
    def __init__(self, username, price, premium):
        self.name = username
        self.price = price
        self.isPremium = premium

    def showStatus(self, status):
        return f"Order is {status} "


order1 = Order("Barry Allen", 400, True)
order2 = Order("John", 100, True)
print(order1.name, order1.price, order1.showStatus("processing"))
print(order2.name, order2.price, order2.showStatus("shipped"))
