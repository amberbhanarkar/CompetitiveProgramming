a, b= input().split()
a = int(a)
b = int(b)
lis = []
def sumdigits(number):
  if number == 0:
    return 0
  else:
    return (number%10) + sumdigits(number//10)

def prime(num):
	count = 0
	for i in range(1,num+1):
		if num%i==0:
			count = count+1
	if count==2:
		return num
			
def prime_range(x,y):
	count = 0
	for i in range(x,y+1):
		count=1
		for j in range(2,i):
			if i%j==0:
				count=0
				break
		if count == 1:
			#print(i)
			a = sumdigits(i)
			#print(a)
			b = prime(a)
			lis.append(b)
	lis.remove(None)
	sarr = [str(a) for a in lis]
	print(" " . join(sarr))
	#print(','.join(lis))
prime_range(a,b)

