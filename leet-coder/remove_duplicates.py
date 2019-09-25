def removeDuplicates( nums):
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        print( res)


removeDuplicates([0,0,1,1,1,2,2,3,3,4])