def plusOne(digits):
    final = []
    remaining = 0
    for i in range(len(digits)-1,-1,-1):
        total = digits[i] + remaining
        if i == len(digits)-1:
            total += 1
            
        if total >=10:
            remaining = 1
            final.append(0)
        else:
            remaining = 0
            final.append(total)
    if remaining != 0:
        final.append(remaining)
            
    return final[::-1]


def plusOne2(digits):
    
    s = ''.join([str(i) for i in digits])
    print(s)
    i = int(s) + 1
    print(i)
    l = [int(n) for n in str(i)]
    print(l)
    return l
    

def plusOne3(digits):
    final = []
    remaining = 0
    for i in range(len(digits)):
        
        total = digits[len(digits)-1] + remaining
        if i == len(digits)-1:
            total += 1
            
        if total >=10:
            remaining = 1
            final.append(0)
        else:
            remaining = 0
            final.append(total)
    if remaining != 0:
        final.append(remaining)
            
    return final[::-1]
    
print(plusOne2([8,9]))