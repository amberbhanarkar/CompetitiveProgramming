def btd(n):
	return int(bin(n)[2:])

T = int(input())
j=0
for i in range(0,T):
	count=0
	X = int(input())
	for j in range(1,X):
		a = btd(j)
		if len(str(a))>=len(str(X//j)):
			count=count+1
	print(count)
	
