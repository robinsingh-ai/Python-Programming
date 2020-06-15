"""
Author : Robin Singh
Implementation of Topological Sorting
"""
class Graph():
    def __init__(self, c):
        self.vertex = {}
        self.count = c
    def print_adj_list(self):
        for i in self.vertex.keys():

            print(i ,"Vertex :",' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    def _edge_add(self, o, d):

        if o in self.vertex.keys():
            self.vertex[o].append(d)
        else:

            self.vertex[o] = [d]
            self.vertex[d] = []

    def topo_Sort(self):
        visited = [0] * self.count
        stack = []
        for vertex in range(self.count):

            if visited[vertex] == False:
                self.topological(vertex, visited, stack)

        print('--> '.join([str(i) for i in stack]))



    def topological(self, vertices, visited, s):

        visited[vertices] = True

        try:
            for adj_node in self.vertex[vertices]:
                if visited[adj_node] == False:
                    self.topological(adj_node, visited, s)
        except KeyError:
            return

        s.insert(0,vertices)

if __name__ == '__main__':
    c = int(input("Entre Number Of vertices"))
    g= Graph(c)
    while 1:
        print(f"\n1.Edge Add\t2.Print Adjancey List\t3.Topological Sort\t4.Exit")
        ch = int(input("Entre Choice"))
        if ch == 4:
            break
        elif ch ==1:
            n1 = int(input("Entre Origin Node 1"))
            n2 = int(input("Entre Destination Node 2"))
            g._edge_add(n1,n2)
        elif ch ==2:
            g.print_adj_list()
        elif ch ==3:
            print("Topological Sort :")
            g.topo_Sort()
        else:
            print("invalid Choice")


