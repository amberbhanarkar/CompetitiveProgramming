N1, N2, N3 = map(int,input().split())
count = 0
import math
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
lis3 = list(map(int,input().split()))
sorted(lis1)
sorted(lis2)
sorted(lis3)
lis4 = []
for i in range(0,N1):
    if lis1[i] in lis2:
        lis4.append(lis1[i])
    elif lis1[i] in lis3:
    	lis4.append(lis1[i])
for i in range(0,N2):
    if lis2[i] in lis3:
        lis4.append(lis2[i])
    elif lis2[i] in lis1:
    	lis4.append(lis2[i])
for i in range(0,N3):
    if lis3[i] in lis2:
        lis4.append(lis3[i])
    elif lis3[i] in lis1:
    	lis4.append(lis3[i])
s = set(lis4)
print(len(s))
print(s)
        
