T = int(input())
for i in range(0,T):
    su = 0
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A = sorted(A)
    B = sorted(B)
    for j in range(0,N):
        su += min(A[j],B[j])
    print(su)