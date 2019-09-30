def has22(nums):
  for i in range(len(nums)-1):
    print(i)
    if nums[i:i+3] == [2,2]:
      return True
  return False


has22([1, 2, 1, 2])

