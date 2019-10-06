li = [2,4,6,10]
llsum =16

#O(n * n)
def sum():
    count =0

    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i]+li[j] == 16:
                count+=1
        
    print(count)
    
sum()