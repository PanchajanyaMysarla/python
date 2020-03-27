
def search(arr,n,x):
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return -1


arr= [1,2,3,4,5]
x=4
n = len(arr)

result  = search(arr,n,x)

if result == -1:
    print('El is not found')
else: 
    print('El found at index',result)