n = 5
cons = 0
itera = 1

def sum(x,c,i):
    c = c + i
    if i >= x:
        return c
    else:
        return sum(x,c,i+1)
    

o = sum(n,cons,itera)
print(o)
