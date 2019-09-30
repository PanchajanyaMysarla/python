pars = { ']':'[', '}':'{',')':'('}

store = []

expr = '{[()]})'
expr = ')('
expr = '[(])'

def bal_par():    
    for i in expr:
        if i in pars.values():
            store.append(i)
        elif len(store) != 0 and pars[i] == store[len(store)-1]:
            store.pop()
        else:
            return False
    return len(store) == 0 

print(bal_par())


     
        