import sys

entry = None

class Node:

	def __init__(self,value):
		self.value=value
		self.arcs = {}
		
	def connect(self, node):
		self.arcs[node.value] = node
		
	
def build_graph():
	global entry
	n = Node(0)
	entry = n
	m = Node(1)
	n.connect(m)
	o = Node(2)
	n.connect(o)
	p = Node(3)
	q = Node(4)
	m.connect(p)
	m.connect(q)
	r = Node(5)
	s = Node(6)	
	o.connect(r)
	o.connect(s)
	t = Node(7)
	u = Node(8)
	p.connect(t)
	q.connect(u)
	v = Node(9)
	w = Node(10)
	r.connect(v)
	s.connect(w)
	x = Node(11)
	y = Node(12)
	z = Node(13)
	v.connect(x)
	w.connect(x)
	t.connect(y)
	u.connect(y)
	x.connect(z)
	y.connect(z)
	
def kruskal():
	global entry
	n = entry

	while n is not None:
		print str(n.value) + " connects to "
		keys = n.arcs.keys()
		if len(keys) > 0:
			n = n.arcs[keys[0]]
		else:
			break

build_graph()

print entry
if len(sys.argv)  > 1:
	algo = sys.argv[1]
	if algo == "kruskal":
		kruskal()