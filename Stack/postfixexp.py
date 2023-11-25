def evaluate(exp):
    stack = []

    def operator(op, op1, op2):
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op1 / op2

    for token in exp:
        if token.isdigit():
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = operator(token, op1, op2)
            stack.append(result)

    return stack[0]


expression = "23*5+"
result = evaluate(expression)
print(f"The result of the postfix expression {expression} is: {result}")
