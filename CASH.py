T = int(input())
for i in range(0,T):
    su = 0
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    A = sorted(A)
    su = sum(A)
    print(su%K)
