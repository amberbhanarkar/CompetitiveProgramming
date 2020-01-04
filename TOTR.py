T, M = map(str,input().split())
c = M.upper()
M = M+c
A = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
T = int(T)
for i in range(0,T):
    S = input()
    for i in S:
        if i!='_':
            a = A.index(i)
            print(M[a], end='')
        else:
            print(' ',end='')
    print()
    
