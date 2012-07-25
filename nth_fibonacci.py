import sys
max_fibonacci = 1
fibonacci = {
	0 : 0,
	1 : 1
}
for line in open(sys.argv[1]).readlines():
	n = int(line.strip("\n"))
	if n > max_fibonacci:
		for m in xrange(max_fibonacci+1,n+1):
			fibonacci[m] = fibonacci[m-1] + fibonacci[m-2]
		max_fibonacci = n
	print fibonacci[n]