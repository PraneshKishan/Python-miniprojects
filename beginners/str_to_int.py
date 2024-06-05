def strtointeger(y):
    ans = 0
    for i in range(len(a)):
        ans += int(a[i])*10**(len(a)-(i+1))
    print(ans)
        
a = str(input("Enter you Number as string: "))
strtointeger(a)
