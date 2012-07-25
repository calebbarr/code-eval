LIMIT = 1000 
numbers = range(2,LIMIT+1)
for i in numbers:
	j = 2
	while i * j <= numbers[-1]:
		if i * j in numbers:
			numbers.remove(i*j)
		j += 1
number = -1
for index in xrange(len(numbers)-1,-1,-1):
	number = str(numbers[index])
	if len(number) == 3:
		if number[0] == number[2]:
			break
	elif len(number) == 2:
		if number[0] == number[1]:
			break
	else:
		break
print number