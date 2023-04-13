import numpy as np
from Nodes import *
from math import *

#function to calculate the distance between two nodes, using latitude and longitude with respect to earth radius
def getdistance(node1, node2):
    earthradius = 6371  # in km
    latitude_distance = np.radians(node2.latitude) - np.radians(node1.latitude)
    longitude_distance = np.radians(node2.longitude) - np.radians(
        node1.longitude)
    a = sin(latitude_distance / 2) ** 2 + cos(np.radians(node1.latitude)) * cos(
        np.radians(node2.latitude)) * sin(longitude_distance / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    dist = earthradius * c
    return dist

#graph for dijkstra which returns the distance between 2 nodes in dictionary
dijkstra_graph = {
    'bishan': {
        'Node39': getdistance(bishan, Node39),
        'Node28': getdistance(bishan, Node28),
        'Node23': getdistance(bishan, Node23),
    },
    'Node1': {
        'Node2': getdistance(Node1, Node2),
        'Node5': getdistance(Node1, Node5),
        'Node39': getdistance(Node1,Node39),
    },
    'Node2': {
        'Node1': getdistance(Node1, Node2),
        'Node3': getdistance(Node2, Node3)
    },
    'Node3': {
        'Node2': getdistance(Node2, Node3),
        'Node4': getdistance(Node3, Node4)
    },
    'Node4': {
        'Node3': getdistance(Node3, Node4),
        'braddell': getdistance(Node4, braddell)
    },
    'Node5': {
        'Node9': getdistance(Node5, Node9),
        'Node1': getdistance(Node5, Node1),
        'Node6': getdistance(Node5, Node6)
    },
    'Node6': {
        'Node5': getdistance(Node5, Node6),
        'Node7': getdistance(Node6, Node7)
    },
    'Node7': {
        'Node6': getdistance(Node6, Node7),
        'Node8': getdistance(Node7, braddell)
    },
    'Node8': {
        'braddell': getdistance(Node8, braddell),
        'Node7': getdistance(Node8, Node7)
    },
    'Node9': {
        'Node5': getdistance(Node9, Node5),
        'Node10': getdistance(Node9, Node10)
    },
    'Node10': {
        'Node9': getdistance(Node9, Node10),
        'Node8': getdistance(Node10, Node8)
    },
    'braddell': {
        'Node8': getdistance(Node8, braddell),
        'Node4': getdistance(Node4, braddell)
    },
    # dest 2
    # blue
    'Node12': {
        'Node13': getdistance(Node12, Node13),
        'Node39': getdistance(Node12, Node39)
    },
    'Node13': {
        'Node12': getdistance(Node12, Node13),
        'Node14': getdistance(Node13, Node14)
    },
    'Node14': {
        'Node13': getdistance(Node13, Node14),
        'MOEctr': getdistance(Node14, MOEctr)
    },
    # grey
    'Node15': {
        'Node16': getdistance(Node15, Node16),
        'Node39': getdistance(Node15, Node39),
    },
    'Node16': {
        'Node15': getdistance(Node16, Node15),
        'Node17': getdistance(Node16, Node17)
    },
    'Node17': {
        'Node16': getdistance(Node16, Node17),
        'Node38': getdistance(Node17, Node38)
    },
    'Node38': {
        'Node17': getdistance(Node38, Node17),
        'MOEctr': getdistance(Node38, MOEctr)
    },
    'MOEctr': {
        'Node14': getdistance(Node14, MOEctr),
        'Node38': getdistance(MOEctr, Node38)
    },
    # route 3
    'Node18': {
        'Node39': getdistance(Node18, Node39),
        'Node19': getdistance(Node18, Node19),
    },
    'Node19': {
        'Node18': getdistance(Node19, Node18),
        'Node20': getdistance(Node19, Node20)
    },
    'Node20': {
        'Node19': getdistance(Node20, Node19),
        'Node21': getdistance(Node20, Node21),
    },
    'Node21': {
        'Node22': getdistance(Node21, Node22),
        'Node20': getdistance(Node21, Node20)
    },
    'Node22': {
        'Node21': getdistance(Node22, Node21),
        'marymount': getdistance(Node22, marymount)
    },
    'Node23': {
        'bishan': getdistance(Node23, bishan),
        'Node24': getdistance(Node23, Node24)
    },
    'Node24': {
        'Node23': getdistance(Node24, Node23),
        'Node25': getdistance(Node24, Node25)
    },
    'Node25': {
        'Node24': getdistance(Node25, Node24),
        'Node26': getdistance(Node25, Node26)
    },
    'Node26': {
        'Node25': getdistance(Node26, Node25),
        'Node27': getdistance(Node26, Node27),
        'Node37': getdistance(Node26, Node37)
    },
    'Node27': {
        'Node26': getdistance(Node27, Node26),
        'marymount': getdistance(Node27, marymount)
    },
    'Node28': {
        'bishan': getdistance(Node28, bishan),
        'Node29': getdistance(Node28, Node29)
    },
    'Node29': {
        'Node28': getdistance(Node29, Node28),
        'Node30': getdistance(Node29, Node30)
    },
    'Node30': {
        'Node29': getdistance(Node30, Node29),
        'Node31': getdistance(Node30, Node31)
    },
    'Node31': {
        'Node30': getdistance(Node31, Node30),
        'Node32': getdistance(Node31, Node32)
    },
    'Node32': {
        'Node31': getdistance(Node32, Node31),
        'Node33': getdistance(Node32, Node33)
    },
    'Node33': {
        'Node32': getdistance(Node33, Node32),
        'Node34': getdistance(Node33, Node34)
    },
    'Node34': {
        'Node33': getdistance(Node34, Node33),
        'Node35': getdistance(Node34, Node35)
    },
    'Node35': {
        'Node34': getdistance(Node35, Node34),
        'Node36': getdistance(Node35, Node36)
    },
    'Node36': {
        'Node35': getdistance(Node36, Node35),
        'Node37': getdistance(Node36, Node37)
    },
    'Node37': {
        'Node36': getdistance(Node37, Node36),
        'Node26': getdistance(Node37, Node26)
    },
    'Node39': {
        'Node18': getdistance(Node39, Node18),
        'bishan': getdistance(Node39, bishan),
        'Node1': getdistance(Node39,Node1),
        'Node15': getdistance(Node39,Node15),
        'Node12': getdistance(Node39,Node12)
    },
    # destination
    'marymount': {
        'Node22': getdistance(marymount, Node22),
        'Node27': getdistance(marymount, Node27)
    },
}