T = int(input())
for i in range(0,T):
	a = input()
	b = input()
	a = sorted(a)
	b = sorted(b)
	flag = 0
	if len(a)!=len(b):
		flag= 0
	else:
		for j in range(0,len(a)):
			if a[j]!=b[j]:
				flag=0
			else:
				flag=1
	if flag==1:
		print(1)
	else:
		print(-1)
