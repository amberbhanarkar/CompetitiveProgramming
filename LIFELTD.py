T = int(input())
L = [[0 for i in range(0,3)] for j in range(0,3)]
for i in range(0,T):
	A = input()
	L[0][0]=A[0]
	L[0][1]=A[1]
	L[0][2]=A[2]
	B = input()
	L[1][0]=B[0]
	L[1][1]=B[1]
	L[1][2]=B[2]
	C = input()
	L[2][0]=C[0]
	L[2][1]=C[1]
	L[2][2]=C[2]
	if L[0][0]=='l' and L[1][0]=='l' and L[1][1]=='l':
		print("yes")
	elif L[0][1]=='l' and L[1][1]=='l' and L[1][2]=='l':
		print("yes")
	elif L[1][0]=='l' and L[2][0]=='l' and L[2][1]=='l':
		print("yes")
	elif L[1][1]=='l' and L[2][1]=='l' and L[2][2]=='l':
		print("yes")
	else:
		print("no")
		
