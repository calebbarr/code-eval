import sys
for line in open(sys.argv[1]).readlines():
	a,b,n = line.split()
	a = int(a)
	b = int(b)
	n = int(n)
	output_line = ""
	for index in xrange(1,n+1):
		output = ""
		if index % a != 0 and index % b != 0:
			output = str(index)
		else:
			if index % a == 0:
				output = "F"
			if index % b == 0:
				output += "B"
		output_line += output + " "
	print output_line[:-1]