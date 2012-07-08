import sys

def combos(string, used, length, level,out):
	if level == length:
		print out
		return
	else:
		for index in range(0,length):
			if string[index] in used:
				index+=1
			else:
				out+=string[index]
				used.append(string[index])
				combos(string,used,length,level+1,out)
				out = out[0:-1]
				used.pop()

string = sys.argv[1]
used = []
combos(string,used,len(string),0,"")