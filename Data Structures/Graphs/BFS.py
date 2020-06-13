"""
Author : Robin Singh
Implementation Of BFS

"""
def bfs(graph, start):

    path = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:

            path.append(vertex)
            queue.extend(graph[vertex])
    return path
if __name__ == '__main__':


    graph={  0: [1, 3,4],
            1: [2],
            2: [3],
            3: [1,4],
            4: [0,2] }
    print(bfs(graph, 0))

