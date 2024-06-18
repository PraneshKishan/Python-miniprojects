alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

twod_arr = ['ABCDE','FGHIJ','KLMNO','PQRST','UVWXY']

Two_D = ['','','','','']
index = 0
n = 5
for i in range(n):    
    str = ''
    for j in range(n):       
        str += alp[index]
        index+=1
        Two_D[i] = str
        
for i in range(n):
    print(Two_D[i])
