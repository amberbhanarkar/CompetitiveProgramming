T = int(input())
j = 0
k = 0
cnt1=0
cnt2=0

for i in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	N = len(A)
	for j in range(0,N):
		for k in range(0,N):
			if j<k and A[j]>A[k]:
				cnt1 = cnt1+1
			#print(cnt1)
	for j in range(0,N-1):
		if A[j]>A[j+1]:
			cnt2 = cnt2+1
		#print(cnt2)
	if cnt1==cnt2:
		print("YES")
	else:
		print("NO")
	cnt1=0
	cnt2=0
