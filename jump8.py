a = 0
while a <= 99:
	a += 1
	if a % 7 ==0:
		continue
	if len(str(a)) == 2 and int(str(a)[1]) == 7:
		continue
	if len(str(a)) == 2 and int(str(a)[0]) == 7:
		continue
	print(a)

