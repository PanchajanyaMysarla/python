"""
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
Example 2:

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
Example 3:

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]
Example 4:

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]
"""
def solution(a, b, target):
    a_dict, b_dict = {}, {}
    for key, value in a:
        a_dict[key] = value

    for key, value in b:
        b_dict[key] = value

    best = target
    best_tuple = list([])
    
    key_combs = [(x, y) for x in list(a_dict.keys()) for y in list(b_dict.keys())]

    for (a_key, b_key) in key_combs:
        if a_dict[a_key]+b_dict[b_key] == target:
            if best == 0:
                best_tuple.append([a_key, b_key])
            else:
                best_tuple = list([[a_key, b_key]],)
            best = target-(a_dict[a_key]+b_dict[b_key])
        elif a_dict[a_key]+b_dict[b_key] < target:
            if target-(a_dict[a_key]+b_dict[b_key]) < best:
                best = target-(a_dict[a_key]+b_dict[b_key])
                best_tuple = ([a_key, b_key])

    return best_tuple

class Solution:
    def optimize(self,a,b,target):
        a.sort(key = lambda x: x[1])
        b.sort(key = lambda x: x[1])
        print(a,b)
        
        l = 0
        r = len(b) -1
        ans = []
        curr_sum = float('inf')
        
        while l < len(a) and r >= 0:
            i,al = a[l]
            j,br = b[r]
            curr_sum = al+br
            if target - al- br == curr_sum:
                ans.append([i,j])
            
            elif al +br <= target and curr_sum > target - al - br:
                ans.clear()
                ans.append([i,j])
                curr_sum = target - al- br
                
            if target > al + br:
                l+=1
            else:
                
                
                
                
            
            
            
        
        print(ans)
        
a = [[1, 2], [2, 4], [3, 6],]
b = [[1, 2]]

s = Solution()
print(s.optimize(a,b,10))
            
