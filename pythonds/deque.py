from collections import deque

a = 'radarq'
b = 'A nut for a jar of tuna'
        
def check_palindrome(s):
    print(s)
    while len(s) > 1:
        if s.pop() == s.popleft():
            continue
        else: return False
    return True



#print(check_palindrome(deque(b.replace(' ','').lower())))

print(deque(''.join(b.split())))
print(list(a))

print(check_palindrome(deque(''.join(b.split()).lower())))