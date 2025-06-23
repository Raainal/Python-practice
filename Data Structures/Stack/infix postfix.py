def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack=[]
    output=[]
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char=='(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = ''.join(['(' if c == ')' else ')' if c == '(' else c for c in expression])
    postfix = infix_to_postfix(expression)
    return postfix[::-1]

if __name__ == "__main__":
    expr = "a+b*(c^d-e)"
    print("Infix:   ", expr)
    print("Postfix: ", infix_to_postfix(expr))
    print("Prefix:  ", infix_to_prefix(expr))