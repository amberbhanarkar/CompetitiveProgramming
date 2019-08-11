T = int(input())
for i in range(0,T):
	N, K = map(int,input().split())
	if((N/K)%K==0.0):
		print("NO") 
	else:
		print("YES")
		

