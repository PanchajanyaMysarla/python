# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

arr=[1,2,3,1]

def contains_duplicate(nums):
    return len(set(nums)) != len(nums)
print(contains_duplicate(arr))