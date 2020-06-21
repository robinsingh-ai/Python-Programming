"""
Author : Robin Singh
Implementation of Dijkstra's Algorithm
Dijkstra’s algorithm finds the shortest path in a weighted graph containing only positive edge weights from a single source


Time Complexity  : O((E+V)Log(V))


"""

from dataclasses import dataclass,field

def dijkstra_SSS(graph , start , Destination):
    shortest_dist = {} #records the cost to reach the destination node and will be updated as we will be moving along the graph
    track_prev_nodes = {} #keep track of the path that has led us to this node
    not_visited_nodes = graph #to iterate through the entire graph
    infinity = 1000000000000 # infinity can be considerd a very large number
    path = [] #going to trace our journey back to the source node

    for node in not_visited_nodes:
        shortest_dist[node] = infinity #initially we want to assign infinity as cost to all other nodes and 0 to the start node
    shortest_dist[start] = 0
    #loop will keep running until we have entirely exhausted the graph until we have seen all the nodes
    while not_visited_nodes:
        min_dist_node = None

        for node in not_visited_nodes:  #if u find out that if the shortest distance is lower then move on the next pointer so that we can move through the graph
            if min_dist_node is None:
                min_dist_node = node

            elif shortest_dist[node] < shortest_dist[min_dist_node]:
                min_dist_node = node

        #these will give the possible paths from from (min_dist_node)current node
        path_options = graph[min_dist_node].items()
        #we have to calculate the cost each time for each path we take and will only update iff it is lower than the current node
        for adj_node,weight in path_options:
            if weight + shortest_dist[min_dist_node] < shortest_dist[adj_node]: #d[u]+c[u,v]<d[v] then d[v] = d[u]+c[u,v]
                shortest_dist[adj_node] = weight+shortest_dist[min_dist_node]
                track_prev_nodes[adj_node] = min_dist_node
        #we will pop out all the nodes that we have just visited so that we don't iterate over them again
        not_visited_nodes.pop(min_dist_node)



    #when we reached the destination node then we want to trace back our path and calculate the total cost
    curreentNode = Destination

    while curreentNode != start:    #for track back all the predessor nodes

        try:
            path.insert(0,curreentNode)
            curreentNode = track_prev_nodes[curreentNode]
        except KeyError:
            print("We Can't Reach To Destination Node")
            break

    path.insert(0,start)
    # if cost is infinity that means the node had not beem reached too the destnation node
    if shortest_dist[Destination] != infinity:
        print(f"Single Source Shortest Path :{path} --> COST : {shortest_dist[Destination]}")


if __name__ == '__main__':
    graph = {
        'a':{'b':4,'h':8},
        'b':{'a':4,'h':11,'c':8},
        'c':{'b':8,'i':2,'d':7},
        'd':{'e':9,'c':7,'f':14},
        'e':{'d':9,'f':10},
        'f':{'d':14,'e':10,'g':2},
        'g':{'i':6,'f':2,'h':1},
        'h':{'a':8,'b':11,'i':7,'g':1},
        'i':{'c':2,'g':6,'h':7}
    }
    while(1):
        print(f"1.Add Source And Destination\t2.Exit")
        ch = int(input("Entre choice"))
        if ch == 2:
            break
        elif ch ==1:
            s = input("Source ?")
            d = input("Destination ?")
            dijkstra_SSS(graph,s,d)
        else:
            print("Invalid Option")












