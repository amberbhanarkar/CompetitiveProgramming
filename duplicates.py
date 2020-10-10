S = input()
se = list()
for i in S:
	if i in se:
		continue
	else:
		se.append(i)
print(se)
