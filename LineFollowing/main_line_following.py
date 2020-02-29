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
from line_follower import LineFollower
from path_visualizer import TrackedPathPlotter


class LineFollowingTestCase(unittest.TestCase):

    def setUp(self):
        self.linefollower = LineFollower()

    def tearDown(self):
        self.linefollower = None


    def test_1_straight(self):
        # Initial conditions
        x_0 = 0
        y_0 = 5
        theta_0 = - 3.0 * np.pi / 4.0
        X_0 = [x_0, y_0, theta_0] # Initial state

        # Line equation: ax + by + c = 0
        a, b, c = 1.0, 5.0, 4.0
        line = [a, b, c]

        # Vehicle's trajectory
        traj_x, traj_y, traj_theta = self.linefollower.move2pose(X_0, line, params)

        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, line)

    def test_2_turn(self):
        # Initial conditions
        x_0 = 8
        y_0 = 4
        theta_0 = - 3.0 * np.pi / 4.0
        X_0 = [x_0, y_0, theta_0] # Initial state

        # Line equation: ax + by + c = 0
        a, b, c = 1.0, -2.0, 4.0
        line = [a, b, c]

        # Vehicle's trajectory
        traj_x, traj_y, traj_theta = self.linefollower.move2pose(X_0, line, params)

        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, line)


    def test_3_random(self):
        for i in range(nb_of_tests):

            # Initial conditions
            x_0 = 6 * random() - 3
            y_0 = 6 * random() - 3
            theta_0 = 2 * np.pi * random() - np.pi
            X_0 = [x_0, y_0, theta_0] # Initial state

            # Line equation: ax + by + c = 0
            a, b, c = 1.0, -2.0, 0.0
            line = [a, b, c]

            # Vehicle's trajectory
            traj_x, traj_y, traj_theta = self.linefollower.move2pose(X_0, line, params)
            plt.arrow(X_0[0],X_0[1], np.cos(X_0[2]), np.sin(X_0[2]),head_width=0.2, head_length=0.3, length_includes_head=True,width=0.05, color = 'black')
            plt.plot(traj_x, traj_y)


        x = np.linspace(-10,10,100)
        plt.plot(x, -(a/b)*x - c/b, '-b',linewidth=2, label='y=2x+1')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(b=True, which='major', color='black', linestyle='-', linewidth=0.5)
        plt.grid(b=True, which='minor', color='black', linestyle='--', linewidth=0.2)
        plt.minorticks_on()
        plt.xlim([-10,10])
        plt.ylim([-10,10])
        plt.ion()
        plt.show()
        raw_input("Press Enter to close plot...")
        plt.close()



if __name__ == '__main__':
    # Just to avoir creating .pyc files
    sys.dont_write_bytecode = True

    dt = 0.01
    L = 1
    Kd = 0.5
    Kh = 1
    dist_min = 0.5
    gamma_max = np.pi / 4
    params = [dt, L, Kd, Kh, dist_min, gamma_max]

    # Number of random tests done in test_3_random
    nb_of_tests = 5

    unittest.main()
