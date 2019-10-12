T = int(input())
for i in range(0,T):
	x1, y1, x2, y2 = map(int,input().split())
	if y1==y2:
		if x1>x2:
			print("left")
		else:
			print("right")
	elif x1==x2:
		if y1>y2:
			print("down")
		else:
			print("up")
	else:
		print("sad")
