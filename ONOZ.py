T = int(input())
for i in range(0,T):
    H, M = map(int,input().split())
    #double digit
    cnt=1
    for j in range(0,9):
        if j<M and i<H:
            cnt = cnt+1
        if j*11<H and i<M:
            cnt = cnt+1
        if i<H and i*11<M:
            cnt = cnt+1
        if i*11<H and i*11<M:
            cnt = cnt+1
    print(cnt)
