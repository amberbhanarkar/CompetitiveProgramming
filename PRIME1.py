def prime(m,n):
	lis=[]
	for i in range(m,n+1): 
		if i > 1: 
			for j in range(2, i): 
				if (i % j) == 0: 
					break
			else: 
				lis.append(i)
	return lis

lis1=[]
lis2=[]	
T = int(input())
for i in range(0,T):
	m, n = map(int,input().split())
	j = prime(m,n)
	j.sort()
	for i in range(0,len(j)):
		if j[i]>=m and j[i]<=n:
			lis2.append(j[i])
	print('\n'.join(map(str, lis2))) 
	j=[]
	lis2=[]
