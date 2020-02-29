# -*- coding: utf-8 -*-
"""
@author: mattia
"""
import numpy as np
import matplotlib.pyplot as plt

class TrackedPathPlotter():
    """
    Used for plotting the path
    """

    @staticmethod
    def path_visualizer(traj_x, traj_y, X_0, line):
        """
        Simple plot for visualizing the trajectory
        """
        a, b, c = line[0], line[1], line[2]

        x = np.linspace(-10,10,100)
        plt.plot(x, -(a/b)*x - c/b, '-r', label='Line to follow')


        plt.plot(traj_x, traj_y, linewidth=2)
        # plt.plot(X_goal[0], X_goal[1], 'ro', label='Target')
        plt.arrow(X_0[0],X_0[1], np.cos(X_0[2]), np.sin(X_0[2]),head_width=0.2, head_length=0.3, length_includes_head=True,width=0.05, color = 'black')

        plt.xlabel('X')
        plt.ylabel('Y')
        # plt.xlim([min(X_0[0],X_goal[0]) - 5, max(X_0[0],X_goal[0]) + 5])
        # plt.ylim([min(X_0[1],X_goal[1]) - 5, max(X_0[1],X_goal[1]) + 5])
        plt.xlim([-10,10])
        plt.ylim([-10,10])
        plt.minorticks_on()
        plt.grid(b=True, which='major', color='black', linestyle='-', linewidth=0.5)
        plt.grid(b=True, which='minor', color='black', linestyle='--', linewidth=0.2)

        plt.ion()
        plt.grid()
        plt.show()
        raw_input("Press Enter to close plot...")
        plt.close()
