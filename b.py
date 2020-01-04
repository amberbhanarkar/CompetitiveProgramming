N, Q = map(int,input().split())
lis = []
for i in range(0,N):
    lis.append(0)
for i in range(0,Q):
    lis1 = []
    A, B, C = map(int,input().split())
    if A==0:
        lis1 = lis[B:C+1]
        for j in range(B,C):
            if lis1[j]==1:
                lis1[j]=0
            else:
                lis1[j]=1
            lis[j]=lis1[j]
        print(lis)
    elif A==1:
        lis1 = lis[B:C+1]
        a = lis1.count(1)
        print(a)
    
