"""
Robin Singh
Implementation of prims algorithm
In Prim's Algorithm, a conquered territory (initialized with any start vertex)
is chosen in which we keep adding the vertices as we go through the algorithm
To get the minimum spanning tree, we keep adding vertices to the conquered edges
with the greedy paradignm that we select the edge with the minimum weight of all the edges starting the
conquered territory and ending at the unconquered territory. The end of the minimum weight edge thus chosen is
then added to the conquered territory and removed from the unconquered territory. In such a way,
we go on till the conquered territory spans all the vertices of the graph


Time Complexity : O(ElogV)
"""


# @dataclass(eq=0)


class Node(object):
    def __init__(self, source=None):
        self._num = source


class Prims(object):
    def __init__(self, source, graph):
        self.source = source
        self._list = graph

    def prims_MCST(self):
        MCST_Cost = 0
        queue = {Node(self.source): 0}
        added = [0]*len(self._list)

        while queue:
            # choosing the adjancent Node having the minimum cost
            node = min(queue, key=queue.get)
            cost_Node = queue[node]
            # Delete that Node from the Dict
            del queue[node]

            if added[node._num] == 0:  # If node is not Visited
                MCST_Cost += cost_Node

                added[node._num] = True  # Mark Visited

                print(f"{node._num} -->  ", end=" ")

                for n in self._list[node._num]:
                    adjancent_node = n[0]
                    adjancent_cost = n[1]
                    if added[adjancent_node] == 0:
                        queue[Node(adjancent_node)] = adjancent_cost
        print("Cost : ", MCST_Cost)


if __name__ == '__main__':
    list = {}
    list[1] = [(6, 10), (2, 28)]
    list[2] = [(1, 28), (3, 16), (0, 14)]
    list[3] = [(2, 16), (4, 12)]
    list[4] = [(3, 12), (5, 22), (0, 18)]
    list[5] = [(4, 22), (6, 25), (0, 24)]
    list[6] = [(1, 10), (5, 25)]
    list[0] = [(2, 14), (4, 18), (5, 24)]

    A = Prims(3, list)  # Insert Any Node
    print("MCST")
    A.prims_MCST()
