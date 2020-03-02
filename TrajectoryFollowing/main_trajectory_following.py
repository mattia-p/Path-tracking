# -*- coding: utf-8 -*-
"""
@author: mattia
Main script for launching some tests
"""

import sys
import unittest
import numpy as np
from random import random
import matplotlib.pyplot as plt
from traj_waypoints import Waypoint
from trajectory_follower import TrajectoryFollower
from path_visualizer import TrackedPathPlotter


class TrajectoryFollowingTestCase(unittest.TestCase):

    def setUp(self):
        self.traj_follower = TrajectoryFollower()

    def tearDown(self):
        self.traj_follower = None


    def test_1_straight_line(self):

        # Initial conditions
        x_0 = -0.5
        y_0 = 0.5
        theta_0 = 0
        X_0 = [x_0, y_0, theta_0] # Initial state

        # Generate trajectory ------------------------------
        # Trajectory to follow - list of waypoints
        traj = []
        list_x = np.linspace(0,20,200)
        i = 0
        for x in list_x:
            wp = Waypoint()
            wp.x = x
            wp.y = x
            wp.i = i
            traj.append(wp)
            i += 1
        # -------------------------------------------------

        traj_x, traj_y, traj_theta = self.traj_follower.follow_traj(X_0, traj, params)
        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, traj)


    def test_3(self):

        # Initial conditions
        x_0 = 0
        y_0 = 0
        theta_0 = 0
        X_0 = [x_0, y_0, theta_0] # Initial state

        # Generate trajectory ------------------------------
        # Trajectory to follow - list of waypoints
        traj = []

        list_x = np.linspace(0,20,200)
        i = 0
        # print list_x
        # wp = Waypoint()
        for x in list_x[0:50]:
            wp = Waypoint()
            wp.x = x
            wp.y = 0
            wp.i = i
            traj.append(wp)
            i += 1

        for x in list_x[50:]:
            wp = Waypoint()
            wp.x = x
            wp.y = 2
            wp.i = i
            traj.append(wp)
            i += 1
        # -------------------------------------------------


        traj_x, traj_y, traj_theta = self.traj_follower.follow_traj(X_0, traj, params)
        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, traj)


    def test_3_sin(self):

        # Initial conditions
        x_0 = 0
        y_0 = 1
        theta_0 = 0
        X_0 = [x_0, y_0, theta_0] # Initial state

    # Generate trajectory ------------------------------
        # Trajectory to follow - list of waypoints
        traj = []

        list_x = np.linspace(0,20,200)
        i = 0
        # print list_x
        # wp = Waypoint()
        for x in list_x:
            wp = Waypoint()
            wp.x = x
            wp.y = np.sin(x)
            wp.i = i
            traj.append(wp)
            i += 1
    # -------------------------------------------------

        traj_x, traj_y, traj_theta = self.traj_follower.follow_traj(X_0, traj, params)
        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, traj)



if __name__ == '__main__':

    dt = 0.01
    L = 1
    Kv = 2     # P for speed
    Ki = 0.05  # I for speed
    Kh = 2     # P for gamma
    gamma_max = np.pi / 3
    look_ahead_dist = 1

    params = [dt, L, Ki, Kh, Kv, gamma_max, look_ahead_dist]


    unittest.main()
