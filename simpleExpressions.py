import math


def infToPost(expressionInInfix):  # Функция преобразования инфикса в постфикс
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    postfixList = []
    tokenList = expressionInInfix
    opStack = []
    for token in tokenList:
        if token in "0123456789":
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

    def calculate(self):  # Считает выражение в постфиксной форме
        expressionInPostfix = infToPost(self.expressionInInfix)  # Преобразовываем инфикс в постфикс
        stack = []
        for i in expressionInPostfix:
            if i == '+':
                if len(stack) > 1:
                    stack.append(stack.pop() + stack.pop())
                else:
                    Calculate.Error()
            elif i == '*':
                if len(stack) > 1:
                    stack.append(stack.pop() * stack.pop())
                else:
                    Calculate.Error()
            elif i == '-':
                if len(stack) > 1:
                    x = stack.pop()
                    stack.append(stack.pop() - x)
                else:
                    Calculate.Error()
            elif i == '/':
                if len(stack) > 1:
                    x = stack.pop()
                    stack.append(stack.pop() / x)
                else:
                    Calculate.Error()
            elif i == 'cos':
                if len(stack) > 0:
                    x = stack.pop()
                    stack.append(math.cos(x))
                else:
                    Calculate.Error()
            elif i == 'sin':
                if len(stack) > 0:
                    x = stack.pop()
                    stack.append(math.sin(x))
                else:
                    Calculate.Error()
            elif i == 'sqrt':
                if len(stack) > 0:
                    x = stack.pop()
                    stack.append(math.sqrt(x))
                else:
                    Calculate.Error()
            elif i == 'abs':
                if len(stack) > 0:
                    x = stack.pop()
                    stack.append(abs(x))
                else:
                    Calculate.Error()
            else:
                stack.append(int(i))
        if len(stack) == 1:
            if type(stack[0]) == int:
                return stack[0]
            else:
                return float('{:.5f}'.format(stack[0]))
        else:
            Calculate.Error()
