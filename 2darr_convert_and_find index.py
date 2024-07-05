#This Program is About manipulating a string into a 2D Array with user defined row and columns, with an Extra feature of finding the index position of an element from the 2d Array

inp = "search_praneshonline_in_instagram
row = int(input("Enter the row length: "))#3
col = int(input("Enter the column length: "))#3

twoD = [[]*col]*row

index = 0

for i in range(row):
    lst = []
    for j in range(col):
        lst.append(inp[index])
        index += 1
        twoD[i] = lst   
print(twoD)

char = str(input("Enter the character from the array: "))

for i in twoD:
    for j in i:
        if j == char:
            print('x: ',twoD.index(i),'y: ',i.index(j))

