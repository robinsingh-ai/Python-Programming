"""
Author : Robin Singh
Implementation of Bellman Ford Algorithm(Dynamic Programming)
Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph.
It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.

Time Complexity : Best Case = O(E)
                  Worst Case = Average Case  = O(VE)

"""


def bellman_ford_SSS(graph,src):
    dist = dict()
    prev = dict()
    for node in graph:
        dist[node] =float('Inf')
        prev[node] = None
    dist[src] = 0

    for _ in range(len(graph)-1):
        for node in graph:
            for neighbour in graph[node]:
                if dist[neighbour]  > dist[node]+graph[node][neighbour]:
                    dist[neighbour] = dist[node]+graph[node][neighbour]
                    prev[neighbour] = node

    for node in graph:
        for neighbour in graph[node]:
            assert dist[neighbour] <= dist[node]+graph[node][neighbour],"Error,Graph Has Negative Weight Cycle"


    return dist,prev

if __name__ == '__main__':
    #Case 1
    graph = {
        'a':{'b':6,'c':4,'d':5},
        'b':{'e':-1},
        'c':{'e':3,'b':-2},
        'd':{'c':-2,'f':-1},
        'e':{'f':3},
        'f':{}
    }

    distance,prev = bellman_ford_SSS(graph,'a')
    print("Distances From point A")
    print(distance)

    print("Predecssor Vertices")
    print(prev)


    #graph with Negative Weight Cycle
    #Case 2
    graph = {
        'a':{'b':4,'c':5},
        'b':{'d':7},
        'c':{'b':7},
        'd':{'c':-15}#change value from -15 to -14 to make graph Postive Weight Cycle
    }
    distance,prev = bellman_ford_SSS(graph, 'a')
    print("")
    print("Distances From point A")
    print(distance)

    print("Predecssor Vertices")
    print(prev)

