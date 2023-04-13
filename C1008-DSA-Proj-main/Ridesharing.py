from math import *
import numpy as np
from Nodes import *
from Graph import *
from Matching import *
import pandas as pd
from Dijkstra import *


def ridesharing(drivers, riders, graph):
    fullPath = [] # empty array to store full path of driver
    min = dijkstra3(graph, drivers[0].loc, riders[0].src) # distance from first driver to main user
    driverToUserPath = dijkstra2(graph, drivers[0].loc, riders[0].src) # path from first driver to main user
    assignedDriver = drivers[0] # set assigned driver as first driver which may be changed depending on distance
    for i in range(len(drivers)):  # let riders[0] be the MAIN user to be plotted on map
        if dijkstra3(graph, drivers[i].loc, riders[0].src) < min:  # check if reiterated driver to user distance less than min
            min = dijkstra3(graph, drivers[i].loc, riders[0].src) # set min distance
            assignedDriver = drivers[i] # set new assigned driver
            driverToUserPath = dijkstra2(graph, drivers[i].loc, riders[0].src)  # set new path from driver to main user
    fullPath.extend(driverToUserPath)  # add path from driver to main user to full path of driver
    minFromMainToShared = dijkstra2(graph, riders[0].src, riders[1].src)# path from main user to shared user
    minToSecondUserDist = dijkstra3(graph, riders[0].src, riders[1].src)# distance from main to shared user
    sharedRider = riders[1] # let riders[1] be the shared user to be plotted on map which may be changed depending on distance
    for i in range(len(riders) - 2):  # check shortest distance between main user and other user
        if dijkstra3(graph, riders[0].src, riders[i + 2].src) < minToSecondUserDist:# check if main user to reiterated user distance less than min
            minFromMainToShared = dijkstra2(graph, riders[0].src, riders[i + 2].src)# set new path from main to shared user
            sharedRider = riders[i] # set new shared user
            minToSecondUserDist = dijkstra3(graph, riders[0].src, riders[i + 2].src)# set new min distance

    if minToSecondUserDist>1.8: # if min distance from main user to shared user is more than 2km, do not pickup shared user
        pass
    else: # statement to run if shared user pickedup
        fullPath.extend(minFromMainToShared[1:])  # use [1:] to remove the first node of second path as repeated
        firstDest = riders[0].dest # set first destination which may be changed depending on distance
        secondDest = sharedRider.dest # set second destination which may be changed depending on distance
        if dijkstra3(graph, sharedRider.src, firstDest) > dijkstra3(graph, sharedRider.src,
                                                                secondDest):  # check if which destination is nearer
            temp = secondDest # exchange first and second destination
            secondDest = firstDest
            firstDest = temp
        sharedRiderToFirstDest = dijkstra2(graph, sharedRider.src, firstDest) # get distance from share rider location to first destination
        firstDestToSecond = dijkstra2(graph, firstDest, secondDest)# get distance from first destination to second destination
        fullPath.extend(sharedRiderToFirstDest[1:])  # add path from shared rider src to first dest
        fullPath.extend(firstDestToSecond[1:])  # add path from first dest to second dest
        # get total distance
        totalDist = min + minToSecondUserDist + dijkstra3(graph, sharedRider.src, firstDest) + dijkstra3(graph, firstDest,secondDest)
        totalDist = round(totalDist, 2)
        timeTaken = int((totalDist / 28.9) * 60)  # calculate time taken
          
        print("\n\n===================================================================")
        print("----------------------Ridesharing Algorithm------------------------")
        print("===================================================================")  
        print("Ridesharing Algorithm: The total time taken is " + str(timeTaken) + " min")
        print("Ridesharing Algorithm: The total distance is " + str(totalDist) + " km")
        # writing dataframe into csv file
        df0 = pd.DataFrame([totalDist])
        df1 = pd.DataFrame(nodeConverter(driverToUserPath, arrayOfNodes))
        df2 = pd.DataFrame(nodeConverter(minFromMainToShared, arrayOfNodes))
        df3 = pd.DataFrame(nodeConverter(sharedRiderToFirstDest, arrayOfNodes))
        df4 = pd.DataFrame(nodeConverter(firstDestToSecond, arrayOfNodes))
        pd.concat([pd.concat([df0, df1, df2, df3, df4], axis=1)]).to_csv('Ridesharing.csv', index=False)
        return 0

    #statement below is for if shared user is not pickedup
    mainUsertoDest = dijkstra2(graph,riders[0].src,riders[0].dest)
    totalDist = +dijkstra3(graph,riders[0].src,riders[0].dest)
    totalDist = round(totalDist, 2)
    timeTaken = int((totalDist / 28.9) * 60)  # calculate time taken

    df0 = pd.DataFrame([totalDist])
    df1 = pd.DataFrame(nodeConverter(driverToUserPath, arrayOfNodes))
    df2 = pd.DataFrame(nodeConverter(mainUsertoDest, arrayOfNodes))
    df3 = pd.DataFrame(nodeConverter(['Node10','Node9','MOEctr'],arrayOfNodes))
    pd.concat([pd.concat([df0, df1, df2,df3], axis=1)]).to_csv('Ridesharing2.csv', index=False)
    print("Ridesharing Algorithm(No pickup): The total time taken is " + str(timeTaken) + " min")
    print("Ridesharing Algorithm(No pickup): The total distance is " + str(totalDist) + " km")
