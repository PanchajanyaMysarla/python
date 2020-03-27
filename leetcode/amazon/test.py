"""
Postfix to infix 
Merge overlapping arrays type 
Merging k sorted lists
"""

"""
Input : abc++
Output : (a + (b + c))

Input  : ab*c+
Output : ((a*b)+c)
"""
    
def postFixToInfix(s):
    stack = []
    
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            stack.append(i)
        else:
            
            x = stack.pop()
            y = stack.pop()
            stack.append('('+y+i+x+')')
    print(stack[0])
    
postFixToInfix('abc++')
postFixToInfix('ab*c+')
postFixToInfix('ab*')
    
    
    