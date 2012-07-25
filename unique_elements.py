import sys
for line in open(sys.argv[1]).readlines():
	current = None
	dupe_list = line.strip("\n").split(",")
	output = ""
	for thing in dupe_list:
		thing = thing.strip("\s+")
		if thing != current:
			current = thing
			output+=thing+","
	print output[:-1]