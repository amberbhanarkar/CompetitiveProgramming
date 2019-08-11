T = int(input())
for i in range(0,T):
	lis=[]
	a=0
	S = input()
	lis.extend(S)
	a = lis.count('1')
	if(a%2!=0):
		print("WIN")
	else:
		print("LOSE")
	
