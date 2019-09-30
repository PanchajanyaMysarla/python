a = '1+2*3'

operands =[]
operators = []


for i in a:
    if i.isdigit():
        operands.append(i)
    else:
        operators.append(i)
        
print(operands,operators)

while True:
    if len(operators) == 0 or len(operands) == 0:
        break
    op1 = operands.pop()
    op2 = operands.pop()
    op = operators.pop()
    res = str(eval(op1+op+op2))
    operands.append(res)
    
print(operands,operators,postfix)