from math import *
import numpy as np
from Nodes import *
from Graph import *
from Matching import *
from Ridesharing import *
from Dijkstra import *

def dijkstra_to_astar_graph(dij_graph): ##to convert existing dijjkstra graph into a format that Astar accepts
    a_star_graph = {}
    for i in dij_graph.items():
        a_star_graph[i[0]] = [(k, v) for k, v in i[1].items()]
    return (a_star_graph)

class AStarGraph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
      H = { }
      node_lst=self.adjac_lis.keys()
      for i in node_lst:
        H[i]=1
      return H[n]

    def a_star_algorithm(self, start, stop):
        # In this open_lst is a list of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])

        # dist_from_start has represent distances from start to all other nodes

        dist_from_start = {}
        dist_from_start[start] = 0

        # adjac_ofNodes contains an adjac mapping of all nodes
        adjac_ofNodes = {}
        adjac_ofNodes[start] = start

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or dist_from_start[v] + self.h(v) < dist_from_start[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while adjac_ofNodes[n] != n:
                    reconst_path.append(n)
                    n = adjac_ofNodes[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node is not present in both open_lst and closed_lst
                # add it to open_lst and node n as it's adjac_ofNodes
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    adjac_ofNodes[m] = n
                    dist_from_start[m] = dist_from_start[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update adjac_ofNodes data and dist_from_start data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if dist_from_start[m] > dist_from_start[n] + weight:
                        dist_from_start[m] = dist_from_start[n] + weight
                        adjac_ofNodes[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None

def get_dist_astar_path(route, graph): #this functions helps to calculate the total distance as per the route returned
    dist=0
    for i in range(0,len(route)-1):
      for j in graph.keys():
        if route[i]==j: #find the (from) node in the path on the graph
          for k in graph[j]:
            if route[i+1]== k[0]:#find the (to) node
              dist+=k[1] #sum up the distance between (from) node and (to) node
    return dist

def normalRide_astar(dijkstra_graph, drivers, riders):
    a_star_graph = dijkstra_to_astar_graph(dijkstra_graph) #to convert dijkstra graph into AStar graph
    graph1 = AStarGraph(a_star_graph) #create a object from the AStarGraph class
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
            # calculate rider1 src to dest
            # a1=distance of the route;a2=list of nodes in the route
            a1 = get_dist_astar_path(graph1.a_star_algorithm(drivers[i].ridersOnBoard[0].src, drivers[i].ridersOnBoard[0].dest), a_star_graph)
            a2 = graph1.a_star_algorithm(drivers[i].ridersOnBoard[0].src, drivers[i].ridersOnBoard[0].dest)
            df3 = pd.DataFrame(nodeConverter(a2, arrayOfNodes))
            # append the calculated distance to the driver
            drivers[i].dist += a1
            drivers[i].dist = round(drivers[i].dist,2)
            # append the calculated path to the driver
            drivers[i].path += a2[1:len(a2)]
            print("\n\n===================================================================")
            print("--------------------------Astar Algorithm--------------------------")
            print("===================================================================")
            print(f"The path from driver {drivers[i].name} to rider {drivers[i].ridersOnBoard[0].name}'s destination is:\n{drivers[i].path}")
            print("The total time taken is " + str(drivers[i].calculateTime()) + " min")
            print("The total distance is " + str(drivers[i].dist) + " km")
            print("The price is $" + str(drivers[i].calculateCharge()))
            df1=pd.DataFrame([drivers[i].dist])
            df4=pd.DataFrame([drivers[i].calculateTime()])
            df5=pd.DataFrame([drivers[i].calculateCharge()])
    pd.concat([pd.concat([df1,df2,df3,df4,df5],axis=1)]).to_csv('Astar.csv',index=False)