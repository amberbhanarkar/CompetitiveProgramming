T = int(input())
for i in range(0,T):
	N, S = map(int,input().split())
	A = list(map(int,input().split()))
	L = []
	su = 0
	for j in range(0,N):
		if su==S:
			print(0)
		elif su<S:
			L.append(A[j])
			su+=A[j]
		else:
			L.pop(A[0])
	print(L)
