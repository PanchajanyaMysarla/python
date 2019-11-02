nums =  [1,1,0,1,1,1]


def maxOnes(nums):
    max_ones,k =0,0
    for i in nums:
        if i == 1:
            k+=1
        else:
            max_ones = max(k,max_ones)
            k = 0
    return max(max_ones,k)


print(maxOnes(nums))