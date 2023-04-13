from math import *
import numpy as np
from Nodes import *
from Graph import *
from Matching import *
from Ridesharing import *
from Dijkstra import *
from Astar import *

class Driver: #driver class
    capacity = 2
    # based on Singapore's average traffic
    # https://data.gov.sg/dataset/road-traffic-conditions?resource_id=bdfdb0b5-c3a4-4dc9-8a9a-ec130ba9fd0f 
    speed = 28.9
    
    def __init__(self, loc, vehicle_type, name):
        self.loc = loc
        self.name = name
        self.vehicle_type = vehicle_type
        self.ridersOnBoard = []
        self.path = []
        self.dist = 0
    
    # calculate time based on distance and speed in minutes
    def calculateTime(self):
        time = (self.dist / self.speed) * 60
        return int(time)

    # calculate charge based on vehicle type and distance
    def calculateCharge(self):
        if self.vehicle_type == 'Hyundai':
          base = 3.9
          meterCharge = self.dist / 0.200 * 0.4
          total = round(base + meterCharge, 2)
          return total
        elif self.vehicle_type == 'Toyota':
          base = 4.1
          meterCharge = self.dist / 0.200 * 0.4
          total = round(base + meterCharge, 2)
          return total
        elif self.vehicle_type == 'Mercedez':
          base = 4.3
          meterCharge = self.dist / 0.200 * 0.4
          total = round(base + meterCharge, 2)
          return total
          

class Rider: #rider class
    def __init__(self, src, dest, name):
        self.src = src
        self.dest = dest
        self.name = name

# initialize all drivers path and distance
def initializeDrivers(drivers):
  for i in range(len(drivers)):
    drivers[i].path = []
    drivers[i].dist = 0

# John is the main user
def setMainRiderLocation(riders, src, dest):
  for i in range(len(riders)):
    if riders[i].name == 'John':
      riders[i].src = src
      riders[i].dest = dest

#create an array of drivers 
drivers = []
driver1 = Driver('Node26', 'Toyota', 'Peter')
driver2 = Driver('MOEctr', 'Hyundai', 'Ben')
driver3 = Driver('Node35', 'Mercedez', 'Ryan')
drivers.append(driver1)
drivers.append(driver2)
drivers.append(driver3)

#create an array of riders 
riders = []
rider1 = Rider('bishan', 'marymount', "John")
rider2 = Rider('Node1', 'braddell', "Doe")
rider3 = Rider('Node6', 'braddell', "Timo")
rider4 = Rider('Node28', 'MOEctr', "Calvin")
riders.append(rider1)
riders.append(rider2)
riders.append(rider3)
riders.append(rider4)

# variable for number of drivers and riders
numberOfDrivers = len(drivers)
numberOfRiders = len(riders)

# create a table to contain the distance from driver to all the riders
results = [[0] * numberOfRiders for i in range(numberOfDrivers)]

# put the distance in the table
for i in range(numberOfDrivers):
    for j in range(numberOfRiders):
        results[i][j] = dijkstra(dijkstra_graph, drivers[i].loc, riders[j].src)

# call batchedmatching algo which will produce csv
batchedMatching2(results, drivers, riders)

#reinitialize main rider's location for next algo
setMainRiderLocation(riders, 'bishan', 'MOEctr')
# reset path for drivers
initializeDrivers(drivers)
# call astar algo which will produce csv
normalRide_astar(dijkstra_graph, drivers, riders)

# reinitialize main rider's location for next algo
setMainRiderLocation(riders, 'bishan', 'braddell') 
# reset path for drivers
initializeDrivers(drivers)
# call dijkstra algo which will produce csv
normalRide_dijkstra(dijkstra_graph, drivers, riders)

# reinitialize main rider's location for next algo
setMainRiderLocation(riders, 'marymount', 'braddell')
# reset path for drivers
initializeDrivers(drivers)
# call ridesharing algo which will produce csv
ridesharing(drivers, riders, dijkstra_graph)
riders[1].src='MOEctr'
riders[2].src='Node9'
riders[3].src='Node10'
ridesharing(drivers, riders, dijkstra_graph)
