"""
Author : Robin Singh
Implementation Of Adjancey matrix
"""
class Graph:
	def __init__(self,no_of_verices):
		self.Nodes = no_of_verices
		self.matrix = []
		self.make_matrix()

	def make_matrix(self):
		for i in range(self.Nodes):
			v =[]
			for i in range(self.Nodes):
				v.append(0)
			self.matrix.append(v)

	def _edge_add(self,node1,node2):
		self.matrix[node1-1][node2-1]=1
		self.matrix[node2-1][node1-1]=1

	def print_matrix(self):
		for row in self.matrix:
			print(row)
		return print(row)



if __name__ == '__main__':

	n = int(input("Entre No Of Nodes(Vertices)"))
	g =Graph(n)
	while(1):
		ch = int(input("1.Add Edge\t2.Print Adjancey Matrix\t3.Exit"))
		if ch == 3:
			break
		elif ch ==1:
			n1 = int(input("Entre Value Of NODE 1"))
			n2 = int(input("Entre Value Of NODE 2"))
			g._edge_add(n1,n2)

		elif ch ==2:
			g.print_matrix()
		else:
			print("INVALID OPTION")


