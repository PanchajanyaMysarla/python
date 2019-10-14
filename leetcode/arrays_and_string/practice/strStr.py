
hay = 'hello'
needle = 'llo'

for i in range(0,len(hay)-len(needle)+1):
    #print(i)
    if hay[i:i+len(needle)] == needle:
        print(hay[i:i+len(needle)])
        print(i)