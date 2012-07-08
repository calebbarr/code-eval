class Node:
	def __init__(self,value=None):
		self.value=value
		self.children = {1:None,2:None,3:None,4:None}
		
def read_in_trie(filename,root):
	for sequence in open(filename).readlines():
		pointer = root
		for char in sequence:
			if pointer.value != char:
				nones = []
				if pointer.children[1] == None:
					nones.append(1)
				elif pointer.children[1].value == char:
					pointer = pointer.children[1]
				else:
					if pointer.children[2] == None:
						nones.append(2)
					elif pointer.children[2].value == char:
						pointer = pointer.children[2]
					else:
						if pointer.children[3] == None:
							nones.append(3)
						elif pointer.children[3].value == char:
							pointer = pointer.children[3]
						else:
							if pointer.children[4] == None:
								nones.append(4)
							elif pointer.children[4].value == char:
								pointer = pointer.children[4]
							else:
								new_child_index = nones[0]
								print "creating new node"
								new_node = Node(char)
								pointer.children[new_child_index] = new_node
								pointer = new_node
	return root

def in_order(node):
	if node.children[1] != None:
		in_order(node.children[1])
	if node.children[2] != None:
		in_order(node.children[2])
	if node.children[3] != None:
		in_order(node.children[3])
	if node.children[4] != None:
		in_order(node.children[4])
	if node.value != None:
		print node.value
		
root = read_in_trie('targets', Node())
in_order(root)