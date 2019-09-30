
b = '23*54*+9-'

li = []


for i in b:
    if i.isdigit():
        li.append(i)
    else:
        op1 = li.pop()
        op2 = li.pop()
        res =  str(eval(op2 +i+ op1))
        li.append(res)
print(li.pop())
        