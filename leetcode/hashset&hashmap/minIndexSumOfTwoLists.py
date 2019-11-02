"""
Minimum Index Sum of Two Lists
Solution
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
"""

l1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
l2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

l3 =["Shogun", "Tapioca Express", "Burger King", "KFC"]
l4 =["KFC", "Shogun", "Burger King"]

l5 = ["Shogun","Tapioca Express","Burger King","KFC"]
l6 = ["KFC","Burger King","Tapioca Express","Shogun"]

def findRestaurant(list1, list2):
    maxSum = 2001
    final = {}
    
    if len(list1) > len(list2):
        shorter = list2
        longer = list1
    else:
        shorter = list1
        longer =list2
        
    shorter_map = {}
    
    for i in range(len(shorter)):
        shorter_map[shorter[i]] = i
    print(shorter_map)
        
    for j in range(len(longer)):
        if longer[j] in shorter_map:
            total = shorter_map[longer[j]] + j
            if total <=  maxSum:
                final[longer[j]]= total
                maxSum = total
    print(list(final.keys()))
    return list(final.keys())
    
            
            
        

print(findRestaurant(l5,l6))
        