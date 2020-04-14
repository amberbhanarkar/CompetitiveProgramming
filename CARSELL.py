T = int(input())
for i in range(0,T):
    N = int(input())
    P = list(map(int,input().split()))
    P = sorted(P)
    P = P[::-1]
    su = 0
    for j in range(0,N):
        P[j]-=j
        if P[j]>0:
            su+=P[j]
        else:
            continue
        #su += P[j]
        #print(P[j])
    res = su%1000000007
    print(res)
