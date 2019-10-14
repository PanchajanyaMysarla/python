# Input: nums = [3, 6, 1, 0]
# Output: 1

nums = [3, 6, 1, 0]

twice = [x+x for x in nums]

#print(twice)

for i in range(len(nums)):
    ranger = nums[:i] + nums[i+1:]
    #print(ranger)
    if nums[i] >= max(ranger):
        #print(i)
        break
   
   
m = max(nums)
print(m)

l = [m >= 2*x for x in nums if x!=m]
print(l)

if all(l):
    print(nums.index(m))
    


