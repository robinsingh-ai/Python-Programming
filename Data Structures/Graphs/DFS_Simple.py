"""
Author : Robbin Singh
Simple Implementaion of DFS(DEPTH FIRST SEARCH) Using Stack
"""
#Entre Adjancey Matrix of the graph
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries row wise:")
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
print("Adjancey Matrix:")
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()


print("\nDFS :")
visited = [0]*R

stack = [2]

visited[2]=1 #Node Starts From Vertex 0
n = stack.pop(len(stack)-1)
print( n ,end="")
while 1:
    for x in range(0,len(visited)):
        if matrix[n][x] == 1 and visited[x]==0:
            visited[x]=1
            stack.append(x)

    if len(stack)==0:
        break
    else:
        n = stack.pop(len(stack)-1)
        print("->",n,end=" ")





