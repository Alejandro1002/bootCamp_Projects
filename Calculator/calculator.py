# calculator class

# class
class PythonCalculator:

    # attributes
    def __init__(self, operator):
        self.selector = operator

    # methods
    def confirmingOperators(self, num1, num2):
        if self.selector == '+':
            return num1 + num2

        elif self.selector == '-':
            return num1 - num2

        elif self.selector == '*':
            return num1 * num2

        elif self.selector == '/':
            return num1 / num2

        elif self.selector == '**':
            return num1 ** num2

        elif self.selector == '%':
            return num1 % num2
