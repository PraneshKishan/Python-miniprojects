inp = 'BAAABBBCCC' #op: A:3, B: 4, C: 3
charlist = list(inp)

n = (len(charlist))

#sorting
for i in range(n-1):
    for j in range(n-1):
        if charlist[j]>charlist[j+1]:
            charlist[j],charlist[j+1] = charlist[j+1],charlist[j]

sorted_str = ''.join(charlist)
print(sorted_str)

#counting the frequncy
no = len(sorted_str)
empty_dict = {}
for i in range(no):
    
    if sorted_str[i] in empty_dict:
        # a = empty_dict[sorted_str[i]]
        empty_dict[sorted_str[i]] += 1
    else:
        empty_dict[sorted_str[i]] = 1

print(empty_dict)

