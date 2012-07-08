import sys

numbers = list(sys.argv[1])

seen = set()
duped = set()
dupes = []
for number in numbers:
	if number in seen:
		if number not in duped:
			dupes.append(number)
			duped.add(number)
	else:
		seen.add(number)
			
print str(dupes).strip("[],").replace("'","")

