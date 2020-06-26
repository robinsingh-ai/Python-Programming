"""
Author : Robin Singh
Implementation of Floyd Warshall's Algorithm
Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph
This algorithm works for both the directed and undirected weighted graphs. But, it does not work for the graphs
with negative cycles (where the sum of the edges in a cycle is negative)

Time Complexity : O(n^3)

"""
INF = 999999999999
def floydWarshall(graph,n): #n=no. of vertex
    APSP=graph
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                APSP[i][j] = min(APSP[i][j] ,APSP[i][k]+ APSP[k][j])
    return APSP

#function to print the final matrix
def APSP_ans(ans,n):
    for i in range(n):
        for j in range(n):
            if(ans[i][j] == INF):
                print("INF", end=" ")
            else:
                print(ans[i][j], end="  ")
        print(" ")


if __name__ == '__main__':
    n = 4  #Number of verices
    #Graph Matrix with Initial Distances
    G = [[0, 9, -4, INF],
         [6, 0, INF, 2],
         [INF, 5, 0, INF],
         [INF, INF, 1, 0]]
    ans = floydWarshall(G,n)
    APSP_ans(ans,n)


    #         (9)
    # /------------\
    # 1-------------2
    # |(-4) (6)   | | (2)
    # | /---------  |
    # |/     (5)    |
    # 3-------------4
    #       1



