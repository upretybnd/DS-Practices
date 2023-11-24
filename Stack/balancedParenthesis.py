def is_parenbalanced(exp):
    stack = []
    ob = "[{("
    cb = ")}]"
    bracket = {')': '(', '}': '{', ']': '['}
    for each in exp:
        if each in ob:
            stack.append(each)
        elif each in cb:
            if not stack or stack.pop() != bracket[each]:
                return False
    return not stack


exp = "[{})()}]"
if is_parenbalanced(exp):
    print("Balanced")
else:
    print("Not Balanced")
