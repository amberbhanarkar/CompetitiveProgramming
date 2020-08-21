T = int(input())
for i in range(0,T):
    count = 0
    k = 0
    A, B = map(int,input().split())
    for j in range(1,A+1):
        for k in range(1,B+1):
            if j*k+j+k == str(j)+str(k):
                count = count +1
    print(count)
