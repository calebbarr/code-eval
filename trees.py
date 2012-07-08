import sys
root = None

class Node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		
def build_tree():
	global root
	
	n =  Node(0)
	m =  Node(1)
	o =  Node(2)
	p =  Node(3)
	q =  Node(4)
	r =  Node(5)
	s =  Node(6)
	
	m.parent=n
	n.left=m
	n.right=o
	o.parent =n
	
	m.left=p
	m.right=q
	p.parent=m
	q.parent=m
	
	o.left=r
	o.right=s
	r.parent=o
	s.parent=o
	
	t = Node(7)
	u = Node(8)
	v = Node(9)
	w = Node(10)
	x = Node(11)
	y = Node(12)
	z= Node(13)
	a= Node(14)
	
	p.left = t
	p.right = u
	t.parent = p
	u.parent = p
	
	q.left = v
	q.right = w
	v.parent = q
	w.parent = q
	
	r.left = x
	r.right = y
	x.parent = r
	y.parent = r
	
	s.left = z
	s.right = a
	z.parent = s
	a.parent = s
	
	root = n
	
def pre_order(node):
	if node.left != None:
		pre_order(node.left)
	if node.right != None:
		pre_order(node.right)
	print node.value
	
def in_order(node):
	if node.left != None:
		pre_order(node.left)
	print node.value			
	if node.right != None:
		pre_order(node.right)

def post_order(node):
	if node.left != None:
		pre_order(node.left)
	if node.right != None:
		pre_order(node.right)
	print node.value
	
def bfs(value=None):
	queue = [root]
	
	while len(queue) > 0:
		node = queue.pop(0)
		print node.value
		if node.value == value:
			return
		if node.left != None:
			queue.append(node.left)
		if node.right != None:		
			queue.append(node.right)
			
def dfs(value=None):
	queue = [root]

	while len(queue) > 0:
		node = queue.pop()
		print node.value
		if node.value == value:
			return
		if node.left != None:
			queue.append(node.left)
		if node.right != None:		
			queue.append(node.right)			
build_tree()
if sys.argv[1] == "pre":
	pre_order(root)
elif sys.argv[1] == "in":
	in_order(root)
elif sys.argv[1] == "post":
	post_order(root)
elif sys.argv[1] == "bfs":
	value = None
	if len(sys.argv) > 2:
		value = int(sys.argv[2])
	bfs(value)
elif sys.argv[1] == "dfs":
	value = None
	if len(sys.argv) > 2:
		value = int(sys.argv[2])
	dfs(value)