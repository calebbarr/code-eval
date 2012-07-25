LIMIT = 7919 #the sieve of Eratosthenes requires a limit, I happen to know the 1000th prime is 7919
numbers = range(2,LIMIT+1)
for i in numbers:
	j = 2
	while i * j <= numbers[-1]:
		if i * j in numbers:
			numbers.remove(i*j)
		j += 1
print sum(numbers)