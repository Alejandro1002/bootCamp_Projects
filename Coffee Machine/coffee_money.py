# import

# class
class CoffeeMoney:

    # variables
    CURRENCY = '$'
    coinValues = {
        'QUARTERS': 0.25,
        'DIMES': 0.10,
        'NICKLES': 0.05,
        'PENNIES': 0.01
    }

    # attributes
    def __init__(self):
        self.profit = 0
        self.moneyReceived = 0

    # methods

    # printing money report
    def printingMoneyReport(self):
        print(f' MONEY: {self.CURRENCY}{self.profit}')

    # processing the coins
    def processingCoins(self):
        print('\n PLEASE INSERT COINS \n')
        for item in self.coinValues:
            self.moneyReceived += int(input(f' HOW MANY {item.upper()} WANT TO INSERT?. ')) * self.coinValues[item]

        return self.moneyReceived

    # processing payment
    def processingPaymentReceived(self, cost):
        # call function
        self.processingCoins()

        if self.moneyReceived >= cost:
            change = round(self.moneyReceived - cost, 2)
            print(f'\n HERE IS YOUR CHANGE: {self.CURRENCY}{change} \n')
            self.profit += cost
            self.moneyReceived = 0
            return True

        else:
            print('\n NOT ENOUGH MONEY INSERTED TO COVER THE COST. MONEY REFUNDED. \n')
            self.moneyReceived = 0
            return False





