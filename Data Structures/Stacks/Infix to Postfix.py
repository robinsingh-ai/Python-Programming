"""
Author : Robin Singh
INFIX TO POSTFIX USING STACKS
"""
from Sstacks import Stack
def oper(char):
    return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z'))

def pr(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char  == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1

def infixToPostfix(Exp, Stack):
    postFix = []
    for i in range(len(Exp)):
        if (oper(Exp[i])):
            postFix.append(Exp[i])
        elif(Exp[i] == '('):
            Stack.push(Exp[i])
        elif(Exp[i] == ')'):
            top = Stack.pop()
            while(not Stack.isEmpty() and top != '('):
                postFix.append(top)
                top = Stack.pop()
        else:
            while (not Stack.isEmpty()) and (pr(Exp[i]) <= pr(Stack.tos())):
                postFix.append(Stack.pop())
            Stack.push(Exp[i])

    while(not Stack.isEmpty()):
        postFix.append(Stack.pop())
    return ' '.join(postFix)

if __name__ == '__main__':
    # for example = a+c+d*(c/r)+a-b+(a(a*b))
    itop = input("Entre your Infix Expression")
    itop = [i for i in itop]
    print("infix expression",' '.join(itop))
    a=Stack()
    print('Postfix exp',infixToPostfix(itop,a))
