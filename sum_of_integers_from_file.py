import sys
total = 0
for number in open(sys.argv[1]).readlines():
	total += int(number.strip("\n"))
print total