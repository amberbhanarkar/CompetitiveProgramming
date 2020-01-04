import math
def agcd(x,y):
    while(y):
        x,y=y,x%y
    return x
T = int(input())
for i in range(0,T):
    N = int(input())
    A = list(map(int,input().split()))
    n1 = A[0]
    n2 = A[1]
    gcd = agcd(n1,n2)
    for i in range(2,len(A)):
        gcd = agcd(gcd,A[i])
    print(gcd)
    A = []
