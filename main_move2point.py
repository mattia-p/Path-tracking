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
from path_tracker import PathTracker
from path_visualizer import TrackedPathPlotter


class PathTrackingTestCase(unittest.TestCase):

    def setUp(self):
        self.pathtracker = PathTracker()

    def tearDown(self):
        self.pathtracker = None


    def test_1_straight(self):
        x_0 = 0
        y_0 = 0
        theta_0 = np.pi / 2
        X_0 = [x_0, y_0, theta_0]

        x_goal = 0
        y_goal = 10
        X_goal = [x_goal, y_goal]

        traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)

        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, X_goal)

    def test_2_turn(self):
        x_0 = 0
        y_0 = 0
        theta_0 = np.pi / 2
        X_0 = [x_0, y_0, theta_0]

        x_goal = 10
        y_goal = 10
        X_goal = [x_goal, y_goal]

        traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)

        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, X_goal)

    def test_3_turn(self):
        x_0 = 0
        y_0 = 0
        theta_0 = np.pi
        X_0 = [x_0, y_0, theta_0]

        x_goal = 10
        y_goal = 10
        X_goal = [x_goal, y_goal]

        traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)

        TrackedPathPlotter.path_visualizer(traj_x, traj_y, X_0, X_goal)



    def test_4_random(self):
        for i in range(nb_of_tests):

            x_0 = 4 * 10 * random() - 20
            y_0 = 4 * 10 * random() - 20
            theta_0 = 2 * np.pi * random() - np.pi
            X_0 = [x_0, y_0, theta_0]

            x_goal = 0
            y_goal = 0
            X_goal = [x_goal, y_goal]


            traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
            plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
            plt.plot(traj_x, traj_y)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.plot(x_goal, y_goal, 'ro', label='Target')
        plt.grid(b=True, which='major', color='black', linestyle='-', linewidth=0.5)
        plt.grid(b=True, which='minor', color='black', linestyle='--', linewidth=0.2)
        plt.minorticks_on()
        plt.xlim([-22,22])
        plt.ylim([-22,22])
        plt.ion()
        plt.show()
        raw_input("Press Enter to close plot...")
        plt.close()


    # def test_5(self):
    #     x_0 = 8
    #     y_0 = 5
    #     theta_0 = np.pi/2
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #     x_0 = 0
    #     y_0 = 10
    #     theta_0 = np.pi
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #     x_0 = 0
    #     y_0 = -7
    #     theta_0 = np.pi
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #
    #     x_0 = -10
    #     y_0 = 2
    #     theta_0 = np.pi/4
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #
    #     x_0 = 4
    #     y_0 = -5
    #     theta_0 = -np.pi/4
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #     x_0 = -6
    #     y_0 = -4
    #     theta_0 = -np.pi * 1.5
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #
    #     x_0 = 3
    #     y_0 = -8
    #     theta_0 = np.pi/2
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #     x_0 = 6
    #     y_0 = 2
    #     theta_0 = np.pi
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #     x_0 = -11
    #     y_0 = 7
    #     theta_0 = np.pi / 2
    #     X_0 = [x_0, y_0, theta_0]
    #
    #     x_goal = 0
    #     y_goal = 0
    #     X_goal = [x_goal, y_goal]
    #
    #     traj_x, traj_y, traj_theta = self.pathtracker.move2pose(X_0, X_goal, params)
    #     plt.arrow(x_0,y_0, 1.5 * np.cos(theta_0), 1.5 * np.sin(theta_0),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')
    #     plt.plot(traj_x, traj_y)
    #
    #     plt.xlabel('X')
    #     plt.ylabel('Y')
    #     plt.plot(x_goal, y_goal, 'ro', label='Target')
    #     plt.grid(b=True, which='major', color='black', linestyle='-', linewidth=0.5)
    #     plt.grid(b=True, which='minor', color='black', linestyle='--', linewidth=0.2)
    #     plt.minorticks_on()
    #     plt.xlim([-12,12])
    #     plt.ylim([-10,12])
    #     plt.ion()
    #     plt.show()
    #     raw_input("Press Enter to close plot...")
    #     plt.close()






if __name__ == '__main__':
    # Just to avoir creating .pyc files
    sys.dont_write_bytecode = True

    dt = 0.01
    L = 1
    Kv = 0.05
    Kh = 0.5
    dist_min = 0.5
    params = [dt, L, Kv, Kh, dist_min]
    nb_of_tests = 5

    unittest.main()
