alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# threeD =[['',''],['',''],['','']]
#o/p:
# threed_arr = [['ABC','DEF'],['GHI','JKL'],['MNO','PQR']]
index = 0
n = 6 #rowXcol
row = 2
col = 3
sli = 3
threeD =[['',''],['',''],['','']]

for i in range(sli):# i = 0,1,2
    li = ['','']
    for j in range(row):# j = 0,1
        str2 = ''
        for k in range(col):# k = 0,1,2
            str2 += alp[index]
            index += 1
        li[j] = str2
    threeD[i] = li

print(threeD)
    
