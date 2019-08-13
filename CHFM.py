import statistics
su=0
flag=0
T = int(input())
for i in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	for i in range(0,N):
		su = su+A[i]
	x = statistics.mean(A)
	for i in range(0,N):
		if (su-A[i])/(N-1)==x:
			print(i+1)
			flag=1
			break
	if flag==0:
		print("Impossible")
	A=[]
	su=0
	flag=0
