def enter(str):
    from fractions import Fraction
    expression = str.split()
    if expression[1] == '+':
        return Fraction(expression[0]) + Fraction(expression[2])
    elif expression[1] == '*':
        return Fraction(expression[0]) * Fraction(expression[2])
    elif expression[1] == '-':
        return Fraction(expression[0]) - Fraction(expression[2])
    elif expression[1] == '/':
        return Fraction(expression[0]) / Fraction(expression[2])
    elif expression[1] == '**':
        return Fraction(expression[0]) ** int(expression[2])
    else:
        pass  # Дописать exeption
