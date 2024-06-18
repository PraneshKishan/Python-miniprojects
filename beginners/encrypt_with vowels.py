inp = 'f*ll*w pr*n*sh *nl*n* t* l**rn c*d*ng'

vow = 'aeiou'
cons = 0

for i in range(len(inp)):#pointers - i, x
    if inp[i] == '*':
        x = cons % 5
        cons += 1
        #inp[i] = vow[x]
        inp = inp.replace(inp[i],vow[x],1)
print(inp)
