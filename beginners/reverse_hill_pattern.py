#reverse hill pattern

#'n' refers to the no. of rows and columns
n = 3

for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
      
    for k in range(i,n-1):
        print("*",end=' ')
      
    for l in range(i,n):
        print("*",end=' ')
      
    print()
