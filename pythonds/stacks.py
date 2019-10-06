s = 'hello'

li = list(s)

rev =[]

while len(li) >0:
    rev.append(li.pop())
    
    
print(li,rev)





"""
Number to Binary
"""

def num_to_binary(num):
    rems = []
    while num > 0:
        rem = num % 2
        rems.append(rem)
        num = num // 2
        
    return ''.join([str(x) for x in rems[::-1]])

print(num_to_binary(100))