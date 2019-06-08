lis1 = []
lis2 = ['a','e','i','o','u','A','E','I','O','U']
                
def sub(Str,n):
	for Len in range(1,n+1):
		for i in range(n-Len+1):
			j=i+Len-1
			for k in range(i,j+1):
				lis1.append(Str[k])
			

T = int(input())
for i in range(0,T):
	count=0
	str1 = input()
	sub(str1,len(str1))
	for i in lis1:
		if i in lis2:
			count = count+1
	print(count)
	lis1=[]	

	
	

