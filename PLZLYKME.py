T = int(input())
for i in range(0,T):
    L,D,S,C = map(int,input().split())
    if D==1:
        if L>=S:
            print("ALIVE AND KICKING")
        else:
            print("DEAD AND ROTTING")     
    else:
        day = S
        result = 0
        for j in range(1,D):
            day = day*(1+C)
            #S = a
            if day>=L:
                print("ALIVE AND KICKING")
                result=1
                break
        if result==0:
            print("DEAD AND ROTTING")
