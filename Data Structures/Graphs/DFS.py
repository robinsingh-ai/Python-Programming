"""
Author : Robin Singh
Implementation of DFS

"""


# v = []
# def dfs_graph(graph,node):
#     global v
#     if node not in v:
#         v.append(node)
#         for n in graph[node]:
#             dfs_graph(graph,n)
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited


if __name__ == '__main__':

    graph1 = {
            0: [1, 3,4],
            1: [2],
            2: [3],
            3: [1,4],
            4: [0,2]
                                    }

    v= dfs(graph1, 2,[])
    print(v)