
def infixToPostfix(s):
    
    prec = {}
    prec['*'] =3
    prec['/'] =3
    prec['+'] =2
    prec['-'] =2
    prec['('] = 1
    
    
    opStack = []
    postfixList = []
    
    tokens = s.split()
    
    for token in tokens:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
           postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while token != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while len(opStack) != 0 and prec[opStack[len(opStack)-1]] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.append(token)
    
    while len(opStack) !=0:
        postfixList.append(opStack.pop())
        
    return ''.join(postfixList)
            
 




def infixToPostfix2(s):
    tokens = s.split()
    
    postfix = []
    prec = {}
    prec['*'] =3
    prec['/'] =3
    prec['+'] =2
    prec['-'] =2
    prec['('] =1
    
    opStack = []
    
    for token in tokens:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            postfix.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = opStack.pop()
        else:
            while len(opStack) != 0 and prec[opStack[len(opStack)-1]] >= prec[token]:
                postfix.append(opStack.pop())
            opStack.append(token)
    
    while opStack:
        postfix.append(opStack.pop())
    
    
    return ' '.join(postfix)
                

print(infixToPostfix2("A * B + C * D"))
print(infixToPostfix2("( A + B ) * C - ( D - E ) * ( F + G )"))