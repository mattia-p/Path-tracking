# -*- coding: utf-8 -*-
"""
@author: mattia
Waypoint class
"""

class Waypoint():
    """
    Waypoint class
    """
    nbWaypoint = 0

    def __init__(self, x = None, y = None, v = None, i = None):
        self.x = x
        self.y = y
        self.v = v
        self.i = i
        Waypoint.nbWaypoint += 1


    def displayNbWaypoint(self):
        print "Total waypoint %d" % Waypoint.nbWaypoint

    def displayWaypoint(self):
        print "x : ", self.x,  ", y: ", self.y, "i: ", self.i

    def __str__(self):
        return 'Waypoint({}, {}, {})'.format(round(self.x, 2), round(self.y, 2), self.i)
