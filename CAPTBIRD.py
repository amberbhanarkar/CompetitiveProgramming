T = int(input())
from math import *
l_max = []
l = []
for i in range(0,T):
	l_max=[]
	l=[]
	n = int(input())
	x = list(map(int,input().split()))
	P, Q = map(int,input().split())
	for j in range(0,n):
		for k in range(0,n):
			if P==0 and (x[j]==0 or x[k]==0):
				l.append(45*0.0174533)
			else:	
				m1 = (Q)/(P-x[j])
				m2 = (Q)/(P-x[k])
				tan = (m2-m1)/(1+m1*m2)
				theta = degrees(atan(tan))
				radian = theta*0.0174533
				l.append(radian)
		l_max.append(max(l))
	print(max(l_max))

		
