def plusOne(nums):
    
    f = []
    carry = 1

    for i in range(len(nums)-1,-1,-1):
        total = nums[i] + carry
        f.append(total%10)
        carry = total//10
    if carry == 1:
        f.append(carry)
    return f[::-1]
    
print(plusOne([1,2,3]))

print(plusOne([9,9,9]))
