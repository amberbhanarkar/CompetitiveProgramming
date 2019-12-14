T = int(input())
for i in range(0,T):
    N = int(input())
    A = list(map(int,input().split()))
    a = A.count(2)
    b = A.count(0)
    asum = (a*(a-1))/2
    bsum = (b*(b-1))/2
    su = int(asum+bsum)
    print(su)
