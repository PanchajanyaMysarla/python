"""
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

"""

a = '11'
b = '1'

c = '1010'
d = '1011'

def addBinary( a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
    
    
    
print(addBinary(c,d))