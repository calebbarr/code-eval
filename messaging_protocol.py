import sys

class Tree:
	def __init__(self,label=None,left=None,right=None):
		self.label = label
		self.left = left
		self.right = right
		
	def left(self,tree):
		self.left = tree
	
	def right(self,tree):
		self.right = tree
	
	def isTerminal(self):
		return self.left == None and self.right == None
	
	def pprint(self,indent = 0):
		output = "\n"
		for i in xrange(indent):
			output += "\t"
		output += "( " + str(self.label)
		if self.left != None:
			output += self.left.pprint(indent+1)
		if self.right != None:
			output += self.right.pprint(indent+1)
		if self.isTerminal():
			output += " "
		else:
			for i in xrange(indent):
				output += "\t"
		output += ")\n"
		return  output		

'''
Grammar returned is in Chomsky Normal Form
'''
def get_grammar():
	return {
		'Z\' Msg' : 'Msg',
		'Cap Msg\'' : 'Msg',
		'Msg Msg' : "Msg\'",
		'leaf' : 'Msg',
		'Z' : 'Z\'',
		'M' : 'Cap',
		'K' : 'Cap',
		'P' : 'Cap',
		'Q' : 'Cap',
		'a' : 'leaf',
		'b' : 'leaf',
		'c' : 'leaf',
		'd' : 'leaf',
		'e' : 'leaf',
		'f' : 'leaf',
		'g' : 'leaf',
		'h' : 'leaf',
		'i' : 'leaf',
		'j' : 'leaf'
	}
	
'''
Implements the CYK algorithm
'''
def parse(characters,grammar):
	table = []
	for column_index in range(0,len(characters)+1):
		table.append([])
	for column in table:
		for row_index in range(0, len(characters)+1):
			column.append([])
	
	for j in range(1, len(characters)+1):
		current_character_index = j-1
		char = characters[current_character_index]
		
		if char not in grammar:
			return []
			
		pos = grammar[char]
		tree = Tree(char)
		tree = Tree(pos,tree)
		if pos in grammar:
			tree = Tree(grammar[pos],tree)
		table[j][j-1].append(tree)
			
		i = j-2
		while i > -1:
			k = i+1
			while k < j:
				left_subtrees = table[k][i]
				right_subtrees = table[j][k]
				
				for lhs in left_subtrees:
					for rhs in right_subtrees:
						rhs_label_candidate = lhs.label+" "+rhs.label
						if rhs_label_candidate in grammar:
							table[j][i].append(Tree(grammar[rhs_label_candidate],lhs,rhs))
				k+=1
			i-=1
			
	parses = []
	for tree in table[len(characters)][0]:
		if tree.label == "Msg":
			parses.append(tree)
	return parses
	
def get_tokens():
	example_input = "Qa Zj MZca Khfa"
	if len(sys.argv) >= 2:
		return open(sys.argv[1]).read().split()
	else:
		return example_input.split()

tokens = get_tokens()
grammar = get_grammar()

for token in tokens:
	output = token
	parses = parse(token,grammar)
	if len(parses) > 0:
		output += " VALID"
	else:
		output += " INVALID"	
	print output
	for tree in parses:
		print tree.pprint()