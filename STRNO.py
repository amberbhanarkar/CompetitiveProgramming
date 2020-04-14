import math 
from functools import reduce 
def primeFactors(n): 
    lis = []  
    while n % 2 == 0: 
        lis.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0:
            lis.append(i)
            n = n // i 
    if n > 2: 
        lis.append(n)
    return lis

T = int(input())
for i in range(0,T):
    X, K = map(int,input().split())
    for j in range(2,2**20):
        a = 0
        a = primeFactors(j)
        print(a)
        flag = 0
        if len(a)==K:
            for i in range(0,len(a)):
                a[i]+=1
            result1 = reduce((lambda x, y: x * y), a)
            print(result1)
            if result1==X:
                flag = 1
                #print(1)
                break
            else:
                flag = 0
        else:
            flag = 0
    if flag==1:
        print(1)
    else:
        print(0)
 
