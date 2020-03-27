arr =[7,1,5,3,6,4]

arr2= [1,2,3,4,5]

arr3 = [7,6,4,3,1]

def buy_and_sell(arr):
    profit = 0
    for i in range(0,len(arr)-1):
        print(i,arr[i])

        if(arr[i] < arr[i+1]):
            profit +=  arr[i+1] - arr[i]

    return profit

res = buy_and_sell(arr3)

print('profit',res)