"""
Author : Robin Singh\
Implementation Of Graph Coloring Problem

Time Complexity : O(Color*Vertices)
"""
def is_safe(n, graph, colors, c):

    for i in range(n):
        if graph[n][i] and c == colors[i]:
            return False
    return True
def m_coloring_prob(graph, color, colors, n):
    if color+1 == n :
        return True
    for c in range(1, color+1):
        if is_safe(n, graph, colors, c):
            colors[n] = c
            if m_coloring_prob(graph, color, colors, n+1):
                return True
            colors[n] = 0
if __name__ == '__main__':
    no_of_vertex = 4
    color = 3
    """
    Colors
    1.Red
    2.Blue
    3.Green
    """
    colors = [0] * no_of_vertex
    adj_matrix = [
        [1,1,0,1],
        [1,1,1,1],
        [0,1,1,1],
        [1,1,1,1],]
    if m_coloring_prob(adj_matrix, color, colors, 0):
        print("Colors With Vertices")
        l = len(colors)
        for i in range(l):
            print(f"{i}-->",end="")
            if colors[i] == 1:
                print("Red",end=" ")
            elif colors[i] == 2:
                print("Blue",end=" ")
            else:
                print("Green",end=" ")
    else:
        print("Solution not Exits")