import sys

for line in filter(lambda x: len(x) > 1, open(sys.argv[1],'r').readlines()):
	seen = set()
	for value in line.split(";")[1].split(","):
		value = value.strip("\n")
		if value in seen:
			print value
			break
		else:
			seen.add(value)