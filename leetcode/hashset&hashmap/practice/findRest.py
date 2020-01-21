list1 =["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

l3 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l4 = ["KFC", "Shogun", "Burger King"]

l5 = ["Shogun","Tapioca Express","Burger King","KFC"]
l6 = ["KFC","Burger King","Tapioca Express","Shogun"]

def findRestaurant( list1, list2):
    d = {}
    res = []
    
    s = float('inf')
    for i in range(len(list1)):
            d[list1[i]] = i
    print(d)
    print(list2)
    for j in range(len(list2)):
        if list2[j] in d:
            total = d[list2[j]] + j
            print('total',total)
            if total < s:
                s = total
                res  = [list2[j]]
            elif total == s:
                s = total
                res.append(list2[j])
    return res
  
print(findRestaurant(l5,l6))
            
    
    
    