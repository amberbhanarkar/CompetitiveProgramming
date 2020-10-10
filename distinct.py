T = int(input())
for i in range(0,T):
	S = input()
	l = []
	maxi = 0
	cnt = 1
	for j in S:
		if j in l:
			if cnt>maxi:
				maxi=cnt
			cnt=1
			continue
		else:
			l.append(j)
			cnt+=1
	print(maxi)
