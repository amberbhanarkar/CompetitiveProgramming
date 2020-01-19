T = int(input())
for i in range(0,T):
    su=0
    su1=0
    N = int(input())
    A = list(map(int,input().split()))
    su = sum(A)
    for j in range(0,len(A)):
        if A[j]>0:
            su1=su1+A[j]
    if su==su1:
        print("YES")
    elif su<su1:
        print("NO")
    else:
        print("NO")
