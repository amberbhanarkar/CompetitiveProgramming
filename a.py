T = int(input())
for i in range(0,T):
    K = int(input())
    for j in range(K+1,9999):
        if K%j==0:
            print(j)
            break
        
