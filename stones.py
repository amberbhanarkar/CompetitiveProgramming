T= int(input())
for i in range(0,T):
    J = str(input())
    S = str(input())
    count = 0
    j = 0
    for j in S:
        if j in J:
            count = count + 1
    print(count)
    
    
    

