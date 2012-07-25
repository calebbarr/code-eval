import sys
for line in open(sys.argv[1],'r'):
	greater_than,multiplier = line.split(",")
	greater_than = int(greater_than)
	multiplier = int(multiplier)
	for multiplicand in xrange(greater_than+1):
		product = multiplier*multiplicand
		if product > greater_than:
			print product
			break