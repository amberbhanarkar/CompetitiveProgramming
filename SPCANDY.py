T = int(input())
for i in range(0,T):
	N, K = map(int,input().split())
	#N = int(N)
	#K = int(K)
	if N==0:
		print(0,0)
	elif K==0:
		print(0,N)
	else:
		a = int(N/K)
		b = N%K
		print(a,b)
