T = int(input())
'''for i in range(0,T):
    M, N = map(int,input().split())
    F = list(map(int,input().split()))
    P = list(map(int,input().split()))
    aa = max(F)
    cost = [0 for i in range(0,aa)]
    for i in range(0,len(F)):
        cost[F[i]-1]+=P[i]
    #print(cost)
    cost = set(cost)
    cost = sorted(cost)
    print(cost[0])'''
for i in range(0,T):
    M, N = map(int,input().split())
    F = list(map(int,input().split()))
    P = list(map(int,input().split()))
    if M==1:
        print(P[0])
    else:
        print(min(P))
