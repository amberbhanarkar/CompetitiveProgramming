T = int(input())
for i in range(0,T):
	N, M=input().split()
	N = int(N)
	M = int(M)
	if M%N==0:
		print('Yes')
	else:
		print('No')

