N, Q = map(int,input().split())
lis = []
for i in range(0,N):
    a=0
    lis.append(a)
for i in range(0,Q):
    C, A, B = map(int,input().split())
    if C==0:
        j = A
        for j in range(A,B+1):
            lis[j]=1
    elif C==1:
        print(lis[A:B+1].count(1))
    
