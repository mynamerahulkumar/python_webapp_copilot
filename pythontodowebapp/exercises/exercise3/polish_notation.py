def polish_notation_without_stack(expression):
    expression = expression.split()
    operators = ['+', '-', '*', '/']
    while len(expression) > 1:
        for i in range(1, len(expression) - 1):
            if expression[i] in operators:
                if expression[i] == '+':
                    expression[i] = str(int(expression[i - 1]) + int(expression[i + 1]))
                elif expression[i] == '-':
                    expression[i] = str(int(expression[i - 1]) - int(expression[i + 1]))
                elif expression[i] == '*':
                    expression[i] = str(int(expression[i - 1]) * int(expression[i + 1]))
                elif expression[i] == '/':
                    expression[i] = str(int(expression[i - 1]) / int(expression[i + 1]))
                expression.pop(i - 1)
                expression.pop(i)
                break
    return int(expression[0])