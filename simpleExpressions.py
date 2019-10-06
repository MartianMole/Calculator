import math
from fractions import Fraction

def infToPost(expressionInInfix):  # Функция преобразования инфикса в постфикс
    prec = {"sin": 3, "sqrt": 3, "cos": 3, "abs": 3, "*": 3, ":": 3, "+": 2, "-": 2, "(": 1}
    postfixList = []
    tokenList = expressionInInfix
    opStack = []
    for token in tokenList:
        if token[0] in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack == []) and \
                    (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)

    while not opStack == []:
        postfixList.append(opStack.pop())
    return postfixList


class Calculate:
    def __init__(self, expressionInInfix):
        self.expressionInInfix = expressionInInfix  # При инициализации получаем инфиксное выражение

    @staticmethod
    def Error():  # В случае неверного ввода выражения
        return 'Error'

    @staticmethod
    def checkFrac(elem):
        return '/' in str(elem)

    @staticmethod
    def myFraction(x):
        if Calculate.checkFrac(x):
            return Fraction(x)
        else:
            return Fraction(str(x))

    def calculate(self):  # Считает выражение в постфиксной форме
        expressionInPostfix = infToPost(self.expressionInInfix)  # Преобразовываем инфикс в постфикс
        stack = []
        fracInExpression = False
        for i in expressionInPostfix:  # Если в выражении есть дробь, все считаем как дроби, а в ответе выводим одно из двух
            if '/' in i:
                fracInExpression = True
                break
        for i in expressionInPostfix:
            if i == '+':
                if len(stack) > 1:
                    x, y = stack.pop(), stack.pop()
                    if fracInExpression:
                        stack.append(Calculate.myFraction(x) + Calculate.myFraction(y))
                    else:
                        stack.append(x + y)
                else:
                    Calculate.Error()
            elif i == '*':
                if len(stack) > 1:
                    x, y = stack.pop(), stack.pop()
                    if fracInExpression:
                        stack.append(Calculate.myFraction(x) * Calculate.myFraction(y))
                    else:
                        stack.append(x * y)
                else:
                    Calculate.Error()
            elif i == '-':
                if len(stack) > 1:
                    x, y = stack.pop(), stack.pop()
                    if fracInExpression:
                        stack.append(Calculate.myFraction(y) - Calculate.myFraction(x))
                    else:
                        stack.append(y - x)
                else:
                    Calculate.Error()
            elif i == ':':
                if len(stack) > 1:
                    x, y = stack.pop(), stack.pop()
                    if fracInExpression:
                        stack.append(Calculate.myFraction(y) / Calculate.myFraction(x))
                    else:
                        stack.append(y / x)
                else:
                    Calculate.Error()
            elif i == 'cos':
                if len(stack) > 0:
                    x = stack.pop()
                    if fracInExpression:
                        stack.append(math.cos(Calculate.myFraction(x)))
                    else:
                        stack.append(math.cos(x))
                else:
                    Calculate.Error()
            elif i == 'sin':
                if len(stack) > 0:
                    x = stack.pop()
                    if fracInExpression:
                        stack.append(math.sin(Calculate.myFraction(x)))
                    else:
                        stack.append(math.sin(x))
                else:
                    Calculate.Error()
            elif i == 'sqrt':
                if len(stack) > 0:
                    x = stack.pop()
                    if fracInExpression:
                        stack.append(math.sqrt(Calculate.myFraction(x)))
                    else:
                        stack.append(math.sqrt(x))
                else:
                    Calculate.Error()
            elif i == 'abs':
                if len(stack) > 0:
                    x = stack.pop()
                    if fracInExpression:
                        stack.append(abs(Calculate.myFraction(x)))
                    else:
                        stack.append(abs(x))
                else:
                    Calculate.Error()
            elif '/' in i:
                stack.append(i)
            else:
                stack.append(int(i))

        if len(stack) == 1:
            if type(stack[0]) == int:
                return stack[0]
            else:
                return stack[0]
                # return float('{:.5f}'.format(stack[0]))
        else:
            Calculate.Error()
