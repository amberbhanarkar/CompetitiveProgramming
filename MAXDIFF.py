import math
W = []
T = int(input())
for i in range(0,T):
    N, K = map(int,input().split())
    W = list(map(int,input().split()))
    a = sorted(W)
    s1 = sum(a[0:K])
    s2 = sum(a[K:])
    s3 = sum(a[:N-K])
    s4 = sum(a[N-K:])
    print(max(s2-s1, s4-s3))
    W = []
    s1 = 0
    s2=0
    s3 = 0
    s4 = 0
