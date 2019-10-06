import simpleExpressions
import fractionExpressions


def mainLoop():
    print('1 - expression in Postfix')
    print('2 - fraction expression')
    print('exit - close app')
    operation = input()
    if operation == '1':
        print('Enter the expression:')
        expression = list(map(str, input().split()))
        print(simpleExpressions.Calculate(expression).calculate())
    elif operation == '2':
        print('Enter the expression:')
        expression = list(map(str, input().split()))
        print(fractionExpressions.Calculate(expression).calculate())
    elif operation == 'exit':
        exit()
    else:
        pass


mainLoop()
