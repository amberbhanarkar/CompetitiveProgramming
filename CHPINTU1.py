T = int(input())
while T>0:
    N, M = map(int,input().split())
    F = list(map(int,input().split()))
    P = list(map(int,input().split()))
    #l = [2501 for j in range(0,N)]
    l = []
    for j in range(0,100):
        l.append(2501)
    print(l)
    for j in range(0,N):
        l[F[j]-1]=0
    print(l)
    for j in range(0,N):
        l[F[j]-1]+=P[j]
    print(l)
    print(min(l))
    T-=1
