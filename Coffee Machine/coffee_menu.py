# import

# class
class MenuItem:

    # attributes for coffee type object
    def __init__(self, name, water, milk, coffee, price):
        self.name = name
        self.price = price
        self.ingredients = {
            "WATER": water,
            "MILK": milk,
            "COFFEE": coffee
        }

# class
class CoffeeMenu:

    # attributes
    def __init__(self):
        self.menu = [
            MenuItem(name='EXPRESSO', price=1.50, water=150, milk=0, coffee=65),
            MenuItem(name='LATTE', price=2.15, water=75, milk=125, coffee=25),
            MenuItem(name='CAPPUCCINO', price=2.50, water=50, milk=100, coffee=40),
            MenuItem(name='MOCKACCINO', price=2.65, water=50, milk=150, coffee=50)
        ]

    # methods
    # getting coffee choices
    def gettingCoffeeChoices(self):
        options = ''
        for item in self.menu:
            options += f' {item.name} \n'

        return options

    # finding the coffee choice
    def findingCoffeeChoice(self, choice):
        for item in self.menu:
            if item.name == choice:
                return item

        print(f'\n {choice.upper()} IS NOT AN AVAILABLE COFFEE CHOICE. PLEASE TRY AGAIN. \n')

