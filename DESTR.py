T = int(input())
for i in range(0,T):
    k = int(input())
    z = 'zyxwvutsrqponmlkjihgfedcba'
    j = k//25
    l = k%25
    i = l
    while i>=0 and l!=0:
        print(chr(97+i),sep='',end='')
        i-=1
    while j>0:
        print(z,sep='',end='')
        j = j-1
    print('',end='\n')
        
    
