inp = 'A1B12C33' 
count_inp = len(inp)

m = 0
freq = ''


def strtointeger(y):
    ans = 0
    for i in range(len(y)):
        ans += int(y[i])*10**(len(y)-(i+1))
    return ans

def nooftime_printchartimes(i,f):
    print(i*f)
    


while m+1 < count_inp:
    
    if m+1 == count_inp-1:
        freq += inp[m+1]
        nooftime_printchartimes(inp[(m-len(freq))+1],strtointeger(freq))
        
    elif ord(inp[m+1]) in range(48,58):
        freq += inp[m+1]
        
    else:
        nooftime_printchartimes(inp[m-len(freq)],strtointeger(freq))
        freq = ''
    m+=1

