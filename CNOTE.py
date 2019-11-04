T = int(input())
cnt1 = 0
cnt2 = 0
for i in range(0,T):
	X, Y, K, N = map(int,input().split())
	for i in range(0,N):
		P, C = map(int,input().split())
		if X-Y<=P and K>=C:
			#print("LuckyChef")
			cnt1 = cnt1+1
		else:
			cnt2 = cnt2+1
			#print("UnluckyChef")	
	if cnt1>=1:
		print("LuckyChef")
	else:
		print("UnluckyChef")
	cnt1=0
	cnt2=0
