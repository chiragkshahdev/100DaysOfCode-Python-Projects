class MoneyMachine:
    CURRENCY = "₹"
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def make_payment(self, cost):
        print(f"Please pay {self.CURRENCY}{cost}")
        self.money_received = float(input(f"Inserted {self.CURRENCY}: "))
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change:
                print(f"Here is {self.CURRENCY}{change} change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Not enough money. Refunded.")
            self.money_received = 0
            return False