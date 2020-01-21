"""
Add Binary
Solution
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
a = "11"
b = "1"

a1 = "1010"
b1 = "1011"

def addBinary(a, b):
    
    res = []
    carry = 0
    i=0
    j=0
    
    if len(a) > len(b):
        short = b
        longer = a
    else:
        short = a
        longer = b
        
    
    for i in range(len(short)-1,-1,-1):
        
        total = int(short[i])+int(longer[i]) + carry
        
        if total < 2:
            res.append(str(total))
            carry = 0
        
        else:
            carry = 1
            res.append('0')
            
    for j in range(len(longer)-1,len(short)-1,-1):
        total = int(longer[j]) + carry
        if total <2:
            res.append(str(total))
            carry =0
        else:
            carry =1
            res.append('0')
        
    if carry ==1:
        res.append(str(carry))
    
    return ''.join(res[::-1])
print(addBinary(a1,b1))