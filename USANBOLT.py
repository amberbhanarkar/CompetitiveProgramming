import math
T = int(input())
for i in range(0,T):
    A,B,C,D = map(int,input().split())
    t1 = A/D
    s1 = A+B
    t2 = math.sqrt(2*s1/C)
    if(t1>t2):
        print("Tiger")
    elif(t1<t2):
        print("Bolt")
    else:
        print("Tiger")
