import pandas as pd

class Node:
    def __init__(self, latitude, longitude,name):
        self.latitude = latitude
        self.longitude = longitude
        self.name=name

# convert path and nodes into coordinates
def nodeConverter(arrayOfPath, arrayOfNodes):
    listForcsv={'Latitude':[], 'Longitude':[]}
    for i in range(len(arrayOfPath)):
        for j in range(len(arrayOfNodes)):
            if arrayOfPath[i]==arrayOfNodes[j].name:
                listForcsv['Latitude'].append(arrayOfNodes[j].latitude)
                listForcsv['Longitude'].append(arrayOfNodes[j].longitude)
    return listForcsv


# ############################ NODES CREATION #########################
# source
bishan = Node(1.350898, 103.848077,'bishan')
# Black line from bishan map diagram
Node1=Node(1.343985, 103.846324,'Node1')
Node2=Node(1.343726, 103.844542,'Node2')
Node3=Node(1.342098, 103.844448,'Node3')
Node4=Node(1.340321, 103.842693,'Node4')
Node8=Node(1.340767, 103.848524,'Node8')

# Red line from bishan map diagram
Node9=Node(1.343148, 103.853641,'Node9')
Node10=Node(1.339083, 103.852493,'Node10')

# Brown line from bishan map diagram
Node5=Node(1.343813, 103.849543,'Node5')
Node6=Node(1.342344, 103.849339,'Node6')
Node7=Node(1.342387, 103.848545,'Node7')

#second routing
# Dark blue line from Junction8 (Bishan) to MOE Lang Centre
Node12 = Node(1.35367345,103.8485965,'Node12')
Node13 = Node(1.353252461,103.8504151,'Node13')

# Grey line from Junction8 (Bishan) to MOE Lang Centre
Node14 = Node(1.347940481,103.8498089,'Node14')
Node15 = Node(1.348007,103.8498598,'Node15')
Node16 = Node(1.350570,103.850626,'Node16')
Node17 = Node(1.351785702,103.8524938,'Node17')
Node38 = Node(1.35213161,103.8525286,'Node38')

# from Junction8 (Bishan) towards Marymount Mrt light-pink highlighted
Node39 = Node(1.348441915,103.8473653, 'Node39')
Node18 = Node(1.348693973,103.8461208, 'Node18')
Node19 = Node(1.347932437,103.8441467, 'Node19')
Node20 = Node(1.346838398,103.8421458, 'Node20')
Node21 = Node(1.347020738,103.8413304, 'Node21')
Node22 = Node(1.347953889,103.8403541, 'Node22')

#from Junction 8 (Bishan) towards Marymount Mrt light-blue highlighted
Node23 = Node(1.352501652,103.8478643, 'Node23')
Node24 = Node(1.352018989,103.8465661, 'Node24')
Node25 = Node(1.352077981,103.8434976, 'Node25')
Node26 = Node(1.353375808,103.840735, 'Node26')
Node27 = Node(1.351332534,103.839941, 'Node27')

#from Junction 8 (Bishan) towards Marymount Mrt green highlighted
Node28 = Node(1.35361714,103.8484168, 'Node28')
Node29 = Node(1.354421578,103.8470542, 'Node29')
Node30 = Node(1.355386903,103.8464534, 'Node30')
Node31 = Node(1.356566745,103.8462174, 'Node31')
Node32 = Node(1.357467714,103.8451338, 'Node32')
Node33 = Node(1.359065861,103.8449943, 'Node33')
Node34 = Node(1.360192072,103.8435566, 'Node34')
Node35 = Node(1.360696185,103.8419473, 'Node35')
Node36 = Node(1.358894248,103.8415396, 'Node36')
Node37 = Node(1.356255696,103.8416684, 'Node37')

# destinations mainly being, MOE centre, Marymount and Braddell
MOEctr = Node(1.352936049,103.8520056,'MOEctr')
marymount = Node(1.348420464, 103.8392812, 'marymount')
braddell = Node(1.3407, 103.8472,'braddell')

#intialize an array of nodes
arrayOfNodes=[bishan,Node1,Node2,Node3,Node4,Node5,Node6,Node7,Node8,Node9,Node10,braddell,Node12,Node13,Node14,Node15,Node16,Node17,Node18,Node19,Node20,Node21,Node22,Node23,Node24,Node25,Node26,Node27,Node28,Node29,Node30,Node31,Node32,Node33,Node34,Node35,Node36,Node37,Node38,Node39,MOEctr, marymount]