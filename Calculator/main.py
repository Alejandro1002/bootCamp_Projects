# import
from ASCII_Art import calculatorLogo
from calculator import PythonCalculator
from replit import clear

# python calculator function
def calculatorPythonFunc():
    # print
    print(f' {calculatorLogo} \n')
    print(' WELCOME TO THE PYTHONISTA CALCULATOR ... \n')

    num1 = float(input(' ENTER THE FIRST NUMBER: '))

    mathOperators = {
        '+': 'SUM',
        '-': 'MINUS',
        '*': 'MULTIPLY',
        '/': 'DIVIDE',
        '**': 'POWER OF',
        '%': 'REMINDER OF',
    }

    # flag for while loop
    shouldContinue = True

    while shouldContinue:
        for item in mathOperators:
            print(f'\n [ {item} ]')

        operator = input('\n PLEASE TYPE THE SYMBOL FOR THE MATH OPERATION TO PERFORM: ')

        # declare object
        calculator = PythonCalculator(operator=operator)

        num2 = float(input('\n ENTER THE SECOND NUMBER: '))

        # print result
        result = round(calculator.confirmingOperators(num1=num1, num2=num2), 2)

        print(f'\n THE RESULT OF {mathOperators[operator]} OPERATION IS: [ {result} ] ')

        # continue
        anotherCalculation = input(f'\n WOULD YOU LIKE TO MAKE ANOTHER CALCULATION USING [ {result} ] ?.'
                                   f' TYPE [ Y ] TO CONTINUE. TYPE [ X ] TO PERFORM A FRESH CALCULATION: ').upper()

        if anotherCalculation == 'Y':
            # clear the screen
            clear()
            num1 = result

        else:
            # clear the screen
            clear()
            shouldContinue = False
            calculatorPythonFunc()

calculatorPythonFunc()

