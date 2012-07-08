import sys

def quicksort(values):
	if len(values) == 0 or len(values) == 1:
		return values
	else:
		pivot = len(values)/2
		greater = []
		lesser = []
		
		for index in xrange(0,pivot):
			value = values[index]
			if value < values[pivot]:
				lesser.append(value)
			else:
				greater.append(value)
			
		for index in xrange(pivot+1,len(values)):
			value = values[index]
			if value < values[pivot]:
				lesser.append(value)
			else:
				greater.append(value)
						
		return quicksort(lesser)+[values[pivot]]+quicksort(greater)


stringvalues = list(sys.argv[1])
numvalues = []
for value in stringvalues:
	numvalues.append(int(value))
	
print str(quicksort(numvalues)).strip("[] ").replace(", ","")