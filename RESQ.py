def divide(N):
	for i in range(1,N//2):
		if N%i==0:
			a = N/i
			return a,i
T = int(input())
lis = []
for i in range(0,T):
	N = int(input())
	#a,b = divide(N)
	for j in range(1,N):
		if N%j==0:
			a = int(N//j)
			#return a,i
			if a>j:
				mini = int(a-j)
				lis.append(mini)
			elif a<j:
				mini = int(j-a)
				lis.append(mini)
			elif a==j:
				mini = int(j-a)
				lis.append(mini)
	print(min(lis))
	lis = []
