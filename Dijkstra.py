import sys
from Matching import *

def dijkstra(graph, src, dest):
    graph = graph.copy()
    shortestdist={}
    track_predessor={}
    unvisited_nodes=graph
    infinity= sys.maxsize
    path=[]

    #initialize distance to infinity and source distance to be 0
    for node in unvisited_nodes:
        shortestdist[node]=infinity
    shortestdist[src] = 0

    # initialize min_distance_node to be none as there is no nodes
    # main loop
    while unvisited_nodes:
        min_distance_node = None

        # check every nearby node and find the node with the shortest distance
        for node in unvisited_nodes:
            if min_distance_node is None:
                min_distance_node=node
            elif shortestdist[node] < shortestdist[min_distance_node]:
                min_distance_node=node

        # check every linked node from the node itself
        path_choices = graph[min_distance_node].items()

        # find the shortest overall distance after calculating each choice
        # edge relaxation
        for child_node,distance in path_choices:
            if distance+shortestdist[min_distance_node] < shortestdist[child_node]:
                shortestdist[child_node] = distance+shortestdist[min_distance_node]
                track_predessor[child_node] = min_distance_node

        # return the shortest distance
        unvisited_nodes.pop(min_distance_node)

    currentNode=dest

    # find the path to destination
    while currentNode!= src:
        try:
            path.insert(0,currentNode)
            currentNode=track_predessor[currentNode]

        except KeyError:
            print("Path not available")
            break

    # add the path from source, to generate the full path from source to destination
    path.insert(0,src)

    # return the shortest distance and the path
    if shortestdist[dest] != infinity:
        return shortestdist[dest],path

#shortest path list of nodes
def dijkstra2(graph, src, dest):
    graph = graph.copy()
    shortestdist={}
    track_predessor={}
    unvisited_nodes=graph
    infinity= sys.maxsize
    path=[]
    for node in unvisited_nodes:
        shortestdist[node]=infinity
    shortestdist[src] = 0

    while unvisited_nodes:
        min_distance_node= None

        for node in unvisited_nodes:
            if min_distance_node is None:
                min_distance_node=node
            elif shortestdist[node] < shortestdist[min_distance_node]:
                min_distance_node=node

        path_choices= graph[min_distance_node].items()

        for child_node,distance in path_choices:
            if distance+shortestdist[min_distance_node] < shortestdist[child_node]:
                shortestdist[child_node] = distance+shortestdist[min_distance_node]
                track_predessor[child_node] = min_distance_node

        unvisited_nodes.pop(min_distance_node)

    currentNode=dest

    while currentNode!= src:
        try:
            path.insert(0,currentNode)
            currentNode=track_predessor[currentNode]

        except KeyError:
            print("Path not available")
            break

    path.insert(0,src)

    if shortestdist[dest] != infinity:
        return path

#return shortest distance
def dijkstra3(graph, src, dest):
    graph = graph.copy()
    shortestdist={}
    track_predessor={}
    unvisited_nodes=graph
    infinity= sys.maxsize
    path=[]
    for node in unvisited_nodes:
        shortestdist[node]=infinity
    shortestdist[src] = 0

    while unvisited_nodes:
        min_distance_node= None

        for node in unvisited_nodes:
            if min_distance_node is None:
                min_distance_node=node
            elif shortestdist[node] < shortestdist[min_distance_node]:
                min_distance_node=node

        path_choices= graph[min_distance_node].items()

        for child_node,distance in path_choices:
            if distance+shortestdist[min_distance_node] < shortestdist[child_node]:
                shortestdist[child_node] = distance+shortestdist[min_distance_node]
                track_predessor[child_node] = min_distance_node

        unvisited_nodes.pop(min_distance_node)

    currentNode=dest

    while currentNode!= src:
        try:
            path.insert(0,currentNode)
            currentNode=track_predessor[currentNode]

        except KeyError:
            print("Path not available")
            break

    path.insert(0,src)

    if shortestdist[dest] != infinity:
        return shortestdist[dest]

#function used to show dijkstra routing and write to CSV
def normalRide_dijkstra(dijkstra_graph, drivers, riders):
    numberOfRiders = len(riders)
    numberOfDrivers = len(drivers)
    results = [[0] * numberOfRiders for i in range(numberOfDrivers)]

    # for loop used for batched matching
    for i in range(numberOfDrivers):
        for j in range(numberOfRiders):
            results[i][j] = dijkstra(dijkstra_graph, drivers[i].loc, riders[j].src)

    batchedMatching(results, drivers, riders)
    for i in range(numberOfDrivers):
        if drivers[i].ridersOnBoard[0].name == 'John':
            df2 = pd.DataFrame(nodeConverter(drivers[i].path, arrayOfNodes))
            a1, a2 = dijkstra(dijkstra_graph, drivers[i].ridersOnBoard[0].src, drivers[i].ridersOnBoard[0].dest)
            df3 = pd.DataFrame(nodeConverter(a2, arrayOfNodes))
            drivers[i].dist += a1
            drivers[i].dist = round(drivers[i].dist,2)
            drivers[i].path += a2[1:len(a2)]
            print("\n\n===================================================================")
            print("-------------------------Dijkstra Algorithm------------------------")
            print("===================================================================")
            print(f"The path from driver {drivers[i].name} to rider {drivers[i].ridersOnBoard[0].name}'s destination is:\n{drivers[i].path}")
            print("The total time taken is " + str(drivers[i].calculateTime())+ " min")
            print("The total distance is " + str(drivers[i].dist) + " km")
            print("The price is $" + str(drivers[i].calculateCharge()))
            df1 = pd.DataFrame([drivers[i].dist])
            df4 = pd.DataFrame([drivers[i].calculateTime()])
            df5 = pd.DataFrame([drivers[i].calculateCharge()])
    pd.concat([pd.concat([df1,df2,df3,df4,df5], axis=1)]).to_csv('Dijkstra.csv',index=False)