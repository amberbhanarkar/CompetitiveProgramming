T = int(input())
for i in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	left = 0
	right = 0
	L = []
	for j in range(0,N):
		if j%2==0:
			L.append(A[N-left-1])
			left+=1
		else:
			L.append(A[right])
			right+=1
	print(L)
