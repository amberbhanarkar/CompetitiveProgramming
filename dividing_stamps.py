import sys
import math
N = int(input())
s1 = int((N*(N+1))/2)
C = tuple(map(int,input().split()))
s2 = sum(C)
if s2 == s1:
    print("YES")
else:
    print("NO")

