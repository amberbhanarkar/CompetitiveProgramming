'''import math

T = int(input())
for i in range(0,T):
    N = int(input())
    A = list(map(int,input().split()))
    lis = ''.join(map(str, A))
    sz = len(lis)
    cnt = 0
    for i in range(0,sz):
        product = 1
        for j in range(i,sz):
            product *= ord(lis[j])-ord('0')
            if product%4!=2:
                cnt+=1
    print(cnt)
'''
import itertools

def allSubArrays(xs):
    n = len(xs)
    indices = list(range(n+1))
    for i,j in itertools.combinations(indices,2):
        yield xs[i:j]
        
a = list(allSubArrays([2,3, 4, 5]))

     
