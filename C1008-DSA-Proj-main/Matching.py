import sys
import pandas as pd
from Nodes import *

#show all possible matching
def matchingBacktracking(numberOfDrivers, numberOfRiders):
    # set to determine if the column is used
    col = set()
    # contains all possible outcome
    res = []
    # initialize all the table to be 0
    board = [["0"] * numberOfRiders for i in range(numberOfDrivers)]
    # backtracking function
    def backtrack(r):
        # if r equals to number of drivers stop
        if r == numberOfDrivers:
            # create a copy of the board
            copy = [list(row) for row in board]
            # append the results into res
            res.append(copy)
            return
        
        for c in range(numberOfRiders):
            # if c in set of col, continue
            if c in col:
                continue
            # if c not in set of col, set the current table box to 1 and add c into set of col
            col.add(c)
            board[r][c] = "1"
            # recursively call the function
            backtrack(r + 1)
            # remove the col in the set of col and set it back to 0
            col.remove(c)
            board[r][c] = "0"
    # start backtracking
    backtrack(0)
    # return all possible answer
    return res

# shows the best matching in terms of total waiting time of riders
def batchedMatching(results, drivers, riders):
    numberOfDrivers = len(drivers)
    numberOfRiders = len(riders)
    # contains table of all possible results
    result = matchingBacktracking(numberOfDrivers, numberOfRiders)
    # set index to 0 and optimal to infinity
    index = 0
    optimal = sys.maxsize
    
    for i in range(len(result)):
        cost = 0
        for j in range(numberOfDrivers):
            for k in range(numberOfRiders):
                # iterative add the cost of each solution from the result table
                if (result[i][j][k] == "1"):
                    cost += results[j][k][0]
        # the most lowest cost will be the optimal
        if cost < optimal:
            optimal = cost
            index = i
    # add the path and distance to the driver using the most optimal solution
    for i in range(numberOfDrivers):
        for j in range(numberOfRiders):
            if result[index][i][j] == '1':
                drivers[i].dist += results[i][j][0]
                drivers[i].path += results[i][j][1]
                drivers[i].capacity -= 1
                drivers[i].ridersOnBoard.append(riders[j])

# same as batchedMatching above but implemented csv write to show demonstration
def batchedMatching2(results, drivers, riders):
    numberOfDrivers = len(drivers)
    numberOfRiders = len(riders)
    # contains table of all possible results
    result = matchingBacktracking(numberOfDrivers, numberOfRiders)
    # set index to 0 and optimal to infinity
    index = 0
    optimal = sys.maxsize
    for i in range(len(result)):
        cost = 0
        for j in range(numberOfDrivers):
            for k in range(numberOfRiders):
                # iterative add the cost of each solution from the result table
                if (result[i][j][k] == "1"):
                    cost += results[j][k][0]
        # the most lowest cost will be the optimal
        if cost < optimal:
            optimal = cost
            index = i
    # round off the optimal to nearest 2 dp
    optimal = round(optimal,2)
    print("\n\n==================================================================")
    print("-------------------------Batched Matching-------------------------")
    print("==================================================================")
    print("The most optimal index is " + str(index + 1) + "  best cost is " + str(optimal) + " km")

    data = pd.DataFrame([])
    # add the path and distance to the driver using the most optimal solution
    for i in range(numberOfDrivers):
        for j in range(numberOfRiders):
            if result[index][i][j] == '1':
                drivers[i].dist += results[i][j][0]
                drivers[i].path += results[i][j][1]
                drivers[i].capacity -= 1
                drivers[i].ridersOnBoard.append(riders[j])
                print("Driver" + str(i + 1) + " is assigned to Rider" + str(j + 1))
    # code to update the csv file
    df1 = pd.DataFrame([drivers[0].dist,drivers[1].dist,drivers[2].dist])
    df2 = pd.DataFrame(nodeConverter(drivers[0].path, arrayOfNodes))
    df3 = pd.DataFrame(nodeConverter(drivers[1].path, arrayOfNodes))
    df4 = pd.DataFrame(nodeConverter(drivers[2].path, arrayOfNodes))
    
    pd.concat([pd.concat([df1, df2, df3, df4], axis=1)]).to_csv('Matching.csv',index=False)