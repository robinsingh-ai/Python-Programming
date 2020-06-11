"""
AUTHOR : Robin Singh
Implementation Of Adjancey List
"""

class Node:
	def __init__(self, value, next='*'):
		self.value = value
		self.next = next

	def get_Next(self):
		return self.next

	def get_Value(self):
		return self.value

	def set_Next(self, next):
		self.next = next

	def set_Value(self, value):
		self.value = value


class AD_LIST_GRAPH:
	def __init__(self, number_of_nodes):
		self.number_of_nodes = number_of_nodes
		self.nodes = []
		self.create_nodes()

	def create_nodes(self):
		for n in range(self.number_of_nodes):
			self.nodes.append(0)

	def Last_Node(self, first_node):
		node = first_node
		while not node.get_Next()=='*':
			node = node.get_Next()
		return node

	def _edge_add(self, node1, node2):
		if self.nodes[node1-1]==0:
			new_Node = Node(node2-1)
			self.nodes[node1-1]= new_Node
		else:
			new_Node = Node(node2-1)
			last_node = self.Last_Node(self.nodes[node1-1])
			last_node.set_Next(new_Node)

		if self.nodes[node2-1]==0:
			new_Node = Node(node1-1)
			self.nodes[node2-1]= new_Node
		else:
			new_Node = Node(node1-1)
			last_node = self.Last_Node(self.nodes[node2-1])
			last_node.set_Next(new_Node)

	def print_List(self, node, node_No):
		if node==0:
			print('node {} :No Edges Present'.format(node_No+1))
		else:
			op = ''
			while not node=='*':
				op = op+str(node.get_Value()+1)+' '
				node = node.get_Next()
			print('node {} -> {}'.format(node_No+1, op))

	def print1(self):
		for nodeess in range(0, self.number_of_nodes):
			self.print_List(self.nodes[nodeess], nodeess)

if __name__ == '__main__':
    n = int(input("Entre No Of Nodes(Vertices)"))
    g = AD_LIST_GRAPH(n)
    while (1):
        ch = int(input("1.Add Edge\t2.Print Adjancey Matrix\t3.Exit"))
        if ch == 3:
            break
        elif ch == 1:
            n1 = int(input("Entre Value Of NODE 1"))
            n2 = int(input("Entre Value Of NODE 2"))
            g._edge_add(n1, n2)

        elif ch == 2:
            g.print1()
        else:
            print("INVALID OPTION")







