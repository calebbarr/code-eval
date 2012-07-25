import sys
lines = open(sys.argv[1],'r').readlines()  # get all lines in the file
n = int(lines[0][0]) # first character in first line is n
lines = sorted(filter(lambda x: len(x) > 0, lines[1:]), key=len, reverse=True) # take the rest of the lines, filter blanks
for index in xrange(min(n,len(lines))): # iterate through n lines, use min in case n > lines.length
	print lines[index].strip("\n")