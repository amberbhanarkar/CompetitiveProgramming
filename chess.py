I, J, N = input().split()
I = int(I)
J = int(J)
N = int(N)
count=0
while N!=0:
	if ((I+2<=10) and (J+1<=10)):
		count = count+1
	if ((I-2>=0) and (J+1<=10)):
		count = count+1
	if ((J+2<=10) and (I+1<=10)):
		count = count+1
	if ((J-2>=0) and (I+1<=10)):
		count = count+1	
	if ((I+2<=10) and (J-1>=0)):
		count = count+1
	if ((I-2>=0) and (J-1>=0)):
		count = count+1
	if ((J+2<=10) and (I-1>=0)):
		count = count+1
	if ((J-2>=0) and (I-1>=0)):
		count = count+1
	N = N-1
print(count)
