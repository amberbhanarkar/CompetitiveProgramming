import math
T = int(input())
for i in range(0,T):
    N, D = map(int,input().split())
    if D<=N:
        print("YES")
    else:
        for j in range(1,N):
            print(j+math.ceil((D/j+1)))
            if j+math.ceil((D/j+1)) <=N:
                print("YES")
            else:
                print("NO")
