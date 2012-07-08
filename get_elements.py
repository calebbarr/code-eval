for line in open('periodic_table.txt','r').readlines():
	element = line.split()[4] 
	try:
		int(element)
		element = line.split()[3]
	except ValueError:
		something = None
	print element