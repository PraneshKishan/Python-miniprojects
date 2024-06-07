inp = 'PRANESH'
charlist = list(inp)
n = (len(charlist))

for i in range(n-1):
    for j in range(n-1):
        if charlist[j]>charlist[j+1]:
            charlist[j],charlist[j+1] = charlist[j+1],charlist[j]

sorted_str = ''.join(charlist)
print(sorted_str)
