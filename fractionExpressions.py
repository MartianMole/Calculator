from fractions import Fraction


class Calculate:
    def __init__(self, expression):
        self.expression = expression

    @staticmethod
    def Error():  # В случае неверного ввода выражения
        return 'Error'

    def calculate(self):
        expression = self.expression
        if expression[1] == '+':
            return Fraction(expression[0]) + Fraction(expression[2])
        elif expression[1] == '*':
            return Fraction(expression[0]) * Fraction(expression[2])
        elif expression[1] == '-':
            return Fraction(expression[0]) - Fraction(expression[2])
        elif expression[1] == ':':
            return Fraction(expression[0]) / Fraction(expression[2])
        elif expression[1] == '**':
            return Fraction(expression[0]) ** int(expression[2])
        else:
            Calculate.Error()

