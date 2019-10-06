import simpleExpressions


def mainLoop():
    print('1 - expression in Postfix')
    print('2 - some other shit')
    print('exit - close app')
    operation = input()
    if operation == '1':
        print('Enter the expression:')
        expression = list(map(str, input().split()))
        print(simpleExpressions.Calculate(expression).calculate())
    elif operation == '2':
        pass
    elif operation == 'exit':
        exit()
    else:
        pass


mainLoop()
