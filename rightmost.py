import sys
for line in open(sys.argv[1],'r').readlines():
	string,char = line.strip("\n").split(",")
	found = False
	for index in xrange(len(string)-1,-1,-1):
		if string[index] == char:
			print index
			found = True
	if not found:
		print -1