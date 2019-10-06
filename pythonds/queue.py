from collections import deque

def hot_potato(names,n):
    enq = deque(names)
    print(enq)

    while len(enq) > 1:
        for i in range(n):
            enq.append(enq.popleft())
        enq.pop()
    return enq
                
            
print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
