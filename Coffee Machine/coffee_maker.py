# import

# class
class CoffeeMaker:

    # attributes
    def __init__(self):
        self.resources = {
            "WATER": 1050,
            "MILK": 850,
            "COFFEE": 350
        }

    # methods

    # printing the resources
    def printingTheResources(self):
        print('\n AVAILABLE RESOURCES \n')
        print(f' WATER: {self.resources["WATER"]} ML')
        print(f' MILK: {self.resources["MILK"]} ML')
        print(f' COFFEE: {self.resources["COFFEE"]} G')

    # verifying resources
    def verifyingResources(self, choice):
        canPrepareCoffee = True
        for item in choice.ingredients:
            if choice.ingredients[item] > self.resources[item]:
                print(f'\n SORRY BUT THERE IS NO ENOUGH {item.upper()} TO PREPARE YOUR COFFEE. \n')
                canPrepareCoffee = False

        return canPrepareCoffee

    # prepare coffee
    def preparingCoffee(self, choice):
        for item in choice.ingredients:
            self.resources[item] -= choice.ingredients[item]

        print(f'\n HERE IS YOUR {choice.name.upper()}! PLEASE ENJOY ..... \n')
