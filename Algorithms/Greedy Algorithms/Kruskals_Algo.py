"""
Author : Robin Singh
Implementation of Kruskal's Algorithm
Minimum Cost Spanning Tree of a given connected, undirected and weighted graph
It is a greedy algorithm in graph theory as it finds a minimum spanning tree for a connected weighted
graph adding increasing cost  at each step

Time Complexity  : O(ElogE) or O(ElogV)


"""


class Edge(object):
    # for storing (Source , destination,weight of the edge)
    def __init__(self, s, d, w):
        self.s = s
        self.d = d
        self.w = w


class Graph(object):
    def __init__(self, num_nodes=None, edgelist=None):
        self.num_nodes = num_nodes
        self.edgelist = edgelist
        self.parent = []
        self.rank = []
        # MCST stores edges of the minimum cost spanning tree
        self.mcst = []

    def _Parent(self, node):  # for finding the parent of the given node

        if self.parent[node] == node:
            return node
        return self._Parent(self.parent[node])

    def Kruskal_MCST(self):

        # Gonna sort all weight objects in the class edge
        self.edgelist.sort(key=lambda Edge: Edge.w)

        self.parent = [None] * self.num_nodes
        self.rank = [None] * self.num_nodes

        for n in range(self.num_nodes):
            # every node in the beginning is parent of itself
            self.parent[n] = n
            self.rank[n] = 0
            # in the beginning rank of every node is 0

        for edge in self.edgelist:
            r1 = self._Parent(edge.s)
            r2 = self._Parent(edge.d)

            # if parents of source and destinations are not in same subset then add that edge in the MCST
            if r1 != r2:
                self.mcst.append(edge)
                if self.rank[r1] < self.rank[r2]:
                    self.parent[r1] = r2
                    self.rank[r2] += 1
                else:
                    self.parent[r2] = r1
                    self.rank[r1] += 1

        print("MCST")
        print(f"SOURCE  DESTINATION  WEIGHT")
        cost = 0
        for edge in self.mcst:
            print(f"{edge.s}    -->  {edge.d}     -->     {edge.w}")

            cost += edge.w
        print("\nMCST(MINIMUM COST) : ", cost)


if __name__ == '__main__':
    num_nodes = 8
    A = Edge(1, 6, 10)
    B = Edge(3, 4, 12)
    C = Edge(7, 2, 14)
    D = Edge(2, 3, 16)
    E = Edge(7, 4, 18)
    F = Edge(4, 5, 22)
    G = Edge(5, 7, 24)
    H = Edge(5, 6, 25)
    I = Edge(1, 2, 28)

    #        1
    #   10  /
    #    6         2
    #    25 /   14   /  \  16
    # 5       7    3
    #   \         /
    # 22   \      /  12
    #       \   /
    #          4
    g1 = Graph(num_nodes, [A, B, C, D, E, F, G, H, I])
    g1.Kruskal_MCST()
