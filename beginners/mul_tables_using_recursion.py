n = 10
times = 20
st = 1
#nx1 nx2 nx3.....
tab = []

def tables(a,b):
    c = a*b
    i = [a,"x",b,'=',c]
    print(a,"x",b,'=',c)
    tab.append(i)
    # print(tab)
    if len(tab)>=times:
        return
    else:
        tables(a,b+1)

tables(n,st)
