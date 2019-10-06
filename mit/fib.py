import time

start = 0
def fib_recursion(n):
    start = time.process_time()
    if n <=2:  return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)
    
#print(fib_recursion(40), time.process_time() - start)


memo = {}
memo_start = 0
def fib_memoize(n):
    memo_start = time.process_time()
    res = 0
    if n in memo: return memo[n]
    elif n <=2: res = 1
    else:
        res = fib_memoize(n-1) + fib_memoize(n-2)
        memo[n] = res
    return res

print(fib_memoize(40), time.process_time() - memo_start)