def resolve(brakets):
    stack = []
    close = [')', ']']

    for braket in brakets:
        if braket in close:
            if braket == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(2)
                elif stack and type(stack[-1]) == int:
                    num = stack.pop()
                    while type(stack[-1]) == int:
                        num += stack.pop()
                    stack.pop()
                    stack.append(num * 2)
            elif braket == ']':
                if stack[-1] == '[':
                    stack.pop()
                    stack.append(3)
                elif stack and type(stack[-1]) == int:
                    num = stack.pop()
                    while type(stack[-1]) == int:
                        num += stack.pop()
                    stack.pop()
                    stack.append(num * 3)
        else:
            stack.append(braket)
    
    return stack

def check(brakets):
    stack = []

    for braket in brakets:
        if braket == '(' or braket == '[':
            stack.append(braket)
        elif braket == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif braket == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    brakets = list(input())
    
    if check(brakets):
        print(sum(resolve(brakets)))
    else:
        print(0)