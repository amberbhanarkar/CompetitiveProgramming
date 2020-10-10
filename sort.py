T = int(input())
for i in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	cnt = [0,0,0]
	cnt[0] = A.count(0)
	cnt[1] = A.count(1)
	cnt[2] = A.count(2)
	print(cnt)
	for j in range(0,cnt[0]):
		A[j] = 0
	for j in range(0,cnt[1]):
		A[j+cnt[0]] = 1
	for j in range(0,cnt[2]):
		A[j+cnt[0]+cnt[1]] = 2
	print(A)
