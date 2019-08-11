T = int(input())
lis = []
lisA = []
lisB = []
A = []
B = []
for i in range(0,T):
	N = int(input())
	lisA = list(map(int,input().strip().split()))[:N] 
	lisB = list(map(int,input().strip().split()))[:N] 
	for i in range(0,N):
		diff = lisA[i]*20-lisB[i]*10
		if diff<0:
			diff = 0
			lis.append(diff)
		lis.append(diff)
	print(max(lis))
	lisA = []
	lisB = []
	lis = []
