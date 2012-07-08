import sys

def mergesort(values):
	if len(values) == 1:
		return values
		
	mid = len(values)/2
	
	left = []
	right = []
	
	for index in xrange(0,mid):
		left.append(values[index])
		
	for index in xrange(mid,len(values)):
		right.append(values[index])
		
	left = mergesort(left)
	right = mergesort(right)
	
	return merge(left,right)
	
def merge(left, right):
	result = []
	
	while len(left) > 0 and len(right) > 0:
		if left[0] < right [0]:
			result.append(left[0])
			left = left[1:len(left)]
		else:
			result.append(right[0])
			right = right[1:len(right)]
	if len(left) > 0:
		result+=left
	elif len(right) > 0:
		result+=right
	
	return result

stringvalues = list(sys.argv[1])
numvalues = []
for value in stringvalues:
	numvalues.append(int(value))
	
print str(mergesort(numvalues)).strip("[] ").replace(", ","")