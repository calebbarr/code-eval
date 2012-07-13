import sys
def first_unique_char(s):
	seen = set()
	unique = []
	for c in s:
		if c in seen:
			unique.remove(c)
		else:
			# c not in seen
			seen.add(c)
			unique.append(c)
	if len(unique):
		return unique[0]
	return None
	# no unique characters

for line in open(sys.argv[1],'r').readlines():
	print first_unique_char(line)