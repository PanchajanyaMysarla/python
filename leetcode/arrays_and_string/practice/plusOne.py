nums = [1,2,3]
n2= [9,9]
n3= [8,9,9,9]


s =[str(n) for n in n2]
print(list(str(int(''.join(s))+1)))

def plusOne(nums):
    final = []
    carry = 0
    total = 0
    
    for i in range(len(nums)-1,-1,-1):
        print(i)
        total =  nums[i] + carry
        if i == len(nums)-1:
            total +=1
        
        if total == 10:
            carry = 1
            final.append(0)
        else:
            carry =0
            final.append(total)
        
    if carry != 0:
        final.append(carry)
            
    print(final[::-1])
        
print(plusOne(n3))