T = int(input())
l = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,T):
    N = int(input())
    for j in range(0,N):
        p, s=map(int,input().split())
        if (p>0 and p<9)and s>l[p-1]:
            l[p-1]=s
    print(sum(l))
    l=[0,0,0,0,0,0,0,0,0,0,0]
