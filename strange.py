def sieveOfEratosthenes(N, s):  
    prime = [False] * (N+1) 
    for i in range(2, N+1, 2):  
        s[i] = 2
    for i in range(3, N+1, 2): 
        if (prime[i] == False): 
            s[i] = i 
            for j in range(i, int(N / i) + 1, 2): 
                if (prime[i*j] == False): 
                    prime[i*j] = True
                    s[i * j] = i 

def generatePrimeFactors(N): 
    s = [0] * (N+1) 
    sieveOfEratosthenes(N, s) 
    #print("Factor Power")  
    curr = s[N] 
    cnt = 1
    power = []
    count = []
    while (N > 1): 
        N //= s[N] 
        if (curr == s[N]): 
            cnt += 1
            continue
        #print(str(curr) + "\t" + str(cnt))
        power.append((cnt))
        count.append((curr))
        curr = s[N] 
        cnt = 1
    return power,count
#N = 360
#powers,count = generatePrimeFactors(N)
#print(powers,count)

import math
from functools import reduce
T = int(input())
for i in range(0,T):
    X, K = map(int,input().split())
    for j in range(2,2**10):
        a = 0
        a, b = generatePrimeFactors(j)
        #print(a, b)
        #print(b)
        flag = 0
        if len(b)==K:
            for i in range(0,len(a)):
                a[i]+=1
            result1 = reduce((lambda x, y: x * y), a)
            #print(result1)
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

