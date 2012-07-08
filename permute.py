#Caleb Barr
#Sorted perumtations of a string

import sys

def permute(string, used, length, level,out,permutations):
	if level == length:
		permutations.append(out)
		return permutations
	else:
		for index in range(0,length):
			if used[index] == True:
				index+=1
			else:
				out+=string[index]
				used[index] = True;
				permutations = permute(string,used,length,level+1,out,permutations)
				used[index] = False
				out = out[0:-1]
	return permutations

filename = sys.argv[1]
for string in open(filename,'r').readlines():
	string = string.strip("\n")
	array = list(string)
	used = [False for letter in string]
	permutations = permute(string,used,len(string),0,"",[])
	permutations.sort()
	print str(permutations).strip("[]").replace(" ","").replace("'","")