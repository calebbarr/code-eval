import random, sys

def shuffle(numbers, mode=1):
	midpoint = random.randrange(0,len(numbers))
	list1 = numbers[0:midpoint]
	list2 = numbers[midpoint:len(numbers)]
	if mode == 2:
		k = 0
		while len(list1) > 0 or len(list2) > 0:
			if len(list1) > 0:			
				numbers[k] = list1.pop(random.randrange(0,len(list1)))
				k+=1
			if len(list2) > 0:
				numbers[k] = list2.pop(random.randrange(0,len(list2)))
				k+=1
	else:
		i = 0
		j = 0
		k = 0
		while i < midpoint or j < len(numbers)-midpoint:
			if i < midpoint:
				numbers[k] = list1[i]
				i+=1
				k+=1
			if j < len(numbers)-midpoint:
				numbers[k] = list2[j]
				j+=1
				k+=1
	return numbers
		
numbers = [1, 2, 3, 4, 5, 6, 7]
print shuffle(numbers, 2)