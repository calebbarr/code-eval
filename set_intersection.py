import sys,re
for line in open(sys.argv[1]).readlines():
	print re.sub("(\[|\s+|\]|\')","",str(sorted(set(line.split(";")[0].split(",")) & set(line.split(";")[1].split(",")))))