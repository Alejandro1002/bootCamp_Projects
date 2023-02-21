# import
from replit import clear
from ASCII import MACHINE_READY, MACHINE_OFF, MACHINE_LOGO
from coffee_menu import CoffeeMenu
from coffee_maker import CoffeeMaker
from coffee_money import CoffeeMoney

# function
def pythonCoffeeMachine():
    # instance the objects
    coffeeMenu = CoffeeMenu()
    coffeeMaker = CoffeeMaker()
    coffeeMoney = CoffeeMoney()

    # flag for while loop
    shouldContinue = True

    while shouldContinue:

        # print
        print(f'\n {MACHINE_LOGO}')
        print('\n WELCOME TO THE PYTHON COFFEE MACHINE ... ')

        # print choices
        menu = coffeeMenu.gettingCoffeeChoices()
        print(f'\n{menu}')

        # input
        userChoice = input('WHAT COFFEE WOULD YOU LIKE TO CHOOSE?. ').upper()

        # machine options
        if userChoice == 'OFF':
            # clear
            clear()
            print(f'\n {MACHINE_OFF}')
            print('\n THE MACHINE IS OFF DUE TO MAINTENANCE. SORRY FOR THE INCONVENIENCE .... \n')

        elif userChoice == 'REPORT':
            # print reports
            coffeeMaker.printingTheResources()
            coffeeMoney.printingMoneyReport()

        else:
            # user coffee choice
            coffeeChoice = coffeeMenu.findingCoffeeChoice(choice=userChoice)

            # verify ingredients
            if coffeeMaker.verifyingResources(choice=coffeeChoice):

                # process payment
                if coffeeMoney.processingPaymentReceived(cost=coffeeChoice.price):
                    # prepare the coffee
                    # clear
                    clear()
                    print(f'{MACHINE_READY} \n')
                    coffeeMaker.preparingCoffee(choice=coffeeChoice)

        # ask to continue
        newOrder = input(
            '\n WOULD YOU LIKE TO PREPARE A NEW COFFEE?. TYPE [ Y ] TO CONFIRM. TYPE [ X ] TO EXIT. '
        ).upper()

        if newOrder == 'Y':
            # clear
            clear()
            # recursive function
            pythonCoffeeMachine()

        else:
            # clear
            clear()
            shouldContinue = False
            print(f'{MACHINE_OFF}\n')
            print(' THANK YOU FOR USING PYTHON COFFEE MACHINE PROGRAM. GOOD BYE ..... \n')

# call the function
pythonCoffeeMachine()










