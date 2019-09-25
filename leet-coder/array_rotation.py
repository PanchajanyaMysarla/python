# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


arr = [1,2,3,4,5,6,7] 
k = 3

def array_rotate(arr,k):
    return arr[k:] + arr[:k]

res = array_rotate(arr,k)
print(res)




