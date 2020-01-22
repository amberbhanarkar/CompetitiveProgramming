T = int(input())
for i in range(0,T):
    N, K = map(int,input().split())
    N = N-1
    K = K-1
    B = 1
    if K>N/2:
        K = N-K
    for j in range(0,K):
        B = B*(N-j)
        B = B//(j+1)
    print(B)
