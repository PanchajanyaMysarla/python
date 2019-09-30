


def sum67(nums):
    for i in range(len(nums)):
        if nums[i] == 6:
            nums[i]= 0
            for j in range(i,len(nums)):
                #print('j',j,nums[j])
                if nums[j] == 7:
                    nums[i:j+1]=[0 for i in range(i,j+1)]
                    #print(nums,'nums')
                    break
                    
                
        #print(i,nums)
    print( sum(nums))


#sum67([1, 2, 2]) #→ 5
#sum67([1, 2, 2, 6, 99, 99, 7]) #→ 5
#sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])
#sum67([1, 2, 2, 6, 99, 99, 7])
sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) 
#sum67([1, 1, 6, 7, 2]) #→ 4
