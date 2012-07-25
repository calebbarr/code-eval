import sys
strip_chars = set(["\'","[","]",","])
for line in open(sys.argv[1]).readlines():
	values = line.strip("\n").split()
	cycle_size = 1
	longest_cycle = None
	while cycle_size <= len(values)/2:
		cycle_candidate = None
		for end_index in xrange(len(values),-1,-cycle_size):
			cycle_matcher = values[end_index-cycle_size:end_index]
			if cycle_matcher == cycle_candidate:
				longest_cycle = filter(lambda x: x not in strip_chars, str(cycle_candidate))
				break
			cycle_candidate = cycle_matcher
		cycle_size +=1
	if longest_cycle != None:
		print longest_cycle