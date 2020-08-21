'''def type(M,S):
    su = M
    l = []
    for i in range(0,len(S)):
        su - S[j]
        for j in range(0,len(S)):
            su = su-S[i]
            if su>=0:
                l.append(S[j])
    for i in range(0,len(S)):
        su=sum(l)
        S[i]=

M, N = map(int,input().split())
for i in range(0,N):
    S = list(map(int,input().split()))
    type(M,S)
'''
from itertools import permutations
M, N = map(int,input().split())
for i in range(0,N):
    S = list(map(int,input().split()))
l = list(permutations(S))
print(l)