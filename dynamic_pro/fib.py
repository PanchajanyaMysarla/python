# 1,1,2,3,5,8, ...

# Time   2n+1 . O(n) = O(n)

memo = []

def fib(n, memo):
    result=None
    if memo[n] != None:
        result = memo[n]
    if n ==1 or n ==2:
        result = 1
    else:
        result = fib(n-1,memo) + fib(n-2,memo)
        memo[n] = result
    return result


def dyn_pro(n):
    memo = [None] * (n+1)
    print(fib(n,memo))
    
dyn_pro(6)




def fib_bottom_up(n):
    if n ==1 or n ==2:
        result = 1
    bottom_up = [None] * (n+1)
    bottum_up[1] = 1
    bottom_up[2] = 1
    for i in range(3,n):
        bottom_up[i] = bottom_up[i-1] + bottum_up[i-2]
    
    return bottom_up[n]

    